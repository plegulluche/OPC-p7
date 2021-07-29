import grandpy
from grandpy.apigoogle import Apigoogle
from grandpy.customparse import Customparser
#a verifier : -status 200 (ok) 
#           : -status 403 (forbidden : key problem)
#           : -status 400 bad request
#           : que le retour est bien une image
#           : que l image n est pas vide ? 



def test_make_api_call_check_status_code_equals_200(mocker):
    mocker.patch("grandpy.customparse.Customparser.get_loc_as_string", return_value = "tour eiffel paris")
    api = Apigoogle()
    response = api.make_api_call_to_google()
    assert response.status_code == 200
    
def test_make_api_call_gets_an_image(mocker):
    mocker.patch("grandpy.customparse.Customparser.get_loc_as_string", return_value = "tour eiffel paris")
    api = Apigoogle()
    response = api.make_api_call_to_google()
    response_body = response.headers
    assert response_body["Content-Type"] == "image/png"
    






