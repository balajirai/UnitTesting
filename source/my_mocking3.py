# Using mocking (patch) in unit testing


import requests


def len_joke():
    joke = get_joke()
    return len(joke)


def get_joke():
    

    url = "http://api.icndb.com/jokes/random"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return "No jokes"

    except requests.exceptions.ConnectionError:
        pass

    except requests.exceptions.HTTPError:
        return "HTTPError was raised"

    else:
        if response.status_code == 200:
            joke = response.json()["value"]["joke"]
        else:
            joke = "No jokes"


    return joke


if __name__ == "__main__":
    print(get_joke())