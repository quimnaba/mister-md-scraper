import MisterMDSide as mister
import AnaliticasFantasy as af

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
    for chollo in list_of_chollos:
        chollo_parts = chollo.split()
        chollo_firstname = chollo_parts[0] if len(chollo_parts) > 1 else None
        chollo_surname = chollo_parts[-1]
        match = player_surname == chollo_surname
        if match:
            if player_firstname and chollo_firstname:  # Check first names if both are available
                if player_firstname == chollo_firstname:
                    results.append((player, chollo))
            else:
                results.append((player, chollo))
if not results:
    print("No chollos in the market. Save the money for tomorrow!")
for player, chollo in results:
    print(f"You should sign: {player} Found in the list as {chollo}")


