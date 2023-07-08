from datetime import datetime
from exceptions import InvalidInputError

def get_folders(path):
    """PUXA PASTAS DE UM DIRETORIO PESQUISADO"""
    return [file for file in path.iterdir() if file.is_dir()]

def get_files(path):
    """PUXA ARQUIVOS DE UM DIRETORIO PESQUISADO"""
    return [file for file in path.iterdir() if file.is_file()]


def find_by_name(path,value):
    """ENCONTRAR ARQUIVOS POR NOME"""
    return [file for file in get_files(path) if file.stem == value]

def find_by_ext(path,value):
    """ENCONTRAR ARQUIVOS POR EXTENSÃO"""
    return [file for file in get_files(path) if file.suffix == value]

def find_by_mod(path,value):
    """"ENCONTRAR ARQUIVOS POR DATA"""
    try:
        datetime_obj = datetime.strptime(value, "%d/%m/%Y")
    except ValueError:
        raise InvalidInputError(f"'{value}'não é uma data valida no formado dd/mm/aaaa!")

    return [file for file in get_files(path) if datetime.fromtimestamp(file.stat().st_mtime >= datetime_obj)]

   
# [file for file in get_files(path) if file.is_file()]

def timestamp_to_string(system_timestamp):
    datetime_obj = datetime.fromtimestamp(system_timestamp)
    return datetime_obj.strftime('%d/%m/%Y - %H:%M:%S:%f')

def get_files_details(files):
    files_details = []

    for file in files:
        stat = file.stat()
        details = [

            file.name,
            timestamp_to_string(stat.st_ctime),
            timestamp_to_string(stat.st_mtime),
            file.absolute(),
        ]

        files_details.append(details)
    return files_details
