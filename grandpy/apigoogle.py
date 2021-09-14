import requests

from grandpy.customparse import Customparser


class Apigoogle:
    """Class designed to make Api calls to the google maps Api using name of a location to retreive its coordinates."""

    def __init__(self, user_input):
        """Apigoogle class constructor.

        Args:
            user_input (string): parsed string with name of a location.
        """
        cparser = Customparser(user_input)
        self.loc = cparser.get_loc_as_string()
        self.baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"

    def __make_api_call_to_google(self):
        """Method of the Apigoogle class, makes an api call to google maps,
        and returns the response object.

        Returns:
            response object: response from requests.
        """

        apikey = "AIzaSyCzrlC0qJAbxqEJheJHOO-QeztZxRm8f9U"  # os.getenv("KEY")
        listofparamforapicall = self.loc.split(" ")
        stringwithlocparam = ""
        for locwords in listofparamforapicall:
            fin = len(listofparamforapicall) - 1
            if listofparamforapicall.index(locwords) != fin:
                stringwithlocparam += locwords + "+"
            else:
                stringwithlocparam += locwords
        payload = {"address": stringwithlocparam, "key": apikey}

        r = requests.get(self.baseurl, params=payload)

        if r.status_code != 200:
            return "request failed"
        else:
            return r

    def extract_google_data_from_response(self):
        """Method of the Apigoogle class, parse the datas from the response
        object and return them as dict.

        Returns:
            dict: contains name of the location and its coordinates.
        """

        response = self.__make_api_call_to_google()
        if response == "request failed":
            return "request failed"
        else:
            data = response.json()
            coord_and_adress_and_status_dict = (
                data.get("results")[0].get("geometry").get("location")
            )
            coord_and_adress_and_status_dict["address"] = data.get("results")[0].get(
                "formatted_address"
            )
            coord_and_adress_and_status_dict["status_google"] = 200
            return coord_and_adress_and_status_dict
