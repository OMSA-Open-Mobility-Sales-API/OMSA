from flask import Flask, request, send_file, make_response
from ogcProcesses import processExecutor
from ogcCollections import collectionRetriever

app = Flask(__name__)

@app.route('/collections/<id>/items', methods=['GET'])
def handle_collection(id):
    output =  collectionRetriever(request, id).items()

    response = make_response(output)        
    response.headers['Version'] = '0.0.1'
    response.headers['Content-Type'] = format
    response.headers['Content-Language'] = request.headers.get("Content-Language")
    response.status_code = 200

    return response

@app.route('/processes/<id>/execute', methods=['POST'])
def handle_process(id):
    output = processExecutor(request, id).execute()
    
    response = make_response(output)        
    response.headers['Version'] = '0.0.1'
    response.headers['Content-Type'] = format
    response.headers['Content-Language'] = request.headers.get("Content-Language")
    response.status_code = 200

    return response

# OGC Section
@app.route('/collections/<id>', methods=['GET'])
@app.route('/processes/<id>', methods=['GET'])
def handle_meta_data_id(id):
    file, format, language = get_file_and_format(request, id)

    response = make_response(send_file(file, as_attachment=False))        
    response.headers['Version'] = '0.0.1'
    response.headers['Content-Type'] = format
    response.headers['Content-Language'] = language
    response.status_code = 200

    return response

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
@app.route('/conformance', methods=['GET'])
@app.route('/collections', methods=['GET'])
@app.route('/processes', methods=['GET'])
def handle_meta_data():
    id = request.base_url.replace(request.root_url, '')
    if id == '':
        id = 'landingpage'

    file, format, language = get_file_and_format(request, id)

    response = make_response(send_file(file, as_attachment=False))        
    response.headers['Version'] = '0.0.1'
    response.headers['Content-Type'] = format
    response.headers['Content-Language'] = language
    response.status_code = 200

    return response

def get_file_and_format(r, id):
    language = r.headers.get("Content-Language")
    if language == None:
        language = 'en-US'
    file = id    
    format = r.args.get('f')
    file = file + '.' + language[:2]
    if (format == 'html'):
        format = 'text/html'
        file = file + '.html' 
    else:
        format = 'application/json'
        file = file + '.json' 
    
    folder = './responses/'
    if id == 'api':
        '../common.yaml'
        format = 'application/yaml'
    return folder + file, format, language

if __name__ == '__main__':
    app.run(debug=True)