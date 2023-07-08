import click
import shutil
from pathlib import Path
from utils import  get_folders,get_files_details
from datetime import datetime
from tabulate import tabulate
from constants import SEARCH_MAPPING, TABLE_HEADERS

def process_search(path, key, value,recursive):
   

    files = SEARCH_MAPPING[key](path,value)

    if recursive:
        subdirs = get_folders(path)
        for subdir in subdirs:
            files += process_search(subdir, key, value, recursive)

    return files

def process_results(files, key, value):
    if not files:
            click.echo(f" Nenhum arquivo com o {key} {value} foi encontrado")
    else:
        table_data = get_files_details(files)
        tabulate_data = tabulate(tabular_data=table_data,headers=TABLE_HEADERS,tablefmt="tsv")
        click.echo(tabulate_data)
        return tabulate_data

    return None
        # for f in files:
        #     click.echo(
        #         f"Nome: {f.name}\n"
        #         f"Data de Criacao: {timestamp_to_string(f.stat().st_ctime)}\n"
        #         f"Data Modificacao: {timestamp_to_string(f.stat().st_mtime)}\n"
        #         f"Localizacao: {f.parent.absolute()}"
        #         )

def save_report(save,report,root):
        if save and report:
            report_file_path = root / f"finder_report_{datetime.now().strftime('%d%m%Y%H%M%S%f')}.txt"
            with open(report_file_path.absolute(), mode="w") as report_file:
                report_file.write(report)

def copy_files(copy_to, files):
    if copy_to:
        copy_path = Path(copy_to)
    if not copy_path.is_dir():
        copy_path.mkdir(parents=True)

    for file in files:
        dst_file = copy_path/file.name
        if dst_file.is_file():
            dst_file = copy_path/ f"{file.stem}{datetime.now().strftime('%d%m%Y%H%M%S%f')}{file.suffix}"
        shutil.copy(src=file.absolute(), dst=dst_file)


@click.command()
@click.argument("path", default="")
@click.option("-k","--key", required=True, type=click.Choice(SEARCH_MAPPING.keys()))
@click.option("-v", "--value",required=True)
@click.option("-r","--recursive", is_flag=True, default=False)
@click.option("-s","--save", is_flag=True, default=False)
@click.option("-c","--copy-to")


def finder(path, key, value,recursive, copy_to, save):

    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho não é um diretorio!")

    click.echo(f"O diretorio selecionado foi {root.absolute()}")

    files = process_search(path=root, key=key, value=value, recursive=recursive)
    report = process_results(files=files, key=key, value=value)
    save_report(save=save,report=report,root=root)
    copy_files(copy_to=copy_to,files=files)

finder()