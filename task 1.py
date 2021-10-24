class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return(self.x)

    def get_y(self):
        return(self.y)

    def get(self):
        return self.x, self.y

    def set_x(self):
        x_new = float(input('New x is '))
        self.x = x_new

    def set_y(self):
        y_new = float(input('New y is '))
        self.y = y_new

    def set(self):
        x_new = float(input('New x is '))
        self.x = x_new
        y_new = float(input('New y is '))
        self.y = y_new
