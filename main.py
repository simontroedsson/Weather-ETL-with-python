import os
from excel_functions.excel import send_data_to_excel, print_forecast_from_excel
from API_files.openweathermap import get_latest_forecast_OWM
from API_files.SMHI import get_latest_forecast_SMHI


if __name__ == "__main__":
    while True:
        print("1. Hämta senaste data")
        print("2. Skriv ut prognos")
        print("9. Avsluta")
        menu_choice = input(">> ")

        if menu_choice == "1":
            os.system("cls")
            print("--------Hämta Prognos------")
            print("1. SMHI")
            print("2. OpenWeatherMap")
            print("3. SMHI och OpenWeatherMap")
            provider_choice = input()
            if provider_choice == "1":
                weather_data = get_latest_forecast_SMHI()
                send_data_to_excel(weather_data)
            elif provider_choice == "2":
                weather_data = get_latest_forecast_OWM()
                send_data_to_excel(weather_data)
            elif provider_choice == "3":
                weather_data_SMHI = get_latest_forecast_SMHI()
                weather_data_OWM = get_latest_forecast_OWM()
                send_data_to_excel(weather_data_SMHI)
                send_data_to_excel(weather_data_OWM)
            else:
                print("felaktig input")

        elif menu_choice == "2":
            os.system("cls")
            print("-----Skriv ut prognos-----")
            print("1. SMHI")
            print("2. OWM")
            provider_choice = input()
            if provider_choice == "1":
                print_forecast_from_excel("SMHI")
            elif provider_choice == "2":
                print_forecast_from_excel("openweathermap")

        elif menu_choice == "9":
            break

        else:
            print("felaktig input")
