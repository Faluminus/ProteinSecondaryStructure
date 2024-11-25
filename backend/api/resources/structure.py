from flask import request, jsonify
from api.controller import Controller
from threading import Thread
from flask_restful import Resource
from flasgger import swag_from

controller = Controller()


class GetStructure(Resource):
    
    @swag_from({
        'responses': {
            200: {
                'description': 'A status code 200 means successful and returns a list of items.',
                'content': {
                    'application/json': {
                        'examples': {
                            'example1': {
                                'summary': 'Successful response',
                                'output': 'CCCCSSSCCSSCCCCCCCEEEECTTCCEEEEECCTTSCTTTCEEEETTCCCTTHHHHHHHHHHC'
                            }
                        }
                    }
                }
            },
            202: {
                'description': 'A status code 202 means accepted and sends link in header.',
                'content': {
                    'application/json': {
                        
                    }
                }
            }
        }
    })
    def post(self):
        return self.__return_status()
    
    def __return_status(self):
        thread = Thread(target = self.__get_structure,args=())
        thread.run()
        response = jsonify({}), 202
        response.headers["Location"] = "https://example.com/your-redirect-link"
        return response
        
    def __get_structure():
        return controller.get_structure(request.data)
