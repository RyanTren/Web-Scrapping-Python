import os
import requests
from bs4 import BeautifulSoup
import json

def scrape_app_store(app_url):
    try:
        # Fetch webpage content
        response = requests.get(app_url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # Extracting app information
            app_name = soup.find('h1', class_='product-header__title').text.strip()
            developer = soup.find('a', class_='link').text.strip()
            ratings = soup.find('div', class_='we-customer-ratings__averages').text.strip()
            description = soup.find('div', class_='section__description').text.strip()

            # Extracting customer reviews and ratings
            reviews = []
            review_blocks = soup.find_all('div', class_='we-customer-review')
            for block in review_blocks:
                rating = block.find('figure', class_='we-star-rating').get('aria-label').strip()
                review_text = block.find('blockquote', class_='we-customer-review__body').text.strip()
                reviews.append({
                    'Rating': rating,
                    'Review': review_text
                })

            # Create a dictionary to store all extracted data
            app_data = {
                'App Name': app_name,
                'Developer': developer,
                'Ratings': ratings,
                'Description': description,
                'Reviews': reviews
            }

            # Specify the directory path for saving the JSON file
            directory = 'info'
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Save data to a JSON file inside the 'info' folder
            file_path = os.path.join(directory, 'app_data.json')
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file, ensure_ascii=False, indent=4)

            print(f'Data saved successfully to {file_path}.')

        else:
            print(f'Failed to fetch webpage. Status code: {response.status_code}')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Example usage
if __name__ == '__main__':
    print("Ryan's Web Scrapper V1.0\n")
    app_url = input('Enter the link to the app store page: ')
    
    scrape_app_store(app_url)
