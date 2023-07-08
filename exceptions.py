

class FileFinderError(Exception):
    pass

class InvalidInputError(FileFinderError):
    pass

class ZeroFilesFoundError(FileFinderError):
    pass