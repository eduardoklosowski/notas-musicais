"""Módulo referente a criação de escalas musicais."""

NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala, grau I
        tonalidade: Tonalidade da escala, ex: 'maior', 'menor'

    Returns:
        Um dicionário com as notas da escala e seus respectivos graus.

    Raises:
       ValueError: Caso a tônica não exista
       KeyError: Caso a escala não exista

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()

    try:
        tonica_pos = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]
    except ValueError:
        raise ValueError(
            f'Essa nota não existe em nossa escala. '
            f'Tente uma dessas {NOTAS}'
        )
    except KeyError:
        raise KeyError(
            f'Essa escala não existe em nossa aplicação. '
            f'Tente uma dessas {list(ESCALAS)}'
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        grau = NOTAS[nota]
        temp.append(grau)

    return {
        'notas': temp,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
