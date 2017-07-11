class CompilerError(Exception):
    def __init__(self, msg: str, line: int):
        self.msg = msg
        self.line = line + 1

    def __str__(self):
        return self.msg + ' @ line ' + str(self.line)