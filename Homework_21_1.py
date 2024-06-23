from colorama import Fore


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    new_color = None

    def __init__(self, owner: str, model: str, engine_power=300, color='blue'):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return Fore.BLUE + 'Модель: {}'.format(self.__model)

    def get_horsepower(self):
        return 'Мощность двигателя: {}'.format(self.__engine_power)

    def get_color(self):
        return Fore.BLUE + 'Цвет: {}'.format(Fore.BLUE + self.__color)

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(Fore.BLUE + 'Владелец: {}'.format(self.owner))

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = Fore.GREEN + new_color
        else:
            print(Fore.RED + 'Нельзя сменить цвет на {}'.format(self.new_color))


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle_1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle_1.print_info()

vehicle_1.set_color('Pink')
vehicle_1.set_color('BLACK')
vehicle_1.owner = Fore.GREEN + 'Vasyok'

vehicle_1.print_info()
