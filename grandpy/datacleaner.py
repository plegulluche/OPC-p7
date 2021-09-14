import json

from grandpy.apigoogle import Apigoogle
from grandpy.apiwikipedia import Apiwikipedia


class Datacleaner:
    """Class that calls the Apigoogle and Apiwikipedia classes 
       and construct a json object with the data returned from those classes.
    """

    def __init__(self, user_input):
        """Datacleaner class constructor.

        Args:
            user_input (string): the user input entered in the app.
        """

        self.user_input = user_input
        self.google = Apigoogle(self.user_input)
        self.google_data = self.google.extract_google_data_from_response()
        self.wiki = Apiwikipedia(self.google_data)
        self.wiki_data = self.wiki.extract_data_from_wiki()

    def response_if_all_status_ok(self):
        """Datacleaner class method,
        build a json object with the data from the calls
        to the Api classes.

        Returns:
            [json]: a json object with the data.
        """

        finalresponse = {
            "google_response": self.google_data,
            "wiki_response": self.wiki_data,
        }
        jsondata = json.dumps(finalresponse)
        return jsondata
