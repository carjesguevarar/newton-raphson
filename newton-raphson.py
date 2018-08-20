def f(n, x):
    """
    Función que devuelve el valor de la función en una de sus derivadas, o en la función original.
    :param n: Indicador del número de derivada que se desea, o cero para la función original.
    :param x: Punto en donde se evalua la función.
    :return: Valor de la función evaluada.
    """
    return {
        0: x**3 - 2*x**2 - 5,
        1: 3*x**2 - 4*x**1,
        2: 6*x**1 - 4
    }[n]


def tenet(v):
    """
    Fúnción que verifica la factibilidad de aplicar el método de Newton-Raphson.
    :param v: Valor de 'xsub0'.
    :return: Valor lógico de la factibilidad del método.
    """
    if abs((f(0, v)*(f(2, v)))/((f(1, v))**2)) < 1:
        return True
    else:
        return False


def xian(v):
    """
    Función que calcula 'xsubi+1', perteneciente a la ecuación del método.
    :param v: Valor de 'xsub0'.
    :return: Valor numérico de 'xsubi+1'.
    """
    return v - ((f(0, v)) / (f(1, v)))


def calder(xi, xaddo):
    """
    Función que calcula el error relativo, perteneciente al método.
    :param xi: Valor de 'xi'.
    :param xaddo: valor de 'xiaddimásuno'.
    :return: Error relativo, en base a los dos valores.
    """
    return abs((xi - xaddo)/xaddo)


def newtonraphson(maxit, err, a, b):
    """
    Fúnción de busqueda de la raíz, en la ecuación mediante el método de Newton-Raphson.
    :param maxit: Máximo número de iteraciónes.
    :param err: Valor del error aceptado.
    :param a: Intervalo inferior.
    :param b: Intervalo superior.
    :return: Raíz de la función tal qué, f(valor) = 0, o esta se aproxime.
    """
    i = 0
    xi = (a + b) / 2
    xione = xian(xi)
    erri = calder(xi, xione)
    while i < maxit and erri > err:
        xione = xian(xi)
        erri = calder(xi, xione)
        xi = xione
        i = i + 1
    return xione
