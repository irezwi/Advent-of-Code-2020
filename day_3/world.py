class WorldBoundariesExceeded(Exception):
    pass


class World:
    TREE = '#'
    FREE_SPACE = '.'

    def __init__(self, lines):
        self.points = list(map(lambda x: list(iter(x)), lines))
        self.width = len(lines[0])
        self.height = len(lines)

    def get_point(self, x, y):
        try:
            return self.points[y][x % self.width]
        except IndexError:
            raise WorldBoundariesExceeded from IndexError
