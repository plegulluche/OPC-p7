import requests
from dotenv import dotenv_values

from grandpy.customparse import Customparser



class Apigoogle:
    
    def __init__(self):
        self.loc = Customparser.get_loc_as_string()
        self.key = dotenv_values(".env")
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?"
          
    
    def make_api_call_to_google(self):
        for key, values in self.key.items():
            apikey = values 
        listofparamforapicall = self.loc.split(" ")
        stringwithlocparam = ""
        for locwords in listofparamforapicall:
            fin = len(listofparamforapicall) -1
            if listofparamforapicall.index(locwords) != fin:
                stringwithlocparam += locwords + "+"
            else:
                stringwithlocparam += locwords
        payload = {'address=': locwords,'key': apikey}
        
        r = requests.get(self.url, params=payload)
        
        if r.status_code == 400:
            return "BAD REQUEST"
        elif r.status_code == 403:
            return "FORBIDDEN KEY MUST BE INVALID"
        elif r.status_code == 200:
            return r
              
    
    def get_coord_from_response(self):
        
        response = self.make_api_call_to_google()
        data = response.json()
        coord = data.get("results")[0].get("geometry").get("location")
        
        return coord
    

        
        

    
    