import requests
from bs4 import BeautifulSoup

# Function to extract movie titles from the search results page
def extract_movie_titles(search_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send GET request to the search page
    response = requests.get(search_url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section with search-page-results type="movie"
    section = soup.find("search-page-result", {"type": "movie"})

    if section:
        # Find the <ul> inside the section
        ul = section.find("ul")
        
        if ul:
            # Find all <search-page-media-row> elements inside the <ul>
            media_rows = ul.find_all("search-page-media-row")
            
            # Extract titles from <a> with data-qa="info-name" inside each media row
            movie_titles = []
            for media_row in media_rows:
                a_tag = media_row.find("a", {"data-qa": "info-name"})
                if a_tag:
                    movie_titles.append(a_tag.text.strip())
            
            return movie_titles
        else:
            return "No <ul> element found inside the section."
    else:
        return "Section with search-page-results not found."

# Example search URL (replace with your desired URL)
input = "life of pie"
input = input.replace(" ", "%20")
# print(input)
search_url = "https://www.rottentomatoes.com/search?search=" + input

# Extract movie titles
movie_titles = extract_movie_titles(search_url)

# Print movie titles
if isinstance(movie_titles, list):
    for idx, title in enumerate(movie_titles):
        print(f"Movie {idx + 1}: {title}")
else:
    print(movie_titles)
