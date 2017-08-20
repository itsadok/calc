#!/usr/bin/env python3
from lark import Lark, InlineTransformer

with open('calc/calc.g') as f:
    parser = Lark(f.read(), start='program')

class CalculateTree(InlineTransformer):
    from operator import add, sub, mul, floordiv as div, neg
    number = int
    identifier = str

    def __init__(self):
        self.vars = {}

    def assign(self, ident, value):
        self.vars[ident] = value

    def assign_plus(self, ident, value):
        self.vars[ident] += value

    def value(self, ident):
        return self.vars[ident]

    def pre_inc(self, ident):
        self.vars[ident] += 1
        return self.vars[ident]

    def post_inc(self, ident):
        self.vars[ident] += 1
        return self.vars[ident] - 1

    def program(self, *args):
        return self.vars        


def run(program):
    vars = CalculateTree().transform(parser.parse(program))
    return "(%s)" % ",".join(["%s=%s" % kv for kv in sorted(vars.items())])


def parse(program):
    print(parser.parse(program).pretty())


if __name__ == '__main__':
    import sys
    print(run(sys.stdin.read()))
