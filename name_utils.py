import unicodedata
from collections import defaultdict

class NameUtils:

    @staticmethod
    def normalize_string(s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        ).lower()

    @staticmethod
    def get_name_parts(full_name):
        name_parts = full_name.split()
        firstname = name_parts[0] if len(name_parts) > 1 else None
        surname = name_parts[-1]

        if surname and surname.lower() in ("jr", "jr.", "junior", "júnior"):
            surname = None

        normalized_surname = NameUtils.normalize_string(surname) if surname else None
        normalized_firstname = NameUtils.normalize_string(firstname) if firstname else None

        return normalized_firstname, normalized_surname

    @staticmethod
    def build_chollos_dict(list_of_chollos):
        chollos_dict = defaultdict(dict)
        for chollo in list_of_chollos:
            chollo_firstname, chollo_surname = NameUtils.get_name_parts(chollo)
            if chollo_surname:
                chollos_dict[chollo_surname][chollo_firstname] = chollo

        return chollos_dict

    @staticmethod
    def find_coincidences(in_market, chollos_dict):
        results = []
        for player in in_market:
            player_firstname, player_surname = NameUtils.get_name_parts(player)
            if player_surname in chollos_dict:
                if player_firstname in chollos_dict[player_surname]:
                    chollo = chollos_dict[player_surname][player_firstname]
                    results.append((player, chollo))
                elif None in chollos_dict[player_surname]:
                    chollo = chollos_dict[player_surname][None]
                    results.append((player, chollo))
        return results