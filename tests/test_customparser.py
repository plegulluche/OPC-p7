from grandpy.customparse import Customparser




def test_parse_enleve_apostrophes():
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la j'tour eiffel?"
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "tour eiffel"
    
def test_parse_met_en_minuscules():
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la Tour Eiffel?"
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "tour eiffel"

def test_parse_enleve_accents():
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la Tour Eiffél?"
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "tour eiffel"
    


def test_parser_get_loc_as_string():
    astring = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "tour eiffel"

def test_parser_get_loc_and_city():
    astring = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    leparser = Customparser(astring)
    result = leparser.get_loc_as_string()
    assert result == "musee art histoire fribourg"