import json
from grandpy.apigoogle import Apigoogle


def mock_requestget(*args,**kwarg):
        
        class mock_response:
         
            def __init__(self):
                datastructure = {
                "results": [
                    {
                        "adress_components": ["some irrelevants components"],
                        "formatted_adress" : "adress full text mode, single string",
                        "geometry" : {
                            "location" : {
                                "lat" : 48.85837009999999,
                                "lng" : 2.2944813
                            }
                        }
                    
                }]}
                self.data = json.dumps(datastructure)
                self.status_code = self.status()
            def status(self):
                return 200
            def json(self):
                return json.loads(self.data)
            
        response = mock_response()
        return response
    
def mock_parser():
    return "tour eiffel paris"
    
def test_response_status_is_200(mocker):
          
    mocker.patch('requests.get', mock_requestget)
    mocker.patch('grandpy.customparse.Customparser.get_loc_as_string', mock_parser)
    api = Apigoogle()
    result = api.make_api_call_to_google()
    assert result.status_code == 200
    


def test_requestget_gets_coordinates(mocker):
    
    mocker.patch('requests.get', mock_requestget)
    mocker.patch('grandpy.customparse.Customparser.get_loc_as_string', mock_parser)
    api = Apigoogle()
    result = api.get_coord_from_response()
    assert result == {"lat" : 48.85837009999999 , "lng" : 2.2944813}
        



