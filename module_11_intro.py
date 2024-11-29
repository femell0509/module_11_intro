import sys
from pprint import pprint
import inspect

class Car:

    def __init__(self, model, collor, max_speed, max_power):
        self.model = model
        self.collor = collor
        self.max_speed = max_speed
        self.max_power = max_power
        self.all_collor = ['white', 'blue', 'red', 'black', 'pink', 'purple', 'yellow']

    def average_speed(self, distance, time_travel):
        return distance/time_travel

    def change_collor(self, new_collor):
        if new_collor in self.all_collor:
            self.collor = new_collor
            print(f'Цвет изменен на: {self.collor}')
        else:print('Этого цвета нет в каталоге')

my_volvo = Car('V40', 'white', 240, 180)

my_volvo.change_collor('qwerty')

my_volvo.change_collor('red')
print(my_volvo.average_speed(450, 6.5))

def introspection_info(obj):
    dict_obj ={}
    dict_obj.update({'type': type(obj), 'attributes': vars(obj),
                     'methods': dir(obj), 'OS': sys.platform,
                     'size_of_bytes': sys.getsizeof(obj)})
    try:
        dict_obj.update({'name': obj.__name__})
    except:pass
    return dict_obj

pprint(introspection_info(my_volvo))
pprint(introspection_info(Car))
