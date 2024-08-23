import threading
from name_utils import NameUtils

class CholloProcessor:

    def __init__(self):
        self.in_market_holder = []
        self.list_of_chollos_holder = []
        self.results_holder = []

    def run(self, mister, af):
        t1 = threading.Thread(target=lambda: self.in_market_holder.append(mister.getPlayersCurrentMister()))
        t2 = threading.Thread(target=lambda: self.list_of_chollos_holder.append(af.retrieve_chollos()))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        in_market = self.in_market_holder[0]
        list_of_chollos = self.list_of_chollos_holder[0]

        chollos_dict = NameUtils.build_chollos_dict(list_of_chollos)
        results = NameUtils.find_coincidences(in_market, chollos_dict)

        self.results_holder.extend(results)

    def print_results(self):
        if not self.results_holder:
            print("No chollos in the market. Save the money for tomorrow!")
        else:
            for player, chollo in self.results_holder:
                print(f"You should sign {player}, found in the list as {chollo}")