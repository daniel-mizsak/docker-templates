import requests

if __name__ == "__main__":
    website = input("Website to check availability: ")
    website_available = False

    print(f"Checking {website}")
    try:
        r = requests.get(f"https://www.{website}")
        if r.status_code == 200:
            website_available = True
    except requests.exceptions.ConnectionError:
        pass

    if website_available:
        print("The website is up and running!")
    else:
        print("The website is currently not available.")
