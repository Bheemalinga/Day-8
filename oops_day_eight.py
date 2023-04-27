"""
class Book:
    numberOfPages = 145
    author = "Sudhanshu"
    scope = "To be sold in India"

    # Constructor

    def __init__(self, zone, dob):
        self.zone = zone
        self.dob = dob
    def __del__(self):
        print("Destructor is called")

# Creating a book object
my_book = Book("Mystry","25-10-1998")

#print(my_book.zone)
#print(my_book.dob)

"""



















#                  Inheritance

"""

class parent1:
    def getname():
        return "parent1"
    
class parent2:
    def getname():
        return "parent2"

class parent3:
    def getname():
        return "parent3"

class child(parent1, parent2, parent3):
    def __init__(self):
        self.getallparent()
    def getallparent(self):
        print(parent1.getname())
        print(parent2.getname())
        print(parent3.getname())
        print("Trying to get all parents of this class")

my_child = child()
parent_list=[]
#print(my_child.getname())
for base in child.__bases__:
    print(base.__name__)


    """



#     Polymorphism in Python

def addnumbers(a, b):
    print(a+b)

def addnumbers(a,b,c=2):
    print(a+b+c)

addnumbers(10,20)