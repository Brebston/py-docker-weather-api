from dotenv import load_dotenv
import requests
import os


load_dotenv()
API_KEY=os.getenv("API_KEY")


def get_weather() -> None:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"
    response = requests.get(url)
    data = response.json()
    location = data.get("location", {})
    city = location.get("name")
    country = location.get("country")
    localtime = location.get("localtime")
    weather = data.get("current", {})
    temperature = weather.get("temp_c")
    weather = data.get("current", {}).get("condition").get("text")
    print(f"{city}/{country} {localtime} Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
