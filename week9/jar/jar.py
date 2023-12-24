class Jar:
    # Constructor
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # String method for object
    def __str__(self):
        return "🍪"*self.size

    # Adding cookies to jar
    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError("More than capacity")
        self.size += n

    # taking cookies out of jar
    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError
        self.size -= n

    # getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # setter for capacity
    @capacity.setter
    def capacity(self, capacity=12):
        if capacity < 0:
            raise ValueError("Cookies not available")
        self._capacity = capacity

    # getter for cookies
    @property
    def size(self):
        return self._size

    # setter for cookies
    @size.setter
    def size(self, n=0):
        self._size = n

def main():
    # instantiating Jar object with 10 capacity
    cookie = Jar(10)

    # adding 5 cookies
    cookie.deposit(5)
    print("Cookies in Jar:", cookie)

    # taking out 2 cookies
    cookie.withdraw(2)
    print("Cookies in Jar:", cookie)

    # calling getters
    print("Jar capacity:", cookie.capacity)
    print("Number of cookies:", cookie.size)

    # making an error
    #cookie.deposit(10)

if __name__ == "__main__":
    main()
