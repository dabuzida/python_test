class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def callName(self):
        print(f'hello my name is {self.name}')
    def callAge(self):
        print(f'hello my age is {self.age}')

p1 = Person('john', 36)

p1.callAge()
p1.age = 44
p1.callAge()
del p1.age
p1.callAge()
