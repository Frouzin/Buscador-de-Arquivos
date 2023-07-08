import click
from pathlib import Path

@click.command()
@click.argument("path", default="")
@click.option("-k","--key", required=True, type=click.Choice(["name","ext","modified"]))
@click.option("-v", "--value",required=True)
def finder(path, key, value):
    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho não é um diretorio!")

    click.echo(f"O diretorio selecionado foi {root.absolute()}")

    if key == "name":
        file = [file for file in root.iterdir() if file.is_file() and file.name == value]
        if not file:
            click.echo(f" Nenhum arquivo com o nome {value} foi encontrado")
        else:
            f = file[0]
            click.echo(f"Nome: {f.name}\nData Modificacao: {f.stat().st_mtime}\nLocalizacao: {root.absolute()}")
    elif key == "ext":
        pass
    else:
        pass


    for item in root.iterdir():
        print(item)

finder()