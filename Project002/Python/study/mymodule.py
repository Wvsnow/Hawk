#! "E:\\Application\\_SourceCodes\\Python3p4p1\\mymodule.py"
# Filename: mymodule.py

import os

version = '0.1'
################################# ################################# ################################# 
################################# function defination
################################# ################################# #################################
def add(a,b):
    return a+b
def reduce(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def sayhi():
    print('Hi, this is mymodule speaking.') 
def dump(value):
    print()
    print(type(value), value)
    print(value, "=>", dir(value))
def getmembers(klass, members=None):
    # get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members
def load(file):
    if isinstance(file, type("")) and os.path.exists(file):
        file = open(file, "rb")
    else:
        file = open('PythonApplication1.py', "rb")
    return file.read()
def dumpCallable(function):
    if callable(function):
        print(function, "is callable")
    else:
        print(function, "is *not* callable")
################################# ################################# ################################# 
################################# class defination
################################# ################################# #################################
class Person:
    '''Represents a person.'''
    population = 0
    def __init__(self, nameStr):
        '''Initializes the person's data.'''
        self.name = nameStr
        print('(Initializing %s)' % self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1
    def __del__(self):
        '''I am out from here.'''
        print('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print('My name is %s, and I am the last one.' % (self.name))
        else:
            print('There are still %d people left.' % Person.population)
    def sayHi(self):
        print('Hello, the first class occurs!')
    def showInfo(self):
        print("My name is %s, and I'm a class" % (self.name))
    def tell(self):
        print("My name is %s, and I'm a Person" % (self.name))
class Teacher(Person):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        Person.__init__(self, name)
        self.age = age
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)
    def __del__(self):
        '''I am out from here.'''
        Person.__del__(self)
    def tell(self):
        Person.tell(self)
        print('Salary: "%d"' % self.salary)
# End of mymodule.py
