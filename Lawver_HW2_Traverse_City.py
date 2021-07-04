class Point(object):
    def __init__(self, x_coordinate = 0, y_coordinate=0):
        self.x = x_coordinate
        self.y = y_coordinate

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y) 

    def __eq__(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False

    def __str__(self):
        return f'x:{self.x} y:{self.y}'

class Directions():
    N = Point(0,1)
    S = Point(0,-1)
    W = Point(-1,0)
    E = Point(1,0)

    @classmethod
    def translate_from_symbol_to_direction(cls, direction_symbol:str):
        if direction_symbol == "N":
            return cls.N
        elif direction_symbol == "S":
            return cls.S
        elif direction_symbol == "W":
            return cls.W
        elif direction_symbol == "E":
            return cls.E
        else:
            raise Exception("Invalid direction.")


def are_we_there_yet(directions:list or tuple, starting_point=Point(0,0)):
    original_point = starting_point

    if len(directions) != 10:
        return False
    if isinstance(directions,(list,tuple)):
        if isinstance(directions,(list)):
            # @1 translate all the directions into the Points
            for index,d in enumerate(directions):
                directions[index] = Directions.translate_from_symbol_to_direction(d)
            # @2 move using all directions
            for point in directions:
                starting_point = starting_point + point
            # @3 Check if you are back at the same spot
            if starting_point == original_point:
                return True
            return False
        if isinstance(directions,(tuple)):
            directions = [d for d in directions]
            # @1 translate all the directions into the Points
            for index,d in enumerate(directions):
                directions[index] = Directions.translate_from_symbol_to_direction(d)
            # @2 move using all directions
            for point in directions:
                starting_point = starting_point + point
            # @3 Check if you are back at the same spot
            if starting_point == original_point:
                return True
            return False
    else:
        raise Exception("Please provide correct arguments.")


