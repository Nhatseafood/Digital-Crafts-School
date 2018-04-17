
#1 
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    def print_contact_info(self):
        print('email:' ,self.email, 'phone number:' ,self.phone)

    def greet(self, other_person):
        self.greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('sonny email: {} , sonny phone: {} '.format(self.email, self.phone))
    def add_friend(self,x):
        self.friends.append(x)
    def num_friend(self):
        print(len(self.friends))
    def print_greeting_count(self):
        print(self.greeting_count)

sonny = Person('sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)

jordan.greet(sonny)
sonny.print_contact_info()
sonny.add_friend(jordan)
sonny.num_friend()
sonny.print_greeting_count()

print(sonny.greeting_count)
#jordan.friends.append(sonny)
#sonny.friends.append(jordan)
#print(len(jordan.friends))

#print("My contact info is: {} and {} ".format(sonny.email, sonny.phone))
#print("My contact infor is: {} and {} ".format(jordan.email, jordan.phone))
# print('Contact info, Name {}, Email {},Phone {}'.format(sonny.name, sonny.email, sonny.phone))


# #2

# #1 
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friend = []
#         self.greeting_count = 0

    
       
 
#     def print_contact_info(self):
#         print('email:' ,self.email, 'phone number:' ,self.phone)
#     def add_friend(self, x):
#         self.friend.append(x)
#     def num_friend(self):
#         print(len(self.friend))


#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))
    
#     def greeting_count(self):
#         print(greet)
#         self.greeting_count += 1


# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.print_contact_info()
# sonny.num_friend()
# sonny.greeting_count


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(self.year, self.make, self.model)

# car = Vehicle('Nissan', 'leaf', '2015')
# car.print_info()


# #3
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friend = []
#         self.greeting_count = 0

#     def __str__(self):
#        return'Person: {} {} {}'.format(self.name, self.email, self.phone)

    
#     def print_contact_info(self):
#         print('email:' ,self.email, 'phone number:' ,self.phone)
#     def add_friend(self, x):
#         self.friend.append(x)
#     def num_friend(self):
#         print(len(self.friend))


#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))
    
#     def greeting_count(self):
#         print(greet)
#         self.greeting_count += 1


# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# sonny.print_contact_info()
# sonny.num_friend()
# sonny.greeting_count
# print(sonny)




# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print("{} {} {}".format(self.make, self.model, self.year))

# mynissancar = Vehicle('Nissan', 'Leaf', '2015')
# mynissancar.print_info()
