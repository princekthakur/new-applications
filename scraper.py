import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_player_stats(player_name, opponent, venue):
    # Example: Scrape from ESPNcricinfo
    url = f"https://stats.espncricinfo.com/ci/engine/player/{player_id}.html?class=3;template=results;type=batting"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from tables
    tables = soup.find_all('table')
    df = pd.read_html(str(tables[0]))[0]  # Assuming first table has batting stats
    
    # Filter by opponent & venue (pseudo-code)
    df_filtered = df[(df['Opposition'] == opponent) & (df['Ground'] == venue)]
    return df_filtered

# Example usage
# df_kohli = scrape_player_stats("Virat Kohli", "vs Australia", "Wankhede")
