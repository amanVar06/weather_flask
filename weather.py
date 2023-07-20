from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="New Delhi"):
    # request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")&units=metric"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("API_KEY"),
        "units": "metric"
    }
    response = requests.get(url, params=params)
    return response.json()


if __name__ == "__main__":
    print("\n********** Get Current Weather Conditions **********\n")

    city = input("\nWhich city do you want the weather for? ")

    # check for empty strings or string with only spaces
    # strip() removes all spaces from the beginning and end of a string
    if not bool(city.strip()):
        city = "New Delhi"

    weather_data = get_current_weather(city)

    print(f"\nCurrent weather in {city}: \n")
    pprint(weather_data)

    print("\n********** Finished **********\n")
    get_current_weather()
