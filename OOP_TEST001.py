"""_
In Python's Object-Oriented Programming (OOP), 
there are three primary types of methods within a class: 
instance methods, 
class methods, and static methods. 

Each type serves a distinct purpose and interacts with the class 
and its instances in different ways.

1. Instance Methods:
Definition: 
These are the most common type of methods. 
They operate on a specific instance of a class.

Access: 
They have access to the instance's attributes and other instance methods 
through the self parameter, which refers to the instance itself.

Usage: 
Used when the method's logic depends on the state of a particular object.

"""

class MyClass:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value
    
"""
2. Class Methods:
Definition:
These methods operate on the class itself, rather than a specific instance. 
They are defined using the @classmethod decorator.

Access:
They receive the class as the first argument, conventionally named cls, 
allowing them to access and modify class-level attributes 
or create new instances of the class (e.g., factory methods).

Usage:
Used for operations that involve class-level data 
or when creating alternative constructors._
            
"""
    
        
class MyClass2:
        count = 0

        @classmethod
        def increment_count(cls):
            cls.count += 1

"""
3. Static Methods:

Definition:
These are utility methods that belong to the class's namespace 
but do not operate on a specific instance or the class itself. They are defined using the @staticmethod decorator.

Access:
They do not receive self or cls as implicit arguments. 
They behave like regular functions 
but are logically grouped within the class.

Usage:
Used for functions that have a logical connection to the class 
but do not require access to instance or class-specific data.
            """


class MyClass3:
        @staticmethod
        def calculate_sum(a, b):
            return a + b
m1 = MyClass(10)
m2= MyClass2()
m3 = MyClass3()
print(m3.calculate_sum(5, 7))
m2.increment_count()
m2.increment_count()
m2.increment_count()
print(m2.count)

m2.increment_count()

print(MyClass2.count)  # Output: 1
print(MyClass2.increment_count())  # Output: None

print(m1.get_value())  # Output: 10

