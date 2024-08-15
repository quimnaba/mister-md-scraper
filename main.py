import MisterMDSide as mister
import AnaliticasFantasy as af
import unicodedata


def normalize_string(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def main():

    #GET MARKET PLAYERS
    in_market = mister.getPlayersCurrentMister()
    #GET CHOLLOS
    list_of_chollos = af.retrieve_chollos()

    #FIND COINCIDENCES
    results = []
    for player in in_market:
        player_parts = player.split()
        player_firstname = player_parts[0] if len(player_parts) > 1 else None
        player_surname = player.split()[-1] #Get last name


        if player_surname == ("Jr" or "Jr." or "Junior" or "Júnior"):
            player_surname = None

        # Normalize names
        normalized_player_surname = normalize_string(player_surname)
        normalized_player_firstname = normalize_string(player_firstname) if player_firstname else None

        for chollo in list_of_chollos:
            chollo_parts = chollo.split()
            chollo_firstname = chollo_parts[0] if len(chollo_parts) > 1 else None
            chollo_surname = chollo_parts[-1]

            if chollo_surname == ("Jr" or "Jr." or "Junior" or "Júnior"):
                chollo_surname = None

            # Normalize chollo names
            normalized_chollo_surname = normalize_string(chollo_surname)
            normalized_chollo_firstname = normalize_string(chollo_firstname) if chollo_firstname else None

            match = normalized_player_surname == normalized_chollo_surname
            if match:
                if normalized_player_firstname and normalized_chollo_firstname:  # Check first names if both are available
                    if normalized_player_firstname == normalized_chollo_firstname:
                        results.append((player, chollo))
                else: #! We accept the result if one side didn't have the first name
                    results.append((player, chollo))
    if not results:
        print("No chollos in the market. Save the money for tomorrow!")
    for player, chollo in results:
        print(f"You should sign {player}, found in the list as {chollo}")

if __name__ == "__main__":
    main()



