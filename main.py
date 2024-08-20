import MisterMDSide as mister
import AnaliticasFantasy as af
import unicodedata
from collections import defaultdict

def normalize_string(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def build_chollos_dict(list_of_chollos):
    chollos_dict = defaultdict(list)
    for chollo in list_of_chollos:
        chollo_parts = chollo.split()
        chollo_firstname = chollo_parts[0] if len(chollo_parts) > 1 else None
        chollo_surname = chollo_parts[-1]

        if chollo_surname.lower() in ("jr", "jr.", "junior", "júnior"):
            chollo_surname = None

        # Normalize the names
        normalized_chollo_surname = normalize_string(chollo_surname)
        normalized_chollo_firstname = normalize_string(chollo_firstname) if chollo_firstname else None

        if normalized_chollo_surname:
            chollos_dict[normalized_chollo_surname].append((normalized_chollo_firstname, chollo))
    
    return chollos_dict

def find_coincidences(in_market, chollos_dict):
    results = []
    for player in in_market:
        player_parts = player.split()
        player_firstname = player_parts[0] if len(player_parts) > 1 else None
        player_surname = player_parts[-1]  # Get last name

        if player_surname.lower() in ("jr", "jr.", "junior", "júnior"):
            player_surname = None

        # Normalize player names
        normalized_player_surname = normalize_string(player_surname)
        normalized_player_firstname = normalize_string(player_firstname) if player_firstname else None

        if normalized_player_surname in chollos_dict:
            for chollo_firstname, chollo in chollos_dict[normalized_player_surname]:
                # Compare first names if both are available
                if normalized_player_firstname and chollo_firstname:
                    if normalized_player_firstname == chollo_firstname:
                        results.append((player, chollo))
                else:  # We accept the result if one side didn't have the first name
                    results.append((player, chollo))
    
    return results

def main():
    in_market = mister.getPlayersCurrentMister()
    list_of_chollos = af.retrieve_chollos()
    chollos_dict = build_chollos_dict(list_of_chollos)
    results = find_coincidences(in_market, chollos_dict)
    if not results:
        print("No chollos in the market. Save the money for tomorrow!")
    else:
        for player, chollo in results:
            print(f"You should sign {player}, found in the list as {chollo}")

if __name__ == "__main__":
    main()
