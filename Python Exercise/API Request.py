import requests
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:     
        data = response.json()
      
        for post in data[:5]:
            print("Title:", post['title'])
            print("Body:", post['body'])
            print()
    else:
        print("Failed to fetch data.")
fetch_data()
