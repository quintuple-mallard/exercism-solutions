import math


class ComplexNumber:
    def __init__(self: object, real: int | float, imaginary: int | float) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def __eq__(self: object, other: object) -> bool:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __add__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __radd__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )
    
    def __rmul__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )
    
    def __sub__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            self.real - other.real, 
            self.imaginary - other.imaginary
        )
    
    def __rsub__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            other.real - self.real,
            other.imaginary - self.imaginary
        )
    
    def __truediv__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
            (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        )
    
    def __rtruediv__(self: object | int | float, other: object | int | float) -> object:
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        denominator = self.real ** 2 + self.imaginary ** 2
        return ComplexNumber(
            ((other.real * self.real + other.imaginary * self.imaginary) / denominator),
            ((other.imaginary * self.real - other.real * self.imaginary) / denominator)
        )

    def __abs__(self: object) -> int | float:
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self: object) -> object:
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self: object) -> object:
        return ComplexNumber((math.e ** self.real * math.cos(self.imaginary)),
                             (math.e ** self.real * math.sin(self.imaginary))
                            )