import constants


class Canvas:
    canvas = None

    def __init__(self, width, height):
        self.canvas = [[" " for i in range(width)] for j in range(height)]

    def printcanvas(self):
        # Printing the upper boundary
        for i in range(len(self.canvas[0]) + 2):
            print("-", end="")
        print()

        # Printing every row of our canvas
        for i in range(len(self.canvas)):
            print("|", end="")  # Left Boundary
            for j in range(len(self.canvas[0])):
                print(self.canvas[i][j], end="")
            print("|")  # Right Boundary

        # Printing the Lower Boundary
        for i in range(len(self.canvas[0]) + 2):
            print("-", end="")
        print()

    def fillcolor(self, x, y, c):
        self.__checkoutofbound(x, y)

        if(len(c) != 1):
            raise Exception(constants.COLOR_LENGTH_EXCEPTION)

        current = self.canvas[y - 1][x - 1]
        self.__floodfill(y - 1, x - 1, current, c)

    def drawline(self, x1, y1, x2, y2):
        self.__checkoutofbound(x1, y1)
        self.__checkoutofbound(x2, y2)

        if (x1 != x2) and (y1 != y2):
            raise Exception(constants.NON_LINEAR_LINE_EXCEPTION)

        x1, y1, x2, y2 = self.__sortpoints(x1, y1, x2, y2)
        # Drawing Vertical Line
        if (x1 == x2):
            for i in range(y1 - 1, y2):
                self.canvas[i][x1 - 1] = "x"

        # Drawing Horizontal Line
        if(y1 == y2):
            for j in range(x1 - 1, x2):
                self.canvas[y1 - 1][j] = "x"

    def drawrectangle(self, x1, y1, x2, y2):
        self.__checkoutofbound(x1, y1)
        self.__checkoutofbound(x2, y2)

        self.drawline(x1, y1, x2, y1)
        self.drawline(x1, y1, x1, y2)
        self.drawline(x2, y1, x2, y2)
        self.drawline(x1, y2, x2, y2)

    # Private Methods / Helper Functions
    def __floodfill(self, i, j, pastcolor, newcolor):
        # Checking out of Bounds
        if (i < 0 or i >= len(self.canvas)) or (j < 0 or j >= len(self.canvas[0])) or pastcolor == newcolor:
            return

        if(self.canvas[i][j] == pastcolor):
            self.canvas[i][j] = newcolor
            self.__floodfill(i + 1, j, pastcolor, newcolor)
            self.__floodfill(i, j + 1, pastcolor, newcolor)
            self.__floodfill(i - 1, j, pastcolor, newcolor)
            self.__floodfill(i, j - 1, pastcolor, newcolor)

    def __sortpoints(self, x1, y1, x2, y2):
        if(x2 < x1):
            x2, x1 = x1, x2
            y2, y1 = y1, y2

        if(y2 < y1):
            x2, x1 = x1, x2
            y2, y1 = y1, y2

        return x1, y1, x2, y2

    def __checkoutofbound(self, x, y):
        if (y <= 0 or y > len(self.canvas)) or (x <= 0 or x > len(self.canvas[0])):
            raise Exception(constants.OUT_OF_BOUNDS_EXCEPTION)
