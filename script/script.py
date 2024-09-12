import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from datetime import datetime, timezone


def fetch_weather_data(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={1606488670}&end={1606747870}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


# Save data to a JSON file
def save_data_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Visualize o3 levels
def visualize_o3_data(data):
    timestamps = [datetime.fromtimestamp(item['dt'], timezone.utc) for item in data['list']]
    o3_levels = [item['components']['o3'] for item in data['list']]
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, o3_levels, marker='o', color='black', linestyle='-', linewidth=1, markersize=2)
    plt.title('Ozone (O3) Levels Over Time')
    plt.xlabel('Time')
    plt.ylabel('O3 Levels')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    
    # Lviv
    lat = 49.8397
    lon = 24.0297
    
    data = fetch_weather_data(lat, lon, api_key)
    
    if data:
        file_name = "script/data.json"
        save_data_to_file(data, file_name)
        visualize_o3_data(data)


if __name__ == "__main__":
    main()
