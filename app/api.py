import requests

def get_weather(city="Hamburg"):
    url = f"https://wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    data = response.json()
    
    current = data["current_condition"][0]
    
    weather_data = {
        "temperature": current["temp_C"],
        "weather": current["weatherDesc"][0]["value"]
    }
    
    return weather_data


if __name__ == "__main__":
    print(get_weather())