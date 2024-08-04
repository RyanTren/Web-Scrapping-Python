import requests
from bs4 import BeautifulSoup
import json

def fetch_page(url):
    """Fetch the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_general_data(soup):
    """Parse general data from the soup object."""
    data = {}
    for element in soup.find_all():
        class_name = " ".join(element.get('class', []))
        if class_name not in data:
            data[class_name] = []
        text_content = element.get_text(strip=True)
        if text_content:
            data[class_name].append(text_content)
    return data

def scrape_website(url):
    """Scrape data from the given URL."""
    page_content = fetch_page(url)
    if not page_content:
        return None
    
    soup = BeautifulSoup(page_content, 'html.parser')
    data = parse_general_data(soup)
    
    return {
        'url': url,
        'data': data
    }

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    data = scrape_website(url)
    if data:
        print(f"Scraped data from {data['url']}:")
        for class_name, contents in data['data'].items():
            print(f"Class: {class_name}")
            for content in contents:
                print(f"Content: {content}")

        # Save data to a JSON file
        json_filename = 'scraped_data.json'
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Data has been saved to {json_filename}")
