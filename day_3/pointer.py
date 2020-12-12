class Pointer:
    def __init__(self, world):
        self.x = 0
        self.y = 0
        self.visited_trees = 0
        self.world = world

    def step(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        if self.world.get_point(self.x, self.y) == self.world.TREE:
            self.visited_trees += 1
