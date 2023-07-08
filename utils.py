

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
    """ENCONTRAR ARQUIVOS POR NOME"""
    [file for file in get_files(path) if file.is_file()]
