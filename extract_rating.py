import requests
from bs4 import BeautifulSoup

# Function to extract movie ratings for both audience and critics
def extract_ratings(movie_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send GET request to the movie page
    response = requests.get(movie_url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize a dictionary to store ratings
    ratings = {}

    # Find the <rt-button> with slot="audienceScore"
    audience_button = soup.find("rt-button", {"slot": "audienceScore"})
    if audience_button:
        # Find the <rt-text> element inside the <rt-button> for audience score
        audience_text = audience_button.find("rt-text")
        if audience_text:
            ratings["Audience Rating"] = audience_text.text.strip()
        else:
            ratings["Audience Rating"] = "Audience rating not found!"
    else:
        ratings["Audience Rating"] = "Audience button not found!"

    # Find the <rt-button> with slot="criticsScore"
    critics_button = soup.find("rt-button", {"slot": "criticsScore"})
    if critics_button:
        # Find the <rt-text> element inside the <rt-button> for critics score
        critics_text = critics_button.find("rt-text")
        if critics_text:
            ratings["Critics Rating"] = critics_text.text.strip()
        else:
            ratings["Critics Rating"] = "Critics rating not found!"
    else:
        ratings["Critics Rating"] = "Critics button not found!"

    return ratings

# Example movie URL (replace with your desired movie URL)
movie_url = "https://www.rottentomatoes.com/m/avengers_endgame"

ratings = extract_ratings(movie_url)
print(ratings)
