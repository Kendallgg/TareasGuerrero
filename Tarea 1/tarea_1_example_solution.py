# Importamos 're' para usar expresiones regulares (regex).
# Se utilizarán para validar que los strings contengan solo letras ASCII (A–Z, a–z) y dígitos (0–9).
import re

# ------------------ Códigos de estado que EL TEST ESPERA (en minúscula) ------------------

# Código de éxito general para ambas funciones.
codigo_exito = 0

# Códigos de error para count_char (exactamente los que exige el test).
err_no_string = -100          # 'cadena' no es string.
err_cadena_invalida = -200    # 'cadena' contiene caracteres fuera de [A-Za-z0-9].
err_caracter_invalido = -300  # 'caracter' no es string de 1 char alfanumérico ASCII.

# Códigos de error para multiplo_2 (exactamente los que exige el test).
err_param_tipo = -400         # parámetros no son enteros válidos (o base < 0 / multiplo <= 0).
err_multiplo_invalido = -500  # 'multiplo' no está en {1, 2, 4, 8, 16}.

# Patrón regex para validar alfanumérico ASCII estricto en toda la cadena:
#   ^ y $ anclan inicio y fin (la cadena completa debe cumplir el patrón).
#   [A-Za-z0-9]+ uno o más caracteres alfanuméricos ASCII.
_ascii_alnum_re = re.compile(r'^[A-Za-z0-9]+$')


def count_char(cadena, caracter):
    """
    Retorna una tupla (codigo, cantidad).
      - En éxito: (0, ocurrencias de 'caracter' en 'cadena').
      - En error: (codigo_de_error_negativo, None).
    """

    # a) Validar que 'cadena' sea un string.
    if not isinstance(cadena, str):
        return err_no_string, None

    # b) Validar que 'cadena' contenga solo letras y dígitos ASCII (sin espacios ni símbolos).
    if not _ascii_alnum_re.match(cadena):
        return err_cadena_invalida, None

    # c) Validar que 'caracter' sea:
    #    - string
    #    - de longitud exactamente 1
    #    - alfanumérico ASCII
    if not (isinstance(caracter, str) and len(caracter) == 1 and _ascii_alnum_re.match(caracter)):
        return err_caracter_invalido, None

    # d) Contar ocurrencias exactas de 'caracter' en 'cadena'.
    cantidad = cadena.count(caracter)

    # e) Devolver éxito y la cantidad hallada.
    return codigo_exito, cantidad


def multiplo_2(base, multiplo):
    """
    Retorna una tupla (codigo, resultado).
      - En éxito: (0, base*multiplo) calculado SIN usar '+', '*' ni bucles.
      - En error: (codigo_de_error_negativo, None).
    """

    # a) Validaciones de tipo/valor:
    #    - Ambos deben ser int (no strings, no floats).
    #    - El test permite base = 0 (por eso se usa base >= 0) y exige multiplo > 0.
    if not (isinstance(base, int) and isinstance(multiplo, int)):
        return err_param_tipo, None
    if base < 0 or multiplo <= 0:
        return err_param_tipo, None

    # b) Validar que 'multiplo' esté en el conjunto permitido {1, 2, 4, 8, 16}.
    if multiplo not in {1, 2, 4, 8, 16}:
        return err_multiplo_invalido, None

    # c) Cálculo SIN '+', '*' ni bucles mediante desplazamiento de bits:
    #    base << n  equivale a base * (2**n).
    #    Se mapea el múltiplo a la cantidad de bits a desplazar.
    shift_map = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}

    # Obtener el número de bits a desplazar desde el mapa.
    desplazamiento = shift_map[multiplo]

    # Desplazar bits a la izquierda; equivalente a multiplicar por 2**desplazamiento.
    resultado = base << desplazamiento

    # d) Devolver éxito y el resultado calculado.
    return codigo_exito, resultado
