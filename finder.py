import click
import shutil
from pathlib import Path
from utils import find_by_ext,find_by_name,find_by_mod,timestamp_to_string, get_folders
from datetime import datetime

def process_search(path, key, value,recursive):
    search_mapping = {
        "name": find_by_name,
        "ext" : find_by_ext,
        "mod" : find_by_mod,
    }

    files = search_mapping[key](path,value)

    if recursive:
        subdirs = get_folders(path)
        for subdir in subdirs:
            files += process_search(subdir, key, value, recursive)

    return files

def process_results(files, key, value):
    if not files:
            click.echo(f" Nenhum arquivo com o {key} {value} foi encontrado")
    else:
        for f in files:
            click.echo(
                f"Nome: {f.name}\n"
                f"Data de Criacao: {timestamp_to_string(f.stat().st_ctime)}\n"
                f"Data Modificacao: {timestamp_to_string(f.stat().st_mtime)}\n"
                f"Localizacao: {f.parent.absolute()}"
                )

@click.command()
@click.argument("path", default="")
@click.option("-k","--key", required=True, type=click.Choice(["name","ext","mod"]))
@click.option("-v", "--value",required=True)
@click.option("-r","--recursive", is_flag=True, default=False)
@click.option("-c","--copy-to")


def finder(path, key, value,recursive, copy_to):

    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho não é um diretorio!")

    click.echo(f"O diretorio selecionado foi {root.absolute()}")

    files = process_search(path=root, key=key, value=value, recursive=recursive)
    process_results(files=files, key=key, value=value)

    if copy_to:
        copy_path = Path(copy_to)
        if not copy_path.is_dir():
            copy_path.mkdir(parents=True)

        for file in files:
            dst_file = copy_path/file.name
            if dst_file.is_file():
                dst_file = copy_path/ f"{file.stem}{datetime.now().strftime('%d%m%Y%H%M%S%f')}{file.suffix}"
            shutil.copy(src=file.absolute(), dst=dst_file)

finder()