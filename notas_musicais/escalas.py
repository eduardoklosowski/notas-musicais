"""Módulo referente a criação de escalas musicais."""

NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala, grau I
        tonalidade: Tonalidade da escala, ex: 'maior', 'menor'

    Returns:
        Um dicionário com as notas da escala e seus respectivos graus.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)

    temp = []

    for intervalo in intervalos:
        nota = tonica_pos + intervalo
        grau = NOTAS[nota]
        temp.append(grau)

    return {
        'notas': temp,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
