from weather_info import get_weather, get_5_day_forecast, save_favourite_city, remove_favourite_city, get_favourite_cities_weather, get_weather_alerts

print("Current Weather for Kanpur:")
print(get_weather("Kanpur", "metric"))

print("\nCurrent Weather for Mumbai:")
print(get_weather("Shimla", "imperial"))

print("\n5-Day Forecast for Mumbai:")
print(get_5_day_forecast("Mumbai", "metric"))

print("\nAdding Mumbai to favourites:")
print(save_favourite_city("Jaipur"))

print("\nWeather for favourite cities:")
print(get_favourite_cities_weather("metric"))

print("\nRemoving Mumbai from favourites:")
print(remove_favourite_city("Mumbai"))
