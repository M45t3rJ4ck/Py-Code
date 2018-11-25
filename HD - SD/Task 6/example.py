# =====================================
# Part 1 - a trivial example of a class
# =====================================
class SimpleCow(object):
    '''
    A triple-quote string is called a docstring and is used to store information
    about the class, function, or file/module in which it is contained.
    It is stored in the 'special variable' __doc__ and may be viewed
    in any of the following ways.

    >>> help(Cow)
    >>> print Cow.__doc__
    >>> cow = Cow()
    >>> help(cow)
    >>> print cow.__doc__

    Documenting the code you write is of fundamental importance.
    Docstrings allow you to somewhat automate the process; there are tools
    like Sphinx and Doxygen that generate documentation from docstrings.
    IDEs like Eclipse can also display them as part of their autocompletion.
    '''

    def __init__(self, color):
        '''
        This is the constructor for the class SimpleCow.
        A constructor creates a new instance of a class (see the introductory reading).

        To instantiate a class with the constructor, you simply call the class name like a function:
        >>> blue_cow = SimpleCow('blue')
        '''
        self.color = color

    _noise = 'moo!'

    def make_noise(self):
        '''
        Method that prints the cow's noise to standard output...

        A method is simply a function attached to an object (see reading).
        In Python, methods and properties are accessed with the dot operator:
        >>> blue_cow.make_noise()
        '''
        print(self._noise)

    def set_color(self, new_color):
        '''
        Paints the cow a different color
        This method is meant to be an example of the way that methods can modify an object's state.

        Get/set methods for object properties are a common sight in object-oriented code,
        but in Python they are not really necessary because Python lacks something called privacy.
        The first expression below is generally considered to be more 'Pythonic' (i.e. idiomatic) than the second:
        >>> blue_cow.color = 'red'
        >>> blue_cow.set_color('red')
        '''
        self.color = new_color

    def get_color(self):
        '''
        Method that returns the cow's color
        '''
        return self.color

    def __cmp__(self, other):
        '''
        The comparison special method.  Returns True if the two cows are the same
        color, and false if they are not.
        This strange-looking method is one of the so-called 'special methods'
        that are part of the Python language.
        Some of the special methods, like __del__(),
        have very specific functions.
        Others, like __cmp__, provide the functionality for 'operators'
        like ==, +, -, *, >, etc.  __cmp__ corresponds to the equality comparison
        operator ==.

        In other words, the following expressions are equivalent:
        >>> blue_cow == red_cow
        >>> blue_cow.__cmp__(red_cow)

        And so are these:
        >>> 'a'.__add__('b')
        >>> 'a' + 'b'

        Implementing these methods for custom classes is called 'operator overloading.'
        An exhaustive if somewhat outdated list of these special methods and their purposes
        may be found at http://docs.python.org/release/2.5.2/ref/specialnames.html

        In practice, it is often better to avoid operator overloading, as it can lead
        to reduced code clarity and strange bugs if errors are not handled correctly.
        '''
        if self.color == other.color:
            return True
        else:
            return False

    def __str__(self):
        '''
        This special method is called by Python when you use the 'print' command
        on an object.
        >>> print blue_cow
        'blue moo'
        >>> print blue_cow.__str__()
        'blue moo'
        '''
        return self.color + ' ' + self._noise

blue_cow = SimpleCow('blue')
red_cow = SimpleCow('red')

blue_cow.make_noise()
red_cow.make_noise()

print(red_cow == blue_cow)

blue_cow.set_color('red')
print(red_cow == blue_cow)


#==============================
# Part 2 - Inheritance
#==============================
class Animal(object):
    '''
    Animal class docstring
    '''
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def make_noise(self):
        pass

class Cow(Animal):
    '''
    An example of inheritance (see reading).
    This class inherits its constructor and the get_color method from Animal,
    and every instance of Cow is also an instance of Animal.
    '''
    _noise = 'moo'

    def make_noise(self):
        '''
        An example of a method that is defined by the base class and overwritten by the derived class
        '''
        print(self._noise)

    def sleep(self):
        '''
        An example of a method that is defined for the derived class but not the base class
        '''
        print('zzz')


pink_cow = Cow('pink')
print(pink_cow.get_color())
pink_cow.make_noise()
pink_cow.sleep()

assert isinstance(pink_cow, Cow) #True
assert isinstance(pink_cow, Animal) #True, all cows are animals
assert isinstance(pink_cow, SimpleCow) #False
pink_animal = Animal(pink_cow) #You can cast base classes to derived classes and vice versa
assert isinstance(pink_animal, Animal) #True
assert isinstance(pink_animal, Cow) #False - not all animals are cows
