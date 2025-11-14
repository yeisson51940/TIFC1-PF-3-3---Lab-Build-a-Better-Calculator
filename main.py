def main():
  print("Hello learners!")

def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0
    result = 1
    for n in numbers:
        result *= n
    return result


def isiteven(num):
    return isinstance(num, int) and num % 2 == 0


def isitaninteger(num):
    return isinstance(num, int)


def main():
    print("Hello learners!")

    # Ejemplos demostrativos:
    print("Suma de [1, 2, 3, 4]:", addmultiplenumbers([1, 2, 3, 4]))
    print("Multiplicación de [2, 3, 4]:", multiplymultiplenumbers([2, 3, 4]))
    print("¿4 es par?:", isiteven(4))
    print("¿5.5 es entero?:", isitaninteger(5.5))
    print("¿10 es entero?:", isitaninteger(10))


if __name__ == "__main__":
    main()