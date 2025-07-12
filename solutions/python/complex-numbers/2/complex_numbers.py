import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __radd__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    

    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = [self.real, self.imaginary, other.real, other.imaginary]
        return ComplexNumber((a * c - b * d), (b * c + a * d))
    
    def __rmul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = [self.real, self.imaginary, other.real, other.imaginary]
        return ComplexNumber((a * c - b * d), (b * c + a * d))
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = [self.real, self.imaginary, other.real, other.imaginary]
        return ComplexNumber((a - c), (b - d))
    
    def __rsub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = [self.real, self.imaginary, other.real, other.imaginary]
        return ComplexNumber((c - a), (d - b))
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = [self.real, self.imaginary, other.real, other.imaginary]
        return ComplexNumber((a * c + b * d) / (c**2 + d**2), (b * c - a * d) / (c**2 + d**2))
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a, b, c, d = other.real, other.imaginary, self.real, self.imaginary
        denominator = c**2 + d**2
        return ComplexNumber((a * c + b * d) / denominator, (b * c - a * d) / denominator)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        a, b = [self.real, self.imaginary]
        return ComplexNumber((math.e ** a * math.cos(b)), (math.e ** a * math.sin(b)))
        
    def __str__(self):
        return f'{self.real}+{self.imaginary}*i'