# Problem Set: https://cs50.harvard.edu/python/2022/psets/8/jar/
""" 
Implement a cookie jar in which to store cookies
Class function, jar
__ini__ cookie jar with capacity 
IF capacity is negative int, then should instead raise a value error
__str__ returns a str with n cookies in a jar
n is a program input

deposit function to add n cookies to a jar, raise a ValueError 

withdraw function to remove cookies from the jar, and
IF there aren't cookies left in a jar, raise ValueError

 """
class Jar:
    def __init__(self, capacity = 12):
        """ if capacity < 0:
            raise ValueError("Wrong Capacity Size") """
        self._capacity = capacity 
        self._size = 0

    def __str__(self) -> str:
        cookie = "🍪" * self.size
        return f"{cookie}"

    def deposit(self, n) -> int:
        if n > self.capacity:
            raise ValueError("Over Capacity")
        if self.size + n > self.capacity:
            raise ValueError("The Jar is Full.")
        else:
            self.size += n
        # self._size = size
    
    def withdraw(self, n) -> int:
        if n > self.size:
            raise ValueError("Not Enough Cookies!!!")
        else:
            self.size -= n

    # getter
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Wrong capacity Size")
        self._capacity = capacity

    # getter
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("The Jar is empty...")
        elif size > self._capacity:
            raise ValueError("Over Capacity")
        self._size = size



