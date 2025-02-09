# Using mocking (patch) in unit testing


import requests


def len_joke():
    joke = get_joke()
    print("The joke from get_joke() is : ", joke)
    return len(joke)


def get_joke():
    
    print("We're inside the get_joke() function")
    print("Type of 'requests.exceptions.Timeout' : ", type(requests.exceptions.Timeout))

    url = "http://api.icndb.com/jokes/random"

    try:
        response = requests.get(url, timeout=30)

    except requests.exceptions.Timeout:
        return "No jokes"

    except requests.exceptions.ConnectionError:
        pass

    else:
        if response.status_code == 200:
            joke = response.json()["value"]["joke"]
        else:
            joke = "No jokes"


    return joke


if __name__ == "__main__":
    print(get_joke())