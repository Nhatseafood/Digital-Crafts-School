'''
#1 
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def print_contact_info(self):
        print('email:' ,self.email, 'phone number:' ,self.phone)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
print('Contact info, Name {}, Email {},Phone {}'.format(sonny.name, sonny.email, sonny.phone))

'''

#2

#1 
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []
        self.greeting_count = 0
       
 
    def print_contact_info(self):
        print('email:' ,self.email, 'phone number:' ,self.phone)
    def add_friend(self, x):
        self.friend.append(x)
    def num_friend(self):
        print(len(self.friend))


    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    
    def greeting_count(self):
        print(greet)
        self.greeting_count += 1


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.print_contact_info()
sonny.num_friend()
sonny.greeting_count


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle('Nissan', 'leaf', '2015')
car.print_info()

