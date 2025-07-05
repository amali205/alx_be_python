class shape:
    def __init__(self):
        self
    def area(self):
        raise NotImplementedError
class Rectangle(shape):
    def __init__(self):
        super().__init__()
    def area(self): 
        raise NotImplementedError  
