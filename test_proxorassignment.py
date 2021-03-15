import unittest
import sys
import constants
from main import parseinput
from io import StringIO
from canvas import Canvas


class testCanvas(unittest.TestCase):

    def setUp(self):
        self.testcanvas = Canvas(2, 3)

    def test_printcanvas(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.testcanvas.printcanvas()
        sys.stdout = sys.__stdout__
        self.assertEqual("----\n|  |\n|  |\n|  |\n----\n",
                         capturedOutput.getvalue())

    def test_printcanvaswithvalue(self):
        self.testcanvas.canvas[0][0] = 'x'
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.testcanvas.printcanvas()
        sys.stdout = sys.__stdout__
        self.assertEqual("----\n|x |\n|  |\n|  |\n----\n",
                         capturedOutput.getvalue())

    def test_fillcolor(self):
        self.testcanvas.fillcolor(1, 1, 'x')
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', 'x'], ['x', 'x'], ['x', 'x']])

    def test_spreadfillcolor(self):
        self.testcanvas.canvas[0][0] = 'x'
        self.testcanvas.canvas[0][1] = 'x'
        self.testcanvas.fillcolor(1, 1, 'x')
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', 'x'], [' ', ' '], [' ', ' ']])

    def test_fillcolor_invalidpoints(self):
        with self.assertRaisesRegex(Exception, constants.OUT_OF_BOUNDS_EXCEPTION):
            self.testcanvas.fillcolor(10, 10, 'x')

    def test_fillcolor_invalidcolor(self):
        with self.assertRaisesRegex(Exception, constants.COLOR_LENGTH_EXCEPTION):
            self.testcanvas.fillcolor(1, 1, "xyz")

    def test_drawline_vertical(self):
        self.testcanvas.drawline(1, 1, 1, 2)
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', ' '], ['x', ' '], [' ', ' ']])

    def test_drawline_horizontal(self):
        self.testcanvas.drawline(1, 1, 2, 1)
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', 'x'], [' ', ' '], [' ', ' ']])

    def test_drawline_samecordinate(self):
        self.testcanvas.drawline(1, 1, 1, 1)
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', ' '], [' ', ' '], [' ', ' ']])

    def test_drawline_outofbound(self):
        with self.assertRaisesRegex(Exception, constants.OUT_OF_BOUNDS_EXCEPTION):
            self.testcanvas.drawline(1, 1, 10, 10)
        with self.assertRaisesRegex(Exception, constants.OUT_OF_BOUNDS_EXCEPTION):
            self.testcanvas.drawline(10, 10, 1, 1)

    def test_drawline_nonlinear(self):
        with self.assertRaisesRegex(Exception, constants.NON_LINEAR_LINE_EXCEPTION):
            self.testcanvas.drawline(1, 1, 2, 2)

    def test_drawrectangle(self):
        self.testcanvas.drawrectangle(1, 1, 2, 2)
        self.assertEqual(self.testcanvas.canvas, [
                         ['x', 'x'], ['x', 'x'], [' ', ' ']])

    def test_drawrectangle_outofbounds(self):
        self.testcanvas.drawrectangle(1, 1, 2, 2)
        with self.assertRaisesRegex(Exception, constants.OUT_OF_BOUNDS_EXCEPTION):
            self.testcanvas.drawrectangle(1, 1, 10, 10)
        with self.assertRaisesRegex(Exception, constants.OUT_OF_BOUNDS_EXCEPTION):
            self.testcanvas.drawrectangle(5, 5, 10, 10)

    def test_parseinput_quit(self):
        self.assertEqual(parseinput(self.testcanvas, ['Q']), (self.testcanvas, False))

    def test_parseinput_noinput(self):
        with self.assertRaisesRegex(Exception, constants.NO_INPUT_PROVIDED_EXCEPTION):
            parseinput(self.testcanvas, [])

    def test_parseinput_nocanvas(self):
        with self.assertRaisesRegex(Exception, constants.NO_CANVAS_EXCEPTION):
            parseinput(None, ['B', '1', '2', 'c'])

    def test_parseinput_invalidinput(self):
        with self.assertRaisesRegex(Exception, constants.INVALID_INPUT_EXCEPTION):
            parseinput(self.testcanvas, ['X', 'Y', 'Z'])


if __name__ == '__main__':
    unittest.main()
