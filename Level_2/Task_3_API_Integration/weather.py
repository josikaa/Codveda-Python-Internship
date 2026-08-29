import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "country": location.get("country", "")
    }


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def main():
    print("===== Weather Information App =====")

    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    try:
        location = get_coordinates(city)

        if location is None:
            print("City not found.")
            return

        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        current = weather["current"]

        print("\n===== Current Weather =====")
        print(f"Location: {location['name']}, {location['country']}")
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Humidity: {current['relative_humidity_2m']} %")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")

    except requests.exceptions.RequestException:
        print("Error: Unable to connect to the weather service.")

    except (KeyError, TypeError):
        print("Error: Unexpected response from the API.")


if __name__ == "__main__":
    main()