from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from .escalas import escala

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
):
    table = Table(title=f'Escala {tonalidade} de {tonica}')
    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau, justify='center')

    table.add_row(*notas)

    console.print(table)
