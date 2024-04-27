from abc import ABC, abstractmethod
import requests


# This is a (useless) class:
# A class is like a blueprint for objects

class AClass:
    pass


print(f'This is a (useless) class: {AClass=}')

# An instance is just an object made from the blueprint of a class

# This is an instance:

a = AClass()

print(f'This is an instance: {a=}')


# This is a class with something more useful:

class XY:
    def __init__(self,
                 x,
                 y):
        self.x = x
        self.y = y

    # Look up __str__ for more info
    def __str__(self):
        return f'({self.x},{self.y})'

    # Look up __repr__ for more info
    def __repr__(self):
        return f'XY(x={self.x}, y={self.y})'

    def __add__(self, other):
        return XY(x=self.x + other.x,
                  y=self.y + other.y)

    def __sub__(self, other):
        return XY(x=self.x - other.x,
                  y=self.y - other.y)


xy1 = XY(y=3, x=10)
xy2 = XY(x=-1, y=2)


print(f'This is an instance of a more useful class {xy1=}\n'
      f'{xy2.x=}\n'
      f'{xy2.y=}\n'
      f'{xy1=}\n'
      f'{xy2=}\n'
      f'{(xy1 + xy2)=}\n'
      f'{(xy1 - xy2)=}')

print(f'{str(xy1)=}. {repr(xy1)=}')


# This is a class with something even more useful:

class XYZ:
    def __init__(self,
                 x,
                 y,
                 z):
        self.x = x
        self.y = y
        self.z = z

    # Look up __str__ for more info
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    # Look up __repr__ for more info
    def __repr__(self):
        return f'XYZ(x={self.x}, y={self.y}, z={self.z})'

    def __add__(self, other):
        return XYZ(x=self.x + other.x,
                   y=self.y + other.y,
                   z=self.z + other.z)

    def __sub__(self, other):
        return XYZ(x=self.x - other.x,
                   y=self.y - other.y,
                   z=self.z - other.z)

    def get_colour_in_xyz(self):
        # This method doesn't belong here. It will raise an exception for XYZ
        return self.colour


xyz1 = XYZ(y=3, x=10, z=0)
xyz2 = XYZ(x=-1, y=2, z=5)

print(f'This is an instance of a even more useful class {xyz1=}\n'
      f'{xyz2.x=}\n'
      f'{xyz2.y=}\n'
      f'{xyz2.z=}\n'
      f'{xyz1=}\n'
      f'{xyz2=}\n'
      f'{(xyz1 + xyz2)=}\n'
      f'{(xyz1 - xyz2)=}')

try:
   assert xyz1.get_colour_in_xyz() is not None
   raise AssertionError('get_colour was meant to work!')
except AttributeError:
    ...  # ... is an empty statement, which is useful for blocks that do nothing
    print('Cool! We wanted that exception on get_colour')


# A class inheriting from another class...

class ColourfulXYZ(XYZ):
    def __init__(self,
                 x,
                 y,
                 z,
                 colour):
        super().__init__(x, y, z)  # Call super class to initialise x and y
        self.colour = colour

    def __repr__(self):
        return f'ColourfulXYZ(x={self.x}, y={self.y}, z={self.z}, colour="{self.colour}")'

    # For our example, we can't add colours together, but we can add teh x,y,z
    # parts together, so we just get XYZ to do that for us


    def get_colour_in_colourful_xyz(self):
        # This method does belong here in ColourfulXYZ
        return self.colour


cxyz1 = ColourfulXYZ(y=3, x=10, z=0, colour='red')
cxyz2 = ColourfulXYZ(x=-1, y=2, z=5, colour='green')

cxyz1 + cxyz2  # Put a breakpoint here to step into XYZ.__add__

print(f'This is an instance of a class with inheritance\n'
      f'{cxyz1=}\n'
      f'{cxyz2 = }\n'
      f'{cxyz2.x = }\n'
      f'{cxyz2.y = }\n'
      f'{(cxyz1 + cxyz2) = }')

assert cxyz1.get_colour_in_xyz() is not None
assert cxyz1.get_colour_in_colourful_xyz() is not None


# Abstract todo_classes are blueprints with something missing
# that needs to be defined by another class called a
# concrete class. You can put stuff that's common in the
# abstract class and just put unique stuff in the concrete
# class.
#
# You can mark abstract classed as ABC.
# You can mark the missing stuff as @abstractmethod
#
# This is an abstract class for searching:

class BaseSearch(ABC):
    @abstractmethod
    def _make_search_query_url(self,
                               query):
        pass

    def query(self,
              query):
        url = self._make_search_query_url(query)
        r = requests.get(url=url)
        return r.content


# If you try to make something from an abstract class,
# it'll raise an exception:

try:
    BaseSearch().query('Sky Glass')
except TypeError as te:
    print(f'Handling: {te}')


# Here's an example of a concrete class. It's based on
# the abstract class, and just defines something real to
# to take the place of the abstract bit:

class DuckDuckGo(BaseSearch):
    def _make_search_query_url(self,
                               query):
        return f'https://duckduckgo.com/?q={query}'


# We can make an instance of this and us it

search = DuckDuckGo()

result = search.query("Sky Glass")
print(f'bytes={len(result)}. {result[:100]}')


# We can make another concrete class that does
# something slightly different.

class Google(BaseSearch):
    def _make_search_query_url(self,
                               query):
        return f'https://google.co.uk/?q={query}'


search = Google()
result = search.query("Sky Glass")
print(f'bytes={len(result)}. {result[:100]}')
