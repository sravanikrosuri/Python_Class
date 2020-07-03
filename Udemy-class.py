### Python Udemy class
#birth_year = input('what year were you born?')

#age = 2020 - int(birth_year)

#print(f'your age is : {age}')

### Exercise: Password

#username = input('What is your username?')
#password = input('What is your password?')

#password_len = len(password)
#hidden_password = '*' * password_len

#print(f' {username}, your password {hidden_password} is {password_len} letters long')

### List methods

#basket =[1,2,3,4,5]

# adding
  #basket.append(100)
  #new_list = basket
#print(basket)
#print(new_list)
## inserting anywhere in the list
  #basket.insert(4,300) 
# inserted at the index of 4 with 100
## extending the items
   #new_list = basket.extend([10, 101])

## removing
# pop removes at the end of the list
   #basket.pop() 
# removes item at the index 0 which is  1
   #basket.pop(0) 
# remove we give value to be removed whereas for pop we give index
   #basket.remove(4)

#bas = ['a','b','c','d','e']
#print('d' in bas)

#print('i' in 'hi my name is Sravi')
## counts how many times this value occurence in the list
#print(bas.count('d'))

## for loops
## counts each item in the zero to mastery

#for item in 'zero to mastery':
#       print(item)

## for loop using lists
#for item in [1,2,3,4]:
#      print(item)

## for loop using tuple
#for item in (1,2,3,4):
#       print(item)

## set
#for item in {3,4,5,6}:
#       print(item)
#       print(item)
#       print(item)
#print('hi')

## nested for loops
#for item in (1,2,3,4,5):
#   for x in ['a','b','c']:
#      print(item, x)



## let's try an dictionary for looping
#user = {
#   'name': 'Sravi',
#   'age': 5006,
#   'can_swim': False
#}
## this will give both key and value as a tuple in the output
#for item in user.items():
#   print(item)

## this will give only values in the dictionary
#for item in user.values():
#   print(item)

## for keys
#for item in user.keys():
#       print(item)

## what to print separately name and values 
## instead of key and value we can use k, v
#for key, value in user.items():
#   print(key, value)

## 
#for item in range(50):
#       print(item)


## exercise
#counter = 0
#for item in [1,2,3,4,5,6,7,8,9,10]:
#   counter = counter + item
   #print(counter)
#print(counter)
## *****************************************************************
## enumerate gives idex for each letter in the output
#for i, char in enumerate('sravi'):
#       print(i, char)

## exercise get index of number 50 is 
#for i, char in enumerate(list(range(100))):
#       print(i, char)
#       if char == 50:
#              print(f'index of 50 is: {i}')


#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

## if we don't want new line each time then use end ='' in the print 
## statement
for image in picture:
  for pixel in image:
    if (pixel== 1):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')

## Exercise check duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm','n','n']

duplicates = []
for items in some_list:
   if some_list.count(items) > 1:
      if items not in duplicates:
          duplicates.append(items)
print(duplicates)

## Return
def sum(num1, num2):
       print(num1 + num2)
sum(4,5)

def sum(num1, num2):
       return num1 + num2
print(sum(9,10))

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def checkDriverAge():
  age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
	  print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
	  print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(92)

### Object Oriented Prgramming

class PlayerCharacter:
       def __init__(self, name, age):
            self.name = name ## attributes
            self.age = age

       def run(self):
            print('run')
            return 'done'

player1 = PlayerCharacter('Sravi', 30)
player2 = PlayerCharacter('Sai', 33)

print(player1.name, player1.age, player1.run())
print(player2.name, player2.age, player2.run())

## adding if statement for the age 
class PlayerCharacter:
      membership = True
      def __init__(self, name, age):
            if (PlayerCharacter.membership):
                  self.name = name ## attributes
                  self.age = age
      
      def shout(self):
            print(f'my name is {self.name}')
            print(f'age {self.age}')

player1 = PlayerCharacter('Sravi', 30)
player2 = PlayerCharacter('Sai', 33)

print(player1.shout())
print(player2.shout())

## There is a mistake we are going to understand how to fix mistakes 
## in the next class
#class PlayerCharacter:
      #class object attribute
 #     membership = True
  #    def __init__(self, name = 'anonymous', age =0):
   #          if (age > 18):
    #                self.name = name # attribute
    #                self.age = age
      
     # def shout(self):
     #        print(f'my name is {self.name}')

#player1 = PlayerCharacter('Tom', 10)

#print(player1.shout())

###  Exercise

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Kitty', 1)
cat2 = Cat('Donny', 2)
cat3 = Cat('rorry', 1)

    
# 2 Create a function that finds the oldest cat
def OldCat(*args):
  return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest #cat age by using the function in #2
print(f'the oldest cat is {OldCat(cat1.age, cat2.age, cat3.age)} years old')

### Encapsulation

class PlayerCharacter:
      def __init__(self, name, score):
            self.name = name
            self.score = score

      def run(self):
             print('In temple run.')
      
      def speak(self):
             print(f'my name is {self.name}, and my score is {self.score}.')

player1 = PlayerCharacter('Sravi', 150)
player1.speak()
player1.run()

## Abstraction
## definition: hiding of information or abstraction away information and giving acess 
## only what is necessary.
print(len((1,2,3,1))) # we don't want to know how len function is implemented 
## learning implementation is not always apprropriate for coding. 
## we don't need to know how iphone camera is capturing the pictures.

## 

class PlayerCharacter:
      def __init__(self, name, age):
             self.name = name
             self.age = age

      def run(self):
             print('run')

      def speak(self):
             print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Sravi', 120)
player1.name = '!!!'
player1.speak = 'Boooooo'
print(player1.speak)

## Public and private variables
## Private: self._name, _ means private. No private variables in python.
## _ means you shouldn't be modified.
## __init Dunder method it is built into python. Don't modified or overwrite this.

## *************** Inheritance **********************

## Inheritance: Allows new object to take on the properties of existing objects.
## so we can inherit properties.

#class User:
#   def sign_in(self):
## if we don't have variables or attributes to assign to user in that 
## case we wouldn't need __init__()
#          print('logged in')
## let's create a bunch of classes (users)
## Users:
       ## wizard, 
       ## Archers
       ## orgers
#class Wizard(User):
#       def __init__(self, name, power):
#              self.name = name
#              self.power = power

#       def attack(self):
#              print(f'attacking with power of {self.power}')

#class Archer(User):
#       def __init__(self, name, num_arrows):
#              self.name = name
#              self.num_arrows = num_arrows
      
#       def attack(self):
#              print(f'attacking with arrows: arrows left {self.num_arrow}')

#wizard1 = Wizard('Merlin', 50)
#print(isinstance(wizard1, User)) ## output is true because wizard1 inherits methods from 
## user class and wizard classes. 

## instantiate a class
#archer1 = Archer('Robin', 100)
#wizard1.attack()
#archer1.attack()
#print(wizard1.sign_in())

### ********************* Polymorphism ********************
## definition: refers to the way in which object classes can share the same
## method name but those method names can act differently based on what their Actions call.


#class User:
#   def sign_in(self):
## if we don't have variables or attributes to assign to user in that 
## case we wouldn't need __init__()
#          print('logged in')
## let's create a bunch of classes (users)
## Users:
       ## wizard, 
       ## Archers
       ## orgers
#class Wizard(User):
#       def __init__(self, name, power):
#              self.name = name
#              self.power = power

#       def attack(self):
#              print(f'attacking with power of {self.power}')

#class Archer(User):
#       def __init__(self, name, num_arrows):
#              self.name = name
#              self.num_arrows = num_arrows
      
#       def attack(self):
#              print(f'attacking with arrows: arrows left {self.num_arrow}')

#wizard1 = Wizard('Merlin', 50)
#archer1 = Archer('robin', 30)

#for char in [wizard1, archer1]:
#       char.attack()

### ************* Exercise ************************
#class Pets():
#    animals = []
#    def __init__(self, animals):
#        self.animals = animals

#    def walk(self):
#        for animal in self.animals:
#            print(animal.walk())

#class Cat():
#    is_lazy = True

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def walk(self):
#        return f'{self.name} is just walking around'

#class Simon(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#class Sally(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#1 Add nother Cat
#class Suzy(Cat):
#    def sing(self, sounds):
#        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
#my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

#3 Instantiate the Pet class with all your cats
#my_pets = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance
#my_pets.walk()

### ********************** Super Class **************************

### copy polymorphism code and add super for the 

#class User:
#       def sign_in(self):
## if we don't have variables or attributes to assign to user in that 
## case we wouldn't need __init__()
#          print('logged in')
## let's create a bunch of classes (users)
## Users:
       ## wizard, 
       ## Archers
       ## orgers
#class Wizard(User):
#       def __init__(self, name, power, email):
#              super().__init__(email)
#              self.name = name
#              self.power = power

#       def attack(self):
#              print(f'attacking with power of {self.power}')

#class Archer(User):
#       def __init__(self, name, num_arrows):
#              self.name = name
#              self.num_arrows = num_arrows
      
#       def attack(self):
#              print(f'attacking with arrows: arrows left {self.num_arrow}')

### *********************** Object Introspection *******************
#wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
## for introspection  print(dir(wizard1))
#print(wizard1, email)

### ************************** Dunder methods ***********************
#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
#class Toy():
#  def __init__(self, color, age):
#    self.color = color
#    self.age = age
#    self.my_dict = {
#        'name':'Yoyo',
#        'has_pets': False,
#    }

#  def __str__(self):
#    return f"{self.color}"

# def __len__(self):
#    return 5

#  def __del__(self):
#    return "deleted"

#  def __call__(self):
#      return('yes??')

#  def __getitem__(self,i):
#      return self.my_dict[i]


#action_figure = Toy('red', 0)
#print(action_figure.__str__())
#print(str(action_figure))
#print(len(action_figure))
#print(action_figure())
#print(action_figure['name'])

#### ************** Exercise ************************

#class SuperList(list):
#      def __len__(self):
#    return 1000

#super_list1 = SuperList();

#print(len(super_list1))
#super_list1.append(5)
#print(super_list1[0])
#print(issubclass(list, object))

### ****************** Map functions ***********************
def multiply_by2(item):
       # in map functions we don't have to create an empty []
       return item*2

print(list(map(multiply_by2, [2,4,6])))

### *********** Filter function **********************
## check odd number
my_list= [1,2,3]

def only_odd(item):
       return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)

###***************** zip function **************************

my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list, your_list)))
print(my_list)

## ******************************************************
my_list = [1,2,3]
your_list = [10,20,30]
our_list = (22, 33, 55)

print(list(zip(my_list, your_list, our_list)))
print(my_list)


### ****************** reduce function *******************
## reduce doesn't come in the part of built in functions in python 
## therefore we need to use library

from functools import reduce

def accumulator(acc, item):
       print(acc, item)
       return acc + item


print(reduce(accumulator, my_list, 0))

### ****************** Exercise **************************

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def Capi(item):
  return item.capitalize()

print(list(map(Capi, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def Pass_Over50(item):
  return item > 50

print(list(filter(Pass_Over50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def Combine(num, item):
  return num + item

print(reduce(Combine, (my_numbers + scores)))

### ***************** Lambda Expressions **************************

my_list = [3,5,7,8]

print(list(map(lambda item: item*2, my_list)))

### ******************* Lambda expression exercise ******************
## Squaring the list
my_list = [5,4,3]

## instead of item we can give anything
print(list(map(lambda item : item**2, my_list )))

#List Sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
## run the sort function based on the second item in the each (), ()
a.sort(key = lambda x : x[1])
print(a)

## ************* List Comprehensions *********************
## instead of doing lengthy thing (the way below)
my_list = []
for char in 'hello':
       my_list.append(char)
print(my_list)

## easy way
mylist = [char for char in 'hello']
mylist2 = [ num for num in range(0,100)]
## all the numbers in the list to be multiplied by 2
mylist3 = [num*2 for num in range(0,100) ]
## keep only even numbers in the list, list contains power of the numbers in the items. 
mylist4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(mylist4)

## **************************************************
##*****************set comprehensions ******************************
mylist = { char for char in 'hello'}
print(mylist)

####******************* Dictionary Comprehensions Example ****************
simple_dict = {
       'sravi' : 2, 
       'Sai' : 3
}
my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)

## ***************** Using if statement *******************

simple_dict = {
       'sravi' : 2, 
       'Sai' : 3
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value %2 ==0}
print(my_dict)

#### **************** Another example **********************

my_dict = {num: num*2 for num in [1,2,3]}
print(my_dict)

### ********* Duplicates Exercise ********************
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

## convert the above code into easy way (applying comprehensions)*********
duplicates = list(set([x for x in some_list if some_list.count(x)>1]))

print(duplicates)

## ************* Decorators ******************************
## super charge our functions 

# high order function HOC a simple example
#def greet(func): # greet accepts another function, this is called Higher order function
#       func()

#def greet2():
#       def func():
#              return 5
#       return func

## ************ Own decorator *****************************
#def my_decorator(func):
#       def wrap_func():
#              print('**********')
#              func()
#              print('**********')
#       return wrap_func

#@my_decorator
#def hello():
#       print('hello')

#@my_decorator
#def bye():
#       print('See you later')
#hello()
#bye()

### ****************************************
## this is the decorator the first part of the code
#def my_decorator(func):
#       def wrap_func(*args, **kwargs):
#              print('**********')
#              func(*args, **kwargs)
#              print('**********')
#       return wrap_func

#@my_decorator
#def hello(greeting, emoji =':('):
#       print(greeting, emoji)

#hello('hiiii')

##*********** Pratical applications of Decorators ***********

## Decorator
#from time import time 

#def performance(func):
#       def wrapper(*args, **kwargs):
#              t1 = time() # Check what is the time now
#              result = func(*args, **kwargs)
#              t2 = time() # check the time
#              print(f'{t2 - t1} seconds')
#              return result
#       return wrapper

#@performance  # we building it python doesn't have this
#def long_time():
#       for i in range(100000000):
#              i * 5
#long_time()

###******************* Exercise *****************
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
#user1 = {
#    'name': 'Sorna',
#    'valid': True #changing this will either run or not run the message_friends function.
#}

#def authenticated(fn):
#  def wrapper(*args, **kwargs):
#    if args[0]['valid']:
#      return fn(*args, **kwargs)
#  return wrapper

#@authenticated
#def message_friends(user):
#    print('message has been sent')

#message_friends(user1)

### ***************** error handling *********************
#while True:
#       try: 
#              age = int(input('What is your age?'))
#              10/age
#       except ValueError:
#              print('Please enter a number')
#       except ZeroDivisionError:
#              print('please enter age higher than zero')
#       else:
#              print('Thank you')
#              break
#       finally: 
       ## finally says no matter what I want to print this 
       ## finally runs regardless even though there is a break statement in 
       ## the else step (it actually exists while loop but does the finally)
#              print('ok, i am finally done')

### ***************** example 2 Error Handling ****************

#def sum(num1, num2):
#       try:
#              return num1 + num2
#       except TypeError as err: 
       # we can also handle multiple exceptions (TypeError, ZeroDivisionError) as err:
       # by doing this way we will see this message in the output 
       # error description to the users.
#              print(f'Please enter numbers {err}')

#print(sum(1,2))

##****************** Error handling exercise ********************
#while True:
#       try: 
#              age = int(input('What is your age?'))
#              10/age
#       except ValueError:
#              print('Please enter a number')
#              continue
#       # continue will try again what is your age even we give a number. 
#       except ZeroDivisionError:
#              print('please enter age higher than zero')
#              break
#       else:
#              print('Thank you')
#              break
       ## we will break this but 2nd print in the finally statement won't 
       ## display in the output.
       ## but if we remove the break in this step we will get the both print 
       ## statements in the finally step. 
#       finally: 
#              print('ok, i am finally done')
#       print('Can you hear me?')

## ********************* Error Handling 3 ***************************

#while True:
#       try: 
#              age = int(input('What is your age?'))
#              10/age
#              #raise ValueError('hey cut it out')
       ## raise clause or except ValueError one is fine 
       ## we can also do this for Exception 
#       except ValueError:
#              print('Please enter a number')
#              continue
#       except ZeroDivisionError:
#              print('please enter age higher than zero')
#              break
#       else:
#              print('Thank you')
#              break 
#       finally: 
#              print('ok, i am finally done')
#       print('Can you hear me?')

## ********************* Generators **********************************

# list is an iterable
# generators are iterable but, not all iterables are generators.
# generators are subset of iterables.

## general way to create
#def generator_function(num):
#       for i in range(num):
#              yield i 
# instead of appending and return we are using yield.
# yield pauses the function and comes back to it when we tell to keep going
# instead of creating the list in the memory we just keep going on one by one (output)
# we only held one item in memory and we use it.
#for item in generator_function(1000):
#       print(item)

## ************* Yield examples ***************
#def gene_func(num):
 #      for i in range(num):
 #             yield i*2
# if we have yield keyword it will become generator. 
#g = gene_func(100)
#next(g)
#next(g)
#print(next(g))

##*************** Exercises *******************************


from time import time
#def performance(fn):
#    def wrapper(*args, **kawrgs):
#        t1 = time()
#        result = fn(*args, **kawrgs)
#        t2 = time()
#        print(f'took {t2-t1} s')
#        return result
#    return wrapper

#@performance
#def long_time():
#    print('1')
#    for i in range(100000):
#        i*5
#@performance
#def long_time2():
#    print('2')
#    for i in list(range(100000)):
#        i*5


#long_time()
#long_time2()

## ***************** Exercise Under the Hood of Generators *************
## Special for loop
def special_for(iterable):
       iterator = iter(iterable)
       while True:
              try: 
                     print(iterator)
                     print(next(iterator))
              except StopIteration:
                     break
special_for([1,2,3,4])

## ************* special range *********************
class MyGen():
       current = 0
       def __init__(self, first, last):
              self.first = first
              self.last = last

       def __iter__(self):
              return self
       
       def __next__(self):
              if MyGen.current < self.last:
                     num = MyGen.current
                     MyGen.current +=1
                     return num 
              raise StopIteration

gen = MyGen(0,100)
for i in gen:
       print(i)

### **************** Fibonacci Numbers (interview Question) **********************
## output: 0 1 1 2 3 5 8 13 21 34 55 89 144 
## here we can do it in two ways 1) list and 2) generators.
def fib(num):
       # num is the index number 
       a = 0
       b = 1
       for i in range(num):
              ## range we need num of times
              yield a 
              # give me what is a and pause the function
              temp = a ## temporary variable
              a = b 
              b = temp + b 
for x in fib(20):
       print(x)

## using List same example ***************
def fib2(num):
       # num is the index number 
       a = 0
       b = 1
       result = []
       for i in range(num):
              result.append(a) 
              temp = a 
              a = b 
              b = temp + b 
       return result 

print(fib2(10))

##*********** Modules in Python ***********************