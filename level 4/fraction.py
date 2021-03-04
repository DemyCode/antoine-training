# https://en.wikipedia.org/wiki/Fraction

class Fraction:
    # Create Fraction Number
    def __init__(self, num, denum = 1):
        # TODO
        pass
    
    # Check wheter two fraction number are equal
    def __eq__(self, other):
        # TODO
        pass

    # add 2 Fraction number together, returns a Fraction number
    def __add__(self, other):
        # TODO
        pass

    # substract 2 Fraction number together, returns a Fraction number
    def __sub__(self, other):
        # TODO
        pass

    # multiply 2 Fraction number together, returns a Fraction number
    def __mul__(self, other):
        # TODO
        pass

    # divide 2 Fraction number together, returns a Fraction number
    def __truediv__(self, other):
        # TODO
        pass

    # evaluate the fraction number, returns a float
    def eval(self) -> float:
        # TODO
        pass

assert(Fraction(5) + Fraction(25) == Fraction(30))
assert(Fraction(5, 5) + Fraction(10, 5) == Fraction(2))
assert(Fraction(30, 15).eval() == 2)

# problem ?
assert(Fraction(2, 4) == Fraction(1, 2))