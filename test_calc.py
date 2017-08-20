#!/usr/bin/env python3
import calc
import unittest

class TestCalc(unittest.TestCase):

    def test_assign(self):
        self.assertEqual('(i=1)', calc.run('i=1'))

    def test_whitespace(self):
        self.assertEqual('(i=1)', calc.run('\n\n\ti = 1\n'))

    def test_add(self):
        self.assertEqual('(i=3)', calc.run('i=1+2'))

    def test_sub(self):
        self.assertEqual('(i=-1)', calc.run('i=1-2'))

    def test_mul(self):
        self.assertEqual('(i=12)', calc.run('i=6*2'))

    def test_div(self):
        self.assertEqual('(i=3)', calc.run('i=6/2'))

    def test_multiterm(self):
        self.assertEqual('(i=22)', calc.run('i=3*4+2*5'))
        self.assertEqual('(i=0)', calc.run('i=1+2+3-3-2-1'))

    def test_negative(self):
        self.assertEqual('(i=1)', calc.run('i = -1*3 - 4*-3 + -8'))
        self.assertEqual('(i=-4)', calc.run('i = -2-2'))

    def test_multiline(self):
        self.assertEqual('(i=3,j=4)', calc.run('i=3\nj=4'))

    def test_assign_plus(self):
        self.assertEqual('(i=4)', calc.run('i=3\ni+=1'))

    def test_ident_value(self):
        self.assertEqual('(i=3,j=3)', calc.run('i=3\nj=i'))

    def test_pre_inc(self):
        self.assertEqual('(i=4,j=4)', calc.run('i=3\nj=++i'))
        self.assertEqual('(i=4,j=6)', calc.run('i=3\nj=2+++i'))

    def test_post_inc(self):
        self.assertEqual('(i=4,j=3)', calc.run('i=3\nj=i++'))

    def test_program(self):
        program = '''
            i = 0
            j = ++i
            x = i++ + 5
            y = 5 + 3 * 10
            i += y
        '''
        self.assertEqual('(i=37,j=1,x=6,y=35)', calc.run(program))

    def test_invalid(self):
        self.assertRaises(calc.ParseError, calc.run, '3')

    def test_ref_before_assign(self):
        self.assertRaises(KeyError, calc.run, 'i=j')

if __name__ == '__main__':
    unittest.main()
