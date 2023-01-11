from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():
    result = runner.invoke(app)
    assert 0 == result.exit_code


@mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_escala_cli_deve_conter_as_notas_no_stdout(nota):
    result = runner.invoke(app)

    assert nota in result.stdout


@mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_escala_cli_deve_conter_os_graus_no_stdout(grau):
    result = runner.invoke(app)

    assert grau in result.stdout


@mark.parametrize('tonica,tonalidade', [('C', 'maior'), ('D#', 'menor')])
def test_ecala_cli_deve_exibir_a_tonalidade_e_a_tonica(tonica, tonalidade):
    msg = f'Escala {tonalidade} de {tonica}'
    result = runner.invoke(app, [tonica, tonalidade])

    assert msg in result.stdout
