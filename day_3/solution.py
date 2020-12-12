from functools import reduce

from utils.io import get_lines
from day_3.pointer import Pointer
from day_3.world import World, WorldBoundariesExceeded


def try_slope(s):
    world = World(get_lines("input.txt"))
    pointer = Pointer(world)

    while pointer.y < world.height:
        try:
            pointer.step(*s)
        except WorldBoundariesExceeded:
            break

    return pointer.visited_trees


# Part 1
print(f'Part 1 solution: {try_slope((3, 1))}')

# Part 2
slopes = {
    (1, 1): 0,
    (3, 1): 0,
    (5, 1): 0,
    (7, 1): 0,
    (1, 2): 0,
}

for slope in slopes.keys():
    slopes[slope] = try_slope(slope)

print(f'Part 2 solution: {reduce(lambda x, y: x * y, slopes.values())}')
