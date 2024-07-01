import requests
import json

def scrape_app_store(app_id, store):
    try:
        if store.lower() == 'apple':
            # Construct API request URL for Apple App Store (iTunes)
            url = f'https://itunes.apple.com/lookup?id={app_id}'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                if data['resultCount'] > 0:
                    app_info = data['results'][0]  # Assuming first result is the app you want
                    
                    # Example: Extracting app name and rating
                    app_name = app_info['trackName']
                    app_rating = app_info.get('averageUserRating', 'N/A')
                    
                    # Print or save the data as needed
                    print(f'App Name: {app_name}')
                    print(f'Rating: {app_rating}')
                    
                    # Optionally, save to JSON file
                    with open('app_data.json', 'w') as json_file:
                        json.dump(app_info, json_file, indent=4)
                        
                    print('Data saved successfully.')
                else:
                    print('No results found for the app ID.')
            else:
                print(f'Failed to fetch data from Apple App Store. Status code: {response.status_code}')
        
        elif store.lower() == 'google':
            # Construct API request URL for Google Play Store
            # Example: Google Play Store API request logic goes here
            print('Google Play Store scraping logic to be implemented.')
            # Replace with actual Google Play Store API scraping logic
            
        else:
            print('Invalid store choice. Please choose either "apple" or "google".')
    
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Prompt the user for an App ID and store choice
app_id = input('Enter the App ID of the app to scrape: ')
store_choice = input('Choose the store to scrape ("apple" for Apple App Store, "google" for Google Play Store): ')

# Call the function to start scraping
scrape_app_store(app_id, store_choice)
