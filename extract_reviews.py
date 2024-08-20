import requests
from bs4 import BeautifulSoup

# Function to extract top reviews (isTopReview = true)
def extract_top_reviews(movie_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send GET request to the movie page
    response = requests.get(movie_url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section with aria-labelledby="critics-reviews-label"
    section = soup.find("section", {"aria-labelledby": "critics-reviews-label"})
    
    if section:
        # Find all review cards with istopreview="true"
        top_reviews = section.find_all("review-card-critic", {"istopreview": "true"})

        # print(top_reviews)
        
        extracted_reviews = []
        for review in top_reviews:
            # Extract review details (critic name, publication, review text, etc.)
            critic_name = review.find("rt-link", {"slot": "displayName"}).text.strip() if review.find("rt-link", {"slot": "displayName"}) else "N/A"
            publication_name = review.find("rt-link", {"slot": "publicationName"}).text.strip() if review.find("rt-link", {"slot": "publicationName"}) else "N/A"
            review_text = review.find("rt-text", {"slot": "content"}).text.strip() if review.find("rt-text", {"slot": "content"}) else "N/A"
            review_date = review.find("rt-text", {"slot": "createDate"}).text.strip() if review.find("rt-text", {"slot": "createDate"}) else "N/A"
            score = review.find("rt-text", {"slot": "originalScore"}).text.strip() if review.find("rt-text", {"slot": "originalScore"}) else "N/A"

            # Store extracted review details in a dictionary
            extracted_reviews.append({
                "Critic Name": critic_name,
                "Publication": publication_name,
                "Review": review_text,
                "Date": review_date,
                "Score": score if score != "" else "No score provided"
            })

        return extracted_reviews
    else:
        return "Section with critics reviews not found."

# Example movie URL (replace with your desired movie URL)
movie_url = "https://www.rottentomatoes.com/m/marvels_the_avengers"

# Extract top reviews
top_reviews = extract_top_reviews(movie_url)

# Print top reviews
for idx, review in enumerate(top_reviews):
    print(f"Review {idx + 1}:")
    for key, value in review.items():
        print(f"{key}: {value}")
    print("\n" + "-"*50 + "\n")
