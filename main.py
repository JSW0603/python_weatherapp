# import modules
import requests
import time
import tkinter as tk

# make function to get a weather info
def getinfo(window):
    place = searchfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid=5ab0115c0bf902343532eaa7ab70d409"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 3600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 3600))

    info = condition + "\n" + str(temp) + "ºC" + "\n"
    info_detail = "Max Temp: " + str(max_temp) + "ºC" + "\n" + "Min Temp: " + str(min_temp) + "ºC" + "\n" + "Pressure: " + str(pressure) + "\n" \
                  + "Humidity: " + str(humidity) + "\n" + "Wind: " + str(wind) + "km/hr" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label_1.config(text=info)
    label_2.config(text=info_detail)

# configure the app design
window = tk.Tk()
window.geometry("800x650")
window.title("What is the weather")

t_1 = ("Times", "36", "bold")
t_2 = ("Times", "16", "bold")

searchfield = tk.Entry(window, font=t_2)
searchfield.pack(pady=35)
searchfield.focus()
searchfield.bind("<Return>", getinfo)

label_1 = tk.Label(window, font=t_1)
label_1.pack()
label_2 = tk.Label(window, font=t_2)
label_2.pack()

window.mainloop()