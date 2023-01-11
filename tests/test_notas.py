from pytest import mark

from notas_musicais.notas import (
    campo_harmonico,
    conversao_de_graus,
    maior_menor,
    triade,
)


@mark.parametrize(
    'nota, acorde',
    [
        ('C', ('C', 'E', 'G')),
        ('D#', ('D#', 'G', 'A#')),
        ('E', ('E', 'G#', 'B')),
    ],
)
def test_triade_deve_ternoar_3_notas(nota, acorde):
    assert acorde == triade(nota)


def test_campo_harmonico():
    tonica = 'C'
    tonalidade = 'maior'
    esperado = {
        'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'],
        'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'],
    }

    assert esperado == campo_harmonico(tonica, tonalidade)


@mark.parametrize(
    'acorde,esperado',
    [
        (('C', 'E', 'G'), 'C'),
        (('D', 'F#', 'A'), 'Dm'),
        (('B', 'D#', 'F#'), 'B°'),
    ],
)
def test_maior_menor_deve_retornar_acordes_maiores_e_menores(
    acorde,
    esperado,
):
    notas = 'C D E F G A B'.split()
    assert esperado == maior_menor(acorde, notas)


@mark.parametrize(
    'acorde,grau,esperado',
    [
        ('Dm', 'I', 'i'),
        ('C#m', 'II', 'ii'),
        ('C', 'V', 'V'),
        ('B°', 'II', 'ii°'),
    ],
)
def test_conversao_de_graus(acorde, grau, esperado):
    assert esperado == conversao_de_graus(acorde, grau)
