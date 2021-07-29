import requests
import os
from dotenv import load_dotenv

from grandpy.customparse import Customparser


#TODO: -generer l'url sans la clef api.
#TODO: -generer l'url avec la clef mise en variable d'environnement.
#TODO: -Faire la requete a l'Api google maps et recup l'image? 

class Apigoogle:
    
    def __init__(self):
        self.loc = Customparser.get_loc_as_string()
        self.key = "key"
    
    def make_api_call_to_google(self):
        return "nein"
    
    
    