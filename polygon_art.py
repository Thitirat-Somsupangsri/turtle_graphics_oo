import turtle
import random

reduction_ratio = 0.618
art = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))


class Ran_num:
    def __init__(self):
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)


class Polygon:
    def __init__(self, side_num: int = 0):
        self.side_num = side_num
        random_properties = Ran_num()
        self._size = random_properties.size
        self.orientation = random_properties.orientation
        self.location = random_properties.location
        self.color = random_properties.color
        self.border_size = random_properties.border_size
        if self.side_num == 0:
            self.side_num = random.randint(3, 5)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val: int):
        self._size = val

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.side_num):
            turtle.forward(self.size)
            turtle.left(360 / self.side_num)
        turtle.penup()


class Polygon_3_size:
    def __init__(self, side_num: int = 0):
        self.side_num = side_num
        random_properties = Ran_num()
        self._size = random_properties.size
        self.orientation = random_properties.orientation
        self.location = random_properties.location
        self.color = random_properties.color
        self.border_size = random_properties.border_size
        if self.side_num == 0:
            self.side_num = random.randint(3, 5)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val: float):
        self._size = val

    def draw(self, size: float, location: list):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.side_num):
            turtle.forward(size)
            turtle.left(360 / self.side_num)
        turtle.penup()

    def draw_three_sizes(self):
        self.draw(self.size, self.location)

        mid_size = self.size * reduction_ratio
        mid_location = [self.location[0] + (self.size - mid_size) / 2,
                        self.location[1] + (self.size - mid_size) / 2]
        self.draw(mid_size, mid_location)

        small_size = mid_size * reduction_ratio
        small_location = [mid_location[0] + (mid_size - small_size) / 2,
                          mid_location[1] + (mid_size - small_size) / 2]
        self.draw(small_size, small_location)


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
for _ in range(30):
    if art == 1:
        shape = Polygon(3)
        shape.draw()
    elif art == 2:
        shape = Polygon(4)
        shape.draw()
    elif art == 3:
        shape = Polygon(5)
        shape.draw()
    elif art == 4:
        shape = Polygon()
        shape.draw()
    elif art == 5:
        shape = Polygon_3_size(3)
        shape.draw_three_sizes()
    elif art == 6:
        shape = Polygon_3_size(4)
        shape.draw_three_sizes()
    elif art == 7:
        shape = Polygon_3_size(5)
        shape.draw_three_sizes()
    elif art == 8:
        shape = Polygon_3_size()
        shape.draw_three_sizes()
    elif art == 9:
        x = random.randint(1,2)
        if x == 1:
            shape = Polygon_3_size()
            shape.draw_three_sizes()
        if x == 2:
            shape = Polygon()
            shape.draw()

turtle.update()
turtle.done()
