from canvas import Canvas
import constants

drawing = None


def parseinput(drawing, source):
    if not source:
        raise Exception(constants.NO_INPUT_PROVIDED_EXCEPTION)
    elif source[0] == "C":
        drawing = Canvas(int(source[1]), int(source[2]))
        drawing.printcanvas()
    elif source[0] == "Q":
        return drawing, False
    elif drawing is None:
        raise Exception(constants.NO_CANVAS_EXCEPTION)
    elif source[0] == "L":
        drawing.drawline(int(source[1]), int(
            source[2]), int(source[3]), int(source[4]))
        drawing.printcanvas()
    elif source[0] == "R":
        drawing.drawrectangle(
            int(source[1]), int(source[2]), int(source[3]), int(source[4])
        )
        drawing.printcanvas()
    elif source[0] == "B":
        drawing.fillcolor(int(source[1]), int(source[2]), source[3])
        drawing.printcanvas()
    else:
        raise Exception(constants.INVALID_INPUT_EXCEPTION)
    return drawing, True


if __name__ == "__main__":
    while True:
        source = input("enter command: ").split()
        drawing, flag = parseinput(drawing, source)
        if not flag:
            break
