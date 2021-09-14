from grandpy.customparse import Customparser


def test_parser_get_loc_as_string():
    astring = (
        "Bonsoir Grandpy, j'espère que tu as passé une belle semaine."
        " Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel"
        " a Paris? Merci d'avance et salutations à Mamie."
    )
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "tour eiffel paris"


def test_parser_get_loc_and_city():
    astring = (
        "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir?"
        " Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se "
        "trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    )
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "musee art histoire fribourg"


def test_parser_get_loc_and_city2():
    astring = (
        "Salut Grandpy! pourrai tu me donner l'adresse de l'arc de triomphe a paris?"
    )
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "arc triomphe paris"


def test_parser_dont_crash():
    astring = "Salut"
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "salut"
