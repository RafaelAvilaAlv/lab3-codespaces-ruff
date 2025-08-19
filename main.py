from src.operaciones import dividir, sumar

print("suma:", sumar(2, 3))

try:
    print("div:", dividir(10, 0))  # fuerza el caso de error
except ZeroDivisionError as e:
    print("div: error ->", e)
