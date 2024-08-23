import MisterMDSide as mister
import AnaliticasFantasy as af
from chollo_processor import CholloProcessor

def main():
    processor = CholloProcessor()
    processor.run(mister, af)
    processor.print_results()

if __name__ == "__main__":
    main()