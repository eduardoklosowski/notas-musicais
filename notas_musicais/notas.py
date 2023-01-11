from .escalas import escala


def triade(nota):
    triade = (0, 2, 4)
    notas, _ = escala(nota, 'maior').values()

    return tuple(notas[pos] for pos in triade)


def maior_menor(acorde, notas):
    tonica, terca, quinta = acorde

    match terca in notas, quinta in notas:
        case True, True:
            return f'{tonica}'
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}°'


def conversao_de_graus(acorde, grau):
    if 'm' in acorde:
        return grau.lower()

    if '°' in acorde:
        return f'{grau.lower()}°'

    return grau


def campo_harmonico(tonica, tonalidade):
    notas, graus = escala(tonica, tonalidade).values()

    acordes = [maior_menor(triade(nota), notas) for nota in notas]

    graus = [
        conversao_de_graus(acorde, grau)
        for acorde, grau in zip(acordes, graus)
    ]

    return {'acordes': acordes, 'graus': graus}
