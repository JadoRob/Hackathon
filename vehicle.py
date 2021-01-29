class Vehicle:
    # Constructor of the class, creates the object with the attributes (optional)
    def __init__(self, id=None, make=None, model=None, year=None, color=None, price=None):
        # if attributes are provided, stores the values to the object
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    #setters and getters, allows the object to set attribute values, and return values
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def setYear(self, year):
        self.year = year

    def getYear(self):
        return self.year

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPrice(self, price):
        self.price = price
    
    def getPrice(self):
        return self.price

