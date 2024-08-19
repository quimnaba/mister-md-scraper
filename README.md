# MD Fantasy Football Chollo Finder

This Python script helps you to identify players available in the market who are considered "chollos" **(great deals)** 
according to a predefined list. It compares the current market players with a list of chollos and **suggests which players 
you should sign**.

The goal of this project is to prevent the user from spending much time on searching through barely known football players to
set the perfect bid on them, and also to reaffirm the user's criteria when it wants to set the bid.

Good to know: If you have multiple accounts, the script will run in the last account you had open. You can change the account before
running the script, or in the browser when it opens automatically in the screen.

## Features
- **Fetch Market Players:** Retrieves the list of players currently available in the market.
- **Fetch Chollos:** Retrieves the list of great deals considered by **www.analiticafantasy.com**
- **Shows Recommendations:** It finds matches in both lists to return the **best deals in MD Fantasy**.

## Required software
- Python (developed with v.3.8.10)
- Git
- Google Chrome

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/quimnaba/mister-md-scrapper.git
    ```
    Or just download the files in a folder.
## Usage
0. Insert your **MD Fantasy credentials** in PrivateData.py, like:
```
user_email="xxxxxxxx@gmail.com"
pwd = "xxxxxxxxx"
```

1. **Run the script:**
- In Linux:
    ```bash
    ./run.sh
    ```
- In Windows:
    Open run.bat

2. **Output:**
   - If there are no chollos in the market: "No chollos in the market. Save the money for tomorrow!"
   - If chollos are found, the script will suggest the players to sign.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any bug fixes or improvements.

## Next steps
- Run concurrently the 2 drivers (threads)
- Put more metrics to consider
- Add error handling
- Add headless mode
- Clean Code
