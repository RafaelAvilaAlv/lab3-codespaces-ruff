from typing import Union

Number = Union[int, float]


def sumar(a: Number, b: Number) -> float:
    return float(a) + float(b)


def dividir(a: Number, b: Number) -> float:
    if float(b) == 0.0:
        raise ZeroDivisionError("b no puede ser 0")
    return float(a) / float(b)
