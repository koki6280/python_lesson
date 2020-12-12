class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

del person

print('##########################')
class Person(object):
    def __init__(self, age=1):
        self.age = age


class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')
    pass

class TeslaCar(Car):
    def __init__(self,
                 model='Model S',
                 enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('######################')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('######################')

tesla_car = TeslaCar('Model S')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()






