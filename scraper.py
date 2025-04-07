import requests
from bs4 import BeautifulSoup

def scrape_player_stats(player_name, opponent):
    """
    Example: Scrape batting averages from ESPN Cricinfo.
    Replace with actual logic later.
    """
    url = f"https://www.espncricinfo.com/player/{player_name.replace(' ', '-')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return {"player": player_name, "points": 70}  # Dummy data for now

# Test
if __name__ == "__main__":
    print(scrape_player_stats("Virat Kohli", "MI"))
