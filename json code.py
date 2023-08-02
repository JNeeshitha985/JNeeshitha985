import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_BASE_URL)
    return response.json()


def get_weather_by_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None


def get_wind_speed_by_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None


def get_pressure_by_date(data, date):
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None


def main():
    data = get_weather_data()
    while True:
        print("Choose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input()

        if option == '1':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_weather_by_date(data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data found for the specified date.")
        elif option == '2':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data found for the specified date.")
        elif option == '3':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data found for the specified date.")
        elif option == '0':
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()


