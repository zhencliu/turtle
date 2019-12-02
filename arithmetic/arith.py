import os
import sys
import time
import turtle

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isdir(os.path.join(basedir, 'utils')):
    sys.path.append(basedir)


from utils import config
import expression


class Arith(object):

    ARITH_PATH = os.path.join(basedir, "arithmetic")
    IMAGE_PATH = os.path.join(ARITH_PATH, "images")
    EXPR = {
        'hooray': os.path.join(IMAGE_PATH, 'hooray.gif'),
        'trying': os.path.join(IMAGE_PATH, 'trying.gif'),
        '0': os.path.join(IMAGE_PATH, '0.gif'),
        '1': os.path.join(IMAGE_PATH, '1.gif'),
        '2': os.path.join(IMAGE_PATH, '2.gif'),
        '3': os.path.join(IMAGE_PATH, '3.gif'),
        '4': os.path.join(IMAGE_PATH, '4.gif'),
        '5': os.path.join(IMAGE_PATH, '5.gif'),
        '6': os.path.join(IMAGE_PATH, '6.gif'),
        '7': os.path.join(IMAGE_PATH, '7.gif'),
        '8': os.path.join(IMAGE_PATH, '8.gif'),
        '9': os.path.join(IMAGE_PATH, '9.gif'),
        '+': os.path.join(IMAGE_PATH, 'add.gif'),
        '-': os.path.join(IMAGE_PATH, 'minus.gif'),
        '?': os.path.join(IMAGE_PATH, 'q.gif'),
        '=': os.path.join(IMAGE_PATH, 'e.gif')
    }

    def __init__(self):
        self.conf = config.Config(os.path.join(Arith.ARITH_PATH, "conf.ini"))

        control = self.conf.setting('control')
        self.speed = int(control.get('speed', 10))
        self.diffx = int(control.get('diffx', 80))
        self.diffy = int(control.get('diffy', 10))
        self.beginx = int(control.get('beginx', -300))
        self.beginy = int(control.get('beginy', 300))

        arith = self.conf.setting('arithmetic')
        self.expr_obj = expression.Expression(int(arith['min']),
                                              int(arith['max']),
                                              arith['operators'])
        screen = self.conf.setting('screen')
        self.screen = turtle.Screen()
        self.screen.setup(int(screen['width']), int(screen['height']))
        self.screen.title(screen['title'])
        self.screen.bgcolor(screen['bg_color'])
        self.images = {}
        self.expr_images = []
        self.result = ''
        self.records = {'hooray': 0, 'trying': 0}

    def _number_0(self):
        self.result = '%s0' % self.result

    def _number_1(self):
        self.result = '%s1' % self.result

    def _number_2(self):
        self.result = '%s2' % self.result

    def _number_3(self):
        self.result = '%s3' % self.result

    def _number_4(self):
        self.result = '%s4' % self.result

    def _number_5(self):
        self.result = '%s5' % self.result

    def _number_6(self):
        self.result = '%s6' % self.result

    def _number_7(self):
        self.result = '%s7' % self.result

    def _number_8(self):
        self.result = '%s8' % self.result

    def _number_9(self):
        self.result = '%s9' % self.result

    def _space(self):
        try:
            result = int(self.result)
        except Exception:
            result = -1

        image = 'hooray'
        if self.expr_obj.result != result:
            image = 'trying'

        self.records[image] += 1
        print(image, self.records[image])
        self.images[image].setpos(0, 0)
        self.images[image].showturtle()
        time.sleep(2)
        self.images[image].hideturtle()

        self.result = ''
        self._clear()
        self._gen_expr_objs()

    def _register_images(self):
        for item in Arith.EXPR:
            self.screen.register_shape(Arith.EXPR[item])
            self.images[item] = turtle.Turtle(Arith.EXPR[item], visible=False)
            self.images[item].speed(self.speed)
            self.images[item].penup()
            self.images[item].setpos(self.beginx, self.beginy)

    def _gen_expr_objs(self):
        # Create a new expression
        self.expr_obj.gen_expr()
        images = []
        for image in self.expr_obj.expr:
            images.append(image)
            obj = self.images[image] if image not in images else self.images[image].clone()
            obj.setpos(self.beginx, self.beginy)
            self.expr_images.append(obj)

    def _register_events(self):
        # register number key event
        self.screen.onkey(self._number_0, '0')
        self.screen.onkey(self._number_1, '1')
        self.screen.onkey(self._number_2, '2')
        self.screen.onkey(self._number_3, '3')
        self.screen.onkey(self._number_4, '4')
        self.screen.onkey(self._number_5, '5')
        self.screen.onkey(self._number_6, '6')
        self.screen.onkey(self._number_7, '7')
        self.screen.onkey(self._number_8, '8')
        self.screen.onkey(self._number_9, '9')

        # register blank space event
        self.screen.onkey(self._space, 'space')

    def _clear(self):
        # First, hide all turtles
        for obj in self.expr_images:
            obj.hideturtle()

        # Then, reset their positions
        for obj in self.expr_images:
            obj.setpos(self.beginx, self.beginy)

        self.expr_images = []

    def _draw(self):
        if not self.expr_images:
            self._gen_expr_objs()

        collision = False
        i = 0
        for obj in self.expr_images:
            x = self.beginx + i * self.diffx
            y = obj.ycor() - self.diffy
            if y < -self.screen.window_height()/2:
                collision = True
                break
            else:
                obj.setpos(x, y)
                if not obj.isvisible():
                    obj.showturtle()
                i += 1

        if collision:
            self.records['trying'] += 1
            print("trying", self.records['trying'])
            self._clear()

        self.screen.ontimer(self._draw, 1000)

    def main(self):
        self.screen.listen()
        self._register_events()
        self._register_images()
        self._draw()
        self.screen.mainloop()

    def move_down(self):
        pass


if __name__ == '__main__':
    g = Arith()
    g.main()
