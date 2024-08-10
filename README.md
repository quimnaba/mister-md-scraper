# MD Fantasy Football Chollo Finder

This Python script helps you to identify players available in the market who are considered "chollos" **(great deals)** 
according to a predefined list. It compares the current market players with a list of chollos and suggests which players 
you should sign.

## Features
- **Fetch Market Players:** Retrieves the list of players currently available in the market.
- **Fetch Chollos:** Retrieves the list of great deals considered by www.analiticafantasy.com
- **Recommendation:** Just find matches in both lists to return the best deals in MD Fantasy.

## Required software
- Python (developed with v.3.8.10)
- Git
- Google Chrome

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/quimnaba/mister-md-scrapper.git
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate (Linux)
    venv/bin/activate (Windows)
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```bash
    ./run.sh
    ```

2. **Output:**
   - If there are no chollos in the market: "No chollos in the market. Save the money for tomorrow!"
   - If chollos are found, the script will suggest the players to sign.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any bug fixes or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Next steps
- Run concurrently the 2 drivers (threads)
- Put more metrics to consider
