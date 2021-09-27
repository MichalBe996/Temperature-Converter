

class TemperatureConverter():
    def __init__(self):
        while True:
            degrees = input("Enter degrees that you want to convert [Celcius degrees]: ")
            unit = input("Do you want to convert to Fahrenheit or Kelvin degrees? [F/K]")


            if unit == "F" or unit == "f":
                unit_fahr = int(degrees) * 9 / 5 + 32
                print("Your temperature in Celcius degrees is ", unit_fahr, "degrees Fahrenheit.")

            elif unit == "K" or unit == "k":
                unit_kel = int(degrees) + 273.15
                print("Your temperature in Celcius degrees is ", unit_kel, "degrees Kelvin.")

            elif unit != "F" or unit != "f" or unit != "K" or unit != "k":
                print("Something's wrong, please try again.")


TemperatureConverter()