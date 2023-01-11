from rich.console import Console
from rich.table import Table
from typer import Argument, Option, Typer

from .escalas import escala
from .notas import campo_harmonico

console = Console()
app = Typer()


@app.command()
def escalas(
    tonica: str = Argument(
        'C',
        help='Tônica da escala. Por exemplo C, C#, ...',
    ),
    tonalidade=Argument(
        'maior',
        help='Tonalidade da escala. Por exemplo: maior, menor, ...',
    ),
    harmonia: bool = Option(False),
):
    table = Table(title=f'Escala {tonalidade} de {tonica}')
    if harmonia:
        notas, graus = campo_harmonico(tonica, tonalidade).values()
    else:
        notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau, justify='center')

    table.add_row(*notas)

    console.print(table)
