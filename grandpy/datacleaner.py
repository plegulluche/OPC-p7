import json

from grandpy.apigoogle import Apigoogle
from grandpy.apiwikipedia import Apiwikipedia


class Datacleaner:
    """[summary]
    """
    
    
    def __init__(self,user_input):
        """[summary]

        Args:
            user_input ([type]): [description]
        """
        
        self.user_input = user_input
        self.google = Apigoogle(self.user_input)
        self.google_data = self.google.extract_google_data_from_response()
        print('pierre debug google: ', self.google_data)
        self.wiki = Apiwikipedia(self.google_data)
        self.wiki_data = self.wiki.extract_data_from_wiki()
        print('pierre debug wiki : ', self.wiki_data)
    
    def response_if_all_status_ok(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        
        finalresponse = {"google_response" : self.google_data,
                         "wiki_response" : self.wiki_data}
        jsondata = json.dumps(finalresponse)
        return jsondata