"""
AAA

Arange: Organizar os dados que são enviados para o teste
Act: Onde chamamos o código com os dados arranjados
Assert: Verificação do retorno com o que era esperado
"""
import pytest

from notas_musicais.escalas import ESCALAS, NOTAS, escala

graus = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


@pytest.mark.parametrize(
    'tonica,notas',
    [
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('E', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
    ],
)
def test_escala_deve_retornar_notas_e_graus_da_escala_maior(tonica, notas):
    """
    Escalas baseadas em: descomplicandoamusica.com/wp-content/uploads/2014/08/escala-maior-12-notas.png
    """
    # Arange
    tonalidade = 'maior'
    esperado = {
        'notas': notas,
        'graus': graus,
    }

    # Act
    resultado = escala(tonica, tonalidade)

    # Assert
    assert esperado == resultado


@pytest.mark.parametrize(
    'tonica,notas',
    [
        ('C', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('D', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('E', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
    ],
)
def test_escala_deve_retornar_notas_e_graus_da_escala_menor(tonica, notas):
    tonalidade = 'menor'
    esperado = {
        'notas': notas,
        'graus': graus,
    }

    resultado = escala(tonica, tonalidade)

    assert esperado == resultado


def test_escala_deve_funcionar_com_tonicas_minusculas():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = {
        'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }

    resultado = escala(tonica, tonalidade)

    assert esperado == resultado


def test_caso_a_nota_nao_exista_deve_retornar_um_erro_dizendo_isso():
    msg = f'Essa nota não existe em nossa escala. Tente uma dessas {NOTAS}'

    with pytest.raises(ValueError) as error:
        escala('B#', 'maior')

    assert msg == error.value.args[0]


def test_caso_a_escala_nao_exista_deve_retornar_um_erro_dizendo_isso():
    msg = (
        f'Essa escala não existe em nossa aplicação. '
        f'Tente uma dessas {ESCALAS}'
    )

    with pytest.raises(KeyError) as error:
        escala('C', 'xpto')

    assert msg == error.value.args[0]
