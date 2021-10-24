# create a function that calculates the slope of a line that consists
# of two points

def slope(x1, y1, x2, y2):
    return float((y2 - y1)/(x2 - x1))



def y_intercept(x1, y1, x2, y2):
    y_intercept = (y2) - (slope(x1, y1, x2, y2)*x2)
    return "equation of the line is: y = {}x + {}".format(slope(x1, y1, x2, y2), y_intercept)

print(y_intercept(1,1,3,2))