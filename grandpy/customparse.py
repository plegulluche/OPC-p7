import re
import unidecode
from grandpy import config


class Customparser:
    """This class is meant to parse sentences and catch key words when you ask for a direction.
    Languages supported : French.
    """

    def __init__(self, user_input):
        """Customparser class constructor, takes the userinput as arg as a string."""
        self.userinput = user_input

    def __enlever_pronom_avec_apostrophe(self, astring):
        """Strip pronun with apostrophe from a string

        Args:
            astring (str): initial string

        Returns:
            str : return a string without pronoun with apostrophe
        """
        result = re.sub(r"(\b\w')+", "", astring)
        return result

    def __make_all_small_caps(self, astring):
        """Put all Caps in a string into small caps

        Args:
            astring (str): initial string

        Returns:
            str : return a string in small caps
        """
        rawstring = self.__enlever_pronom_avec_apostrophe(astring)
        result = rawstring.lower()
        return result

    def __enlever_les_accents(self, astring):
        """Replace all letters with accents with the same
        letter without accent.

        Args:
            astring (str): initial string

        Returns:
            str : return a string without accentuated letters
        """
        rawstring = self.__make_all_small_caps(astring)
        cleanstring = unidecode.unidecode(rawstring)
        return cleanstring

    def __cut_loc(self, astring):
        """Takes the part of a string where a location is asked (in french only).
           From a stopword that indicate that we are looking for a loc to the next
           punctuation stop (!?.)

        Args:
            astring (str): initial string

        Returns:
            list : return a list of string
        """
        rawstring = self.__enlever_les_accents(astring)
        stop1 = config.locwords
        splittedstring = rawstring.split(" ")
        indexdebut = 0
        for words in splittedstring:
            if words in stop1:
                indexdebut = splittedstring.index(words)
        firstclean = splittedstring[indexdebut::]
        patern = r'\w+\?'
        if len(firstclean) > 1:
            for words in firstclean:
                if re.match(patern, words) is not None:
                    indexfin = firstclean.index(words)
        else:
            return firstclean
                
        cleanlist = firstclean[: indexfin + 1]

        return cleanlist

    def get_loc_as_string(self):
        """From the list of string return by Customparse.__cut_loc() method
           extract the keyword defining the location asked by the user and return it as a string.
        Args:
            alist (list): initial list

        Returns:
            string : return a string with a location
        """
        rawlist = self.__cut_loc(self.userinput)
        put_in_string = " ".join(rawlist)
        newstring = re.sub("[?!.,]", "", put_in_string)
        make_a_list = newstring.split(" ")
        for words in config.stopwords:
            while words in make_a_list:
                make_a_list.remove(words)
        for words in config.locwords:
            while words in make_a_list:
                make_a_list.remove(words)
        finalstring = " ".join(make_a_list)
        return finalstring
