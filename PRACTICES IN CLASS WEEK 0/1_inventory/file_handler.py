class FileHandler:
    #filepath: str #indicated filepath is expected to be a string
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        return None

    def read(self) -> list[str]:
        rows: list[str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != '':
                rows.append(row.rstrip('\n'))
                row = filehandle.readline()
            filehandle.close()
        except Exception:
            print(f'File not found')
            exit(-1)
        return rows
