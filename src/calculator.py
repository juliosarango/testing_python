def suma(a, b):
    """Add two numbers

    Args:
        a (numeric): First number
        b (numeric): Second number

    Returns:
        numeric: Return the result of addition

    >>> suma(4,5)
    9

    >>> suma(14,20)
    34
    """
    return a + b


def resta(a, b):
    """Diff two numbers

    Args:
        a (numeric): First number
        b (numeric): Second number

    Returns:
        numeric: Result

    >>> resta(3,44)
    -41
    """
    return a - b


def multiplicacion(a, b):
    """Multiply two numbers

    Args:
         a (numeric): First number
        b (numeric): Second number

    Returns:
        numeric: Result
    >>> multiplicacion(4,6)
    24
    >>> multiplicacion(4,0)
    0
    """
    return a * b


def division(a, b):
    """_summary_

    Args:
         a (numeric): First number
        b (numeric): Second number

    Raises:
        ZeroDivisionError: _description_

    Returns:
        numeric: Result

    >>> division(20,5)
    4.0
    >>> division(20,0)
    Traceback (most recent call last):
    ZeroDivisionError: Operación no permitida
    """
    if b == 0:
        raise ZeroDivisionError("Operación no permitida")

    return a / b
