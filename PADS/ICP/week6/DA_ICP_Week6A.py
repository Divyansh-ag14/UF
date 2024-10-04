class Temp:
    def __init__(self):
        self.__celsius = 0
        self.__fahrenheit = 32

    def get_fahrenheit(self):
        return self.__fahrenheit

    def get_celsius(self):
        return self.__celsius

    def set_fahrenheit(self, fahrenheit):
        self.__fahrenheit = fahrenheit
        self.__celsius = (fahrenheit - 32) * 5 / 9

    def set_celsius(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = (celsius * 9 / 5) + 32

def main():
  f = [0, 40, 80, 120, 160, 200]
  for i in f:
    temp = Temp()
    temp.set_fahrenheit(i)
    print(f"{i} Fahrenheit equals {temp.get_celsius():.1f} Celsius")

  c = [0, 20, 40, 60, 80]
  for i in c:
    temp = Temp()
    temp.set_celsius(i)
    print(f"{i} Celsius equals {temp.get_fahrenheit():.1f} Fahrenheit")


if __name__ == "__main__":
    main()
    