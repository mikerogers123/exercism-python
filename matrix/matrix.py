class Matrix:
    def __init__(self, matrix_string):
        self._rows = [line.split(' ') for line in matrix_string.splitlines()]
        self._rows = [[int(val) for val in r] for r in self._rows]

    def row(self, index):
        return [x for x in self._rows[index - 1]]

    def column(self, index):
        return [i[index - 1] for i in self._rows]
