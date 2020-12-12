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

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

     def drive(self):
        print('ok')

baby = Baby()
#baby.drive()
adult = Adult()
#adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()



class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self,
                 model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

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

tesla_car = TeslaCar('Model S')
tesla_car.__enable_auto_run = 'XXXXXXXXXX'
print(tesla_car.__enable_auto_run)




