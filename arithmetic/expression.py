import random


class Expression(object):

    def __init__(self, min, max, operators):
        self._min = min
        self._max = max
        self._operators = operators.split()
        self.expr = None
        self.result = None

    def gen_expr(self):
        x, y = random.sample(range(self._min, self._max), 2)
        oper = random.choice(self._operators)
        expr = '{x} {oper} {y}'
        result = eval(expr.format(x=x, oper=oper, y=y))
        (x, y) = (y, x) if result < 0 else (x, y)
        print(x, y)
        self.expr = expr.format(x=' '.join([s for s in str(x)]),
                                oper=oper,
                                y=' '.join([s for s in str(y)])).split()
        self.expr.append('=')
        self.expr.append('?')
        print(self.expr)
        self.result =  result if result > 0 else -result


if __name__ == '__main__':
    arith = Expression(0, 20, '- +')
    arith.gen_expr()
    print(self.expr)
    print(self.result)

