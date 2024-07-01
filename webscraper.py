import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    # Fetch the webpage
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        # Example: Scraping app names and ratings
        app_data = []
        
        # Replace with actual HTML structure and tags to find app names and ratings
        app_name_tags = soup.find_all('h2', class_='app-name')
        app_rating_tags = soup.find_all('div', class_='app-rating')
        
        for name_tag, rating_tag in zip(app_name_tags, app_rating_tags):
            app_name = name_tag.text.strip()
            app_rating = rating_tag.text.strip()
            app_data.append({
                'App Name': app_name,
                'Rating': app_rating
            })
        
        # Store data in JSON
        json_filename = 'mental_health_apps.json'
        with open(json_filename, 'w') as jsonfile:
            json.dump(app_data, jsonfile, indent=4)
        
        print(f'Data scraped and saved successfully to {json_filename}')
    else:
        print('Failed to retrieve the webpage')

# Prompt the user for a website URL
url = input('Enter the URL of the website to scrape: ')

# Call the function to start scraping
scrape_website(url)
