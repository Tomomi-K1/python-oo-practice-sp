"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=0):
        """ make a new generator, starting at start"""
        self.start = self.next = start
        # you can set two variables at once. That's what's going on there. Well actually you can set more than two at a time. 
        # That syntax inside the __init__ method will actually define both self.next and self.start and set it to the value of start
        # you can do self.a = self.b = self.c ="hello" then you are setting both a and b and c as "hello"
        # this is called Chained assignment syntax

    def __repr__(self):
        "show representation"
        return f"<SerialGenerator start = {self.start} next ={self.next}"

    def generate(self):
        """ return next serial number """
        self.next += 1
        return self.next -1

    def reset(self):
        """ reset number to original start """
        self.next = self.start
