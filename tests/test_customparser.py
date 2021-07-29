from grandpy.customparse import Customparser




def test_parse_enleve_apostrophes():
    leparser = Customparser()
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la j'tour eiffel?"
    result = leparser.get_loc_as_string(astring)
    assert result == "tour eiffel"
    
def test_parse_met_en_minuscules():
    leparser = Customparser()
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la Tour Eiffel?"
    result = leparser.get_loc_as_string(astring)
    assert result == "tour eiffel"

def test_parse_enleve_accents():
    leparser = Customparser()
    astring = "j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la Tour Eiffél?"
    result = leparser.get_loc_as_string(astring)
    assert result == "tour eiffel"
    


def test_parser_get_loc_as_string():
    leparser = Customparser()
    astring = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
    result = leparser.get_loc_as_string(astring)
    assert result == "tour eiffel"
    