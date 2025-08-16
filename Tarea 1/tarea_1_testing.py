import tarea_1_example_solution
import random
import string
import pytest

# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo de count_char
# Error en caso de que cadena no sea un string => -100
# Error en caso de que cadena posea algo distinto a letras del abecedario o
# numeros del 0 al 9 => -200
# Error en caso de que parametro caracter posea mas de 1 caracter o no sea un
# valor del abecedario o numero del 0 al 9 => -300

# Errores esparados metodo de multiplo_2
# Error en caso de que los parametros no sean enteros positivos => -400
# Error en caso de que el parametro multiplo no este
# entre [1, 2, 4, 8, 16] => -500


# Prueba 1
# Verifica todos los casos de error de la solución
def test_casos_error_count_char():
    # Error si el parametro cadena no es un string
    estado, res = tarea_1_example_solution.count_char(cadena=7, caracter="a")
    assert estado == -100
    assert res is None

    # Error si cadena posee valores indebidos
    random_string = "abc{}123".format(random.choice(string.punctuation))
    estado, res = tarea_1_example_solution.count_char(
        cadena=random_string, caracter="a")
    assert estado == -200
    assert res is None

    # Error si el parametro caracter no es un unico caracter
    estado, res = tarea_1_example_solution.count_char(
        cadena="example", caracter="ab")
    assert estado == -300
    assert res is None

    # Error si el parametro caracter no es un caracter
    estado, res = tarea_1_example_solution.count_char(
        cadena="example", caracter=8)
    assert estado == -300
    assert res is None

    # Error si el parametro caracter no es valido
    random_invalid_char = random.choice(string.punctuation)
    estado, res = tarea_1_example_solution.count_char(
        cadena="example", caracter=random_invalid_char)
    assert estado == -300
    assert res is None


# Prueba 2
# Verifica casos de exito de la funcion
def test_casos_exito_count_char():
    estado, res = tarea_1_example_solution.count_char(
        cadena="A12CD3GBPXA", caracter="A")
    assert estado == 0
    assert res == 2

    estado, res = tarea_1_example_solution.count_char(
        cadena="asdpom1638416asdf", caracter="x")
    assert estado == 0
    assert res == 0

    estado, res = tarea_1_example_solution.count_char(
        cadena="apdPoP1638p16asPf", caracter="P")
    assert estado == 0
    assert res == 3

    estado, res = tarea_1_example_solution.count_char(
        cadena="ad16839s888sd51af", caracter="8")
    assert estado == 0
    assert res == 4


# Prueba 3
# Verifica los casos de error de la funcion de multiplo_2
def test_casos_error_multiplo_2():
    estado, result = tarea_1_example_solution.multiplo_2(base="c", multiplo=2)
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.multiplo_2(base=2, multiplo="c")
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.multiplo_2(base="", multiplo="c")
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.multiplo_2(base=900, multiplo=7)
    assert estado == -500
    assert result is None


# Prueba 4
# Verifica los casos de exito de la funcion de multiplo_2
def test_casos_exito_multiplo_2():
    param2 = random.choice([1, 2, 4, 8, 16])
    param1 = random.randint(0, 100)
    expected_result = param1 * param2

    print(param1, "---", param2)
    estado, result = tarea_1_example_solution.multiplo_2(
        base=param1, multiplo=param2)
    assert estado == 0
    assert result == expected_result
