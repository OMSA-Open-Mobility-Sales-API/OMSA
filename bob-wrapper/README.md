# BoB wrapper

In this directory, you'll find 2 tools: one to simulate a BoB server, and another that wraps it and publishes an OMSA interface.  
This is an example demo setup, and not usable for production environments.

- [BoB wrapper](#bob-wrapper)
  - [Installation guide](#installation-guide)
  - [BoB Server](#bob-server)
    - [Start](#start)
    - [Test](#test)
    - [Implementation details](#implementation-details)
  - [OMSA wrapper server](#omsa-wrapper-server)
    - [Start](#start-1)
    - [Test](#test-1)
    - [Implementation details](#implementation-details-1)

## Installation guide

Both tools are build with Node.js, this is what you have to install at first.  
When installed, you have to open a terminal (or powershell), and navigate to this folder.  
Execute `npm install jsonata express @apidevtools/swagger-parser openapi-sampler axios`.  
You're ready!

## BoB Server

### Start

To start the BoB server, open a new terminal/shell, navigate to this folder.
Execute `node ./bob.js`.

### Test

You can test it, see if it works by executing in another terminal this command:  
`curl -X POST http://localhost:3001/v1/product`

It will return a JSON result.

### Implementation details

This server is created using the OpenAPI Sampler library, generating a JSON output that complies to the BoB definition in the OpenAPI specification (expressed in the file BoB-product-340.yaml).  
  
If you want to replace this generated output, you'll have to modify the BoB.js, for instance to publish JSON output provided in files.

## OMSA wrapper server

### Start

To start the OMSA server, open a new terminal/shell, navigate to this folder.
Execute `node ./omsa.js`.

### Test

You can test it, see if it works by executing in another terminal this command:  
`curl -X GET http://localhost:3000/v1/`

It will return a JSON result, representing the landing page.

### Implementation details

It created using the JSONATA library. Please have a look to understand what it does.  
Source: https://www.npmjs.com/package/jsonata
Reference implementation of the [JSONata query and transformation language](http://jsonata.org/).

* [JSONata in 5 minutes](https://www.youtube.com/embed/ZBaK40rtIBM)
* [JSONata language documentation](http://docs.jsonata.org/)
* [Try it out!](http://try.jsonata.org/)

When the server is started, the OMSA OpenAPI specification is read and the endpoints are initiated whenever a corresponding file is found in the `/requests` folder.

If you want to extend this example, or just want to modify the mapping (requests from OMSA->BoB or responses from BoB->OMSA), you'll have to modify the files in the `/requests` or `/responses` folders. The name of the file corresponds with the operationId from the OMSA endpoint.
