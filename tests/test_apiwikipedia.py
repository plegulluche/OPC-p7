import json

from grandpy.apiwikipedia import Apiwikipedia


def mock_requestget(*args, **kwarg):

    data_structure_geo_search = {
        "batchcomplete": "",
        "query": {
            "geosearch": [
                {
                    "pageid": 1359783,
                    "ns": 0,
                    "title": "Tour Eiffel",
                    "lat": 48.858296,
                    "lon": 2.294479,
                    "dist": 8.2,
                    "primary": "",
                }
            ]
        },
    }
    data_structure_extract = {
        "batchcomplete": "",
        "query": {
            "pages": {
                "1359783": {
                    "pageid": 1359783,
                    "ns": 0,
                    "title": "Tour Eiffel",
                    "extract": "La tour Eiffel  est une tour de fer puddlé de 324 "
                    "mètres de hauteur (avec antennes) située à Paris,"
                    " à l’extrémité nord-ouest du parc du Champ-de-Mars "
                    "en bordure de la Seine dans le 7e arrondissement."
                    " Son adresse officielle est 5, avenue Anatole-France."
                    "\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs"
                    " pour l’Exposition universelle de Paris de 1889, et"
                    " initialement nommée « tour de 300 mètres », elle est"
                    " devenue le symbole de la capitale française et "
                    "un site touristique de premier plan : il s’agit du troisième "
                    "site culturel français payant le plus visité en 2015, avec"
                    " 5,9 millions de visiteurs en 2016. Depuis son ouverture "
                    "au public, elle a accueilli plus de 300 millions de visiteurs."
                    "\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est "
                    "restée le monument le plus élevé du monde pendant quarante ans."
                    " Le second niveau du troisième étage, appelé parfois quatrième étage,"
                    " situé à 279,11 mètres, est la plus haute plateforme d'observation"
                    " accessible au public de l'Union européenne et la deuxième plus haute "
                    "d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres."
                    " La hauteur de la tour a été plusieurs fois augmentée par l’installation "
                    "de nombreuses antennes. Utilisée dans le passé pour de nombreuses "
                    "expériences scientifiques, elle sert aujourd’hui "
                    "d’émetteur de programmes radiophoniques et télévisés.",
                }
            }
        },
    }

    class mock_response:
        def __init__(self, data):
            self.data = json.dumps(data)
            self.status_code = self.status()

        def status(self):
            return 200

        def json(self):
            return json.loads(self.data)

    if (
        args[0] == "https://fr.wikipedia.org/w/api.php?action=query&format=json"
        "&prop=extracts&exintro&explaintext&redirects&list=geosearch"
    ):
        response = mock_response(data_structure_geo_search)
    elif (
        args[0] == "https://fr.wikipedia.org/w/api.php?format=json"
        "&action=query&prop=extracts&exintro&explaintext&redirects=1"
    ):
        response = mock_response(data_structure_extract)

    return response


datas = {
    "lat": 48.85837009999999,
    "lng": 2.2944813,
    "status": 200,
    "address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France",
}


def test_wiki_api_call_status_ok(mocker):
    mocker.patch("requests.get", mock_requestget)
    wiki = Apiwikipedia(datas)
    result = wiki.extract_data_from_wiki()
    assert result != "request failed"


def test_wiki_api_call_returns_correct_datas(mocker):
    mocker.patch("requests.get", mock_requestget)
    wiki = Apiwikipedia(datas)
    result = wiki.extract_data_from_wiki()
    assert result == {
        "extract": "La tour Eiffel  est une tour de fer puddlé de 324 "
        "mètres de hauteur (avec antennes) située à Paris,"
        " à l’extrémité nord-ouest du parc du Champ-de-Mars "
        "en bordure de la Seine dans le 7e arrondissement."
        " Son adresse officielle est 5, avenue Anatole-France."
        "\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs"
        " pour l’Exposition universelle de Paris de 1889, et"
        " initialement nommée « tour de 300 mètres », elle est"
        " devenue le symbole de la capitale française et "
        "un site touristique de premier plan : il s’agit du troisième "
        "site culturel français payant le plus visité en 2015, avec"
        " 5,9 millions de visiteurs en 2016. Depuis son ouverture "
        "au public, elle a accueilli plus de 300 millions de visiteurs."
        "\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est "
        "restée le monument le plus élevé du monde pendant quarante ans."
        " Le second niveau du troisième étage, appelé parfois quatrième étage,"
        " situé à 279,11 mètres, est la plus haute plateforme d'observation"
        " accessible au public de l'Union européenne et la deuxième plus haute "
        "d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres."
        " La hauteur de la tour a été plusieurs fois augmentée par l’installation "
        "de nombreuses antennes. Utilisée dans le passé pour de nombreuses "
        "expériences scientifiques, elle sert aujourd’hui "
        "d’émetteur de programmes radiophoniques et télévisés.",
        "status_wikipedia": 200,
        "url_wikipedia": "https://fr.wikipedia.org/?curid=1359783",
    }
