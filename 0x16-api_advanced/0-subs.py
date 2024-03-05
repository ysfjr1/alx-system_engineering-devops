import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

# Testing the function
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    print(number_of_subscribers(subreddit))
