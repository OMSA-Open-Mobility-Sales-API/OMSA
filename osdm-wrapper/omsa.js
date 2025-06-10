const express = require('express');
const SwaggerParser = require('@apidevtools/swagger-parser');
const path = require('path');

const bodyParser = require('body-parser');
const jsonata = require('jsonata');
const fs = require('fs');
const endpointMap = require(path.join(__dirname, 'endpoint-mapping.json'));
const axios = require('axios');

const app = express();
const port = 3000;
const requestsDir = path.join(__dirname, 'requests');
const responsesDir = path.join(__dirname, 'responses');

// Laad en dereference de OpenAPI spec
const openApiV2 = path.join(__dirname, 'OMSA-001.yaml');

async function postToOSDM(url, body) {
  console.log(`calling http://localhost:3001${url}`);
  try {
    const response = await axios.post('http://localhost:3001' + url, body);
    return response
  } catch (error) {
    console.error('Fout:', error.message);
  }
}

function addPost(baseRoutePath, methods) {
    if (methods.post && methods.post.operationId) {
        toAdd = {}
        operation = methods.post.operationId;
        if (baseRoutePath.includes('{')) {
            methods.post.parameters.forEach((p, i) => {
                if (p.in === 'path' && p.schema?.enum){
                    p.schema.enum.forEach( (enumValue, i2) => {
                        o2 = operation + '-' + enumValue;
                        r2 = baseRoutePath.replace('{' + p.name + '}', enumValue );
                        toAdd[o2] = r2;
                    });
                }
            });
        }
        else {
            toAdd[operation] = baseRoutePath;
        }

        Object.entries(toAdd).forEach( ([operationId, routePath]) => {
            const requestPath = path.join(requestsDir, `${operationId}.jsonata`);
            const responsePath = path.join(responsesDir, `${operationId}.jsonata`);

            if( !fs.existsSync(requestPath) )
                return;

            app.post(routePath, (req, res) => {
                const data = req.body;
                // data.bbox = req.params.bbox ? req.params.bbox : [0,0,1,1];

                fs.readFile(requestPath, 'utf8', (err, expressionText) => {
                    if (err) {
                        return res.status(500).json({ error: `Kan expressie niet lezen voor '${operationId}': ${err.message}` });
                    }

                    try {
                        (async() => { 
                            const expression = jsonata(expressionText);
                            body = await expression.evaluate(data);
                            
                            url = endpointMap[operationId];

                            if (url === 'none') {
                              res.json(body);
                              return;
                            }

                            if (url instanceof Array){
                                result1 = postToOSDM(url[0], body)
                                result2 = postToOSDM(url[1], "{}")
                                res.json(result2, body);
                                return;
                            }

                            callUrl(url, responsePath, res);
                        })()
                    } catch (e) {
                        res.status(400).json({ error: `Fout in JSONata expressie: ${e.message}` });
                    }
                });
            });
            msg = `Endpoint geladen: POST ${routePath} => request/${operationId}.jsonata`;

            if (operationId in endpointMap) {
                msg += ' | ' + endpointMap[operationId] + ` | response/${operationId}.jsonata`
            }
            
            console.log(msg);
        } );
    }
}

async function callUrl(url, responsePath, res) {
    if (url.includes("{") ) {
        const match = url.match(/{([^}]+)}/);
        if (match) {
            toFind = match[1];
        }
        id = data.inputs[toFind];
        url = url.replace(/{(\w+)}/g, id);
    }

    url = url.replace('POST ', '').replace('GET ', '');

    result = await postToOSDM(url, body);

    fs.readFile(responsePath, 'utf8', (err, responseJsonata) => {
        (async() => {
            const responseExpression = jsonata(responseJsonata);
            const resp = await responseExpression.evaluate(result.data);
            res.json(resp);
        })()}
    ) 
}

function addGet(routePath, methods) {
    if (methods.get && methods.get.operationId) {
        const operationId = methods.get.operationId;
        const requestPath = path.join(requestsDir, `${operationId}.jsonata`);

        msg = `Endpoint geladen: GET ${routePath} => ${operationId}.jsonata`
        if (operationId == 'openApi') {
            msg = `Endpoint geladen: GET ${routePath} => TOMP-API.yaml`
        }

        if(operationId != 'openApi' && !fs.existsSync(requestPath))
            return;

        app.get(routePath, (req, res) => {
            const data = req.query;

            if (operationId == 'openApi' ){
                fs.readFile(openApi, (err, content) => { 
                    res.send(content); 
                } );
                return;
            }

            fs.readFile(requestPath, 'utf8', (err, expressionText) => {
                if (err) {
                    return res.status(500).json({ error: `Kan expressie niet lezen voor '${operationId}': ${err.message}` });
                }

                    (async() => { 
                      try {
                        const expression = jsonata(expressionText);
                        const result = await expression.evaluate(data);
                        res.json(result);
                      } catch (e) {
                        res.status(400).json({ error: `Fout in JSONata expressie: ${e.message}` });
                      }
                    })()                    
            });
        });

        console.log(msg);
    }
}

app.use(bodyParser.json());

// Laad en parse de OpenAPI specificatie
if( !fs.existsSync(openApiV2) )
    return;

SwaggerParser.dereference(openApiV2)
  .then(api => {
    console.log('OpenAPI succesvol geladen en dereferenced.');
    setupServer(api); 
  })
  .catch(err => {
    console.error('Fout bij parsen/dereferencing van OpenAPI:', err.message);
    process.exit(1);
  });

function setupServer(openapi) {
    for (const [routePath, methods] of Object.entries(openapi.paths)) {
        route = '/v1' + routePath;
        addPost(route, methods);
        addGet(route, methods);
    }
}

app.listen(port, () => {
  console.log(`Server draait op http://localhost:${port}`);
});