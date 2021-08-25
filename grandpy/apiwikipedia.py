import requests
from grandpy.apigoogle import Apigoogle



class Apiwikipedia:
    """[summary]
    """
    
    def __init__(self,data_dict):
        """[summary]

        Args:
            data_dict ([type]): [description]
        """
        self.google_datas = data_dict
        self.base_url_for_geo_search = "https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&explaintext&redirects&list=geosearch"
        self.base_url_for_abstract = "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1"
        self.page_id = 0
    
    def __make_api_call_to_wikipedia(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        for key,values in self.google_datas.items():
            if key == "lat":
                lat = values
            elif key == "lng":
                lng = values
        payload = {'gscoord' : f"{lat}|{lng}", 'gsradius' : 10}
        
        r_page_id = requests.get(self.base_url_for_geo_search, params=payload)
        
        if r_page_id.status_code != 200:
            return "request failed"
        else:
            pageiddatas = r_page_id.json()['query']['geosearch'][0]['pageid']
            self.page_id = pageiddatas
        
        payload = {'pageids' : pageiddatas}
        
        r_extract = requests.get(self.base_url_for_abstract, params=payload)
        
        if r_extract.status_code != 200:
            return "request failed"
        else:
            return r_extract
        
    
    def extract_data_from_wiki(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        data_wiki = {}
        raw_data = self.__make_api_call_to_wikipedia()
        if raw_data == "request failed":
            return "request failed"
        else:
            clean_data = raw_data.json()
            data_wiki["status_wikipedia"] = 200
            data_wiki["extract"] = clean_data["query"]["pages"][f"{self.page_id}"]["extract"]
            data_wiki["url_wikipedia"] = f"https://fr.wikipedia.org/?curid={self.page_id}"
        return data_wiki