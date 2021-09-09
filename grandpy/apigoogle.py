import requests
from dotenv import dotenv_values

from grandpy.customparse import Customparser



class Apigoogle:
    """[summary]
    """
    
    def __init__(self,user_input):
        """[summary]

        Args:
            user_input ([type]): [description]
        """
        cparser = Customparser(user_input)
        self.loc = cparser.get_loc_as_string()
        self.key = dotenv_values(".env")
        self.baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
          
    
    def __make_api_call_to_google(self):
        """[summary]

        Returns:
            [type]: [description]
        """
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
        payload = {'address': stringwithlocparam,'key': apikey}
        
        r = requests.get(self.baseurl, params=payload)


        
        if r.status_code != 200:
            return "request failed"
        else:
            return r
              
    
    def extract_google_data_from_response(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        
        response = self.__make_api_call_to_google()
        if response == "request failed":
            return "request failed"
        else:
            data = response.json()
            coord_and_adress_and_status_dict = data.get("results")[0].get("geometry").get("location")
            coord_and_adress_and_status_dict["address"] = data.get("results")[0].get("formatted_address")
            coord_and_adress_and_status_dict["status_google"] = 200
            return coord_and_adress_and_status_dict
        

        
        

    
    