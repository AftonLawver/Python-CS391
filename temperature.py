# Lead Programmer: Afton Lawver
'''
This program creates temperature objects, which can then be 
converted to celcius or fahrenheit. 
'''
class Temperature():

    def __init__(self, temp:int):
        self.temp = temp

    def convert_fahrenheit(self):
        temperature = ((self.temp - 32)*5)/9
        formatted_temperature = "{:.1f}".format(temperature)
        return "{}°F is {}°C".format(self.temp,formatted_temperature)

    def convert_celcius(self):
        temperature = (((self.temp)*9)/5)+32
        formatted_temperature = "{:.1f}".format(temperature)
        return "{}°C is {}°F".format(self.temp,formatted_temperature)

a = Temperature(98)
print(a.convert_fahrenheit())

x = Temperature(4)
print(x.convert_celcius())
