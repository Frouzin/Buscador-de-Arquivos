import click
from pathlib import Path

@click.command()
@click.argument("path", default="")
def finder(path):
    root = Path(path)

    click.echo(f"O diretorio selecionado foi {root.absolute()}")

    for item in root.iterdir():
        print(item)

finder()