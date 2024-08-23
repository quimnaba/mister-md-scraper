# MD Fantasy Football Chollo Finder - La Liga

This Python script is designed to help you quickly identify "chollos" (bargains) in the Mister Fantasy Football market, 
specifically for the Spanish first division, **La Liga**, in the **Mister Fantasy MD** application (BeManager).

The application compares the players currently available on the market with a predefined list of chollos, and the script **suggests which players 
you should sign**.

The purpose of this project is to save users time by streamlining the process of finding valuable yet lesser-known football players. 
It also serves to **validate the user's bidding criteria**, ensuring you make informed decisions when placing bids.

**Important**: If you have multiple accounts, the script will run in the last account you had open. You can either switch accounts before
running the script, or change accounts in the browser when it opens automatically.

## Features
- **Market Player Retrieval:** Automatically fetches the list of players currently available on the market.
- **Chollo detection:** Retrieves and compares players against the list of chollos provided **www.analiticafantasy.com**
- **Personalized Recommendations:** Identifies and suggests the best deals available on MD Fantasy.

## Required software
- Google Chrome

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/quimnaba/mister-md-scraper.git
    ```
    Or just download the files in a folder.
## Usage
0. Open PrivateData.json and insert your **MD Fantasy credentials**:
```json
"user_email": "your_email@example.com"
"pwd": "your_password"

```
Never post or push this file on internet.

1. **Run the script:**
- On Linux:
    ```bash
    ./run.sh
    ```
- On Windows:
    Double click 'run.bat'.

2. **View Console Output:**
   - No Chollos found: 
        - Message: "No chollos in the market. Save the money for tomorrow!"
   - Chollos found:
        - The script will suggest players you should consider signing.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any bug fixes or improvements.

## Future enhancements
- Incorporate additional metrics for better player evaluation
- Add headless mode for chrome drivers
