import requests

def get_fact(choice):
    categories = {
        1: ("Random", "https://uselessfacts.jsph.pl/random.json?language=en"),
        2: ("Technology", "https://uselessfacts.jsph.pl/category/Technology.json?language=en"),
        3: ("History", "https://uselessfacts.jsph.pl/category/History.json?language=en"),
        4: ("Science", "https://uselessfacts.jsph.pl/category/Science.json?language=en")
    }
    
    category_name, url = categories.get(choice, (None, None))
    
    if url:
        response = requests.get(url)
        print(f"Fetching {category_name} fact... Status: {response.status_code}")
        
        if response.status_code == 200:
            fact_data = response.json()
            print(f"Did you know? {fact_data['text']}")
        else:
            print(f"Failed to fetch {category_name.lower()} fact")
    else:
        print("Invalid choice!")
while True:
    user_input = input("Press 1 for a random fact, 2 for a technology fact, 3 for a history fact, 4 for a science fact, or type 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    get_fact(int(user_input))