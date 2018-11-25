"""
A really simple implementation of the Flood Fill algorithm.
by Al Sweigart
http://inventwithpython.com

This script can be run with either Python 2 or Python 3.
"""

import sys

textmap = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""

lines = textmap.strip().split('\n')
assert ['bad width' for x in lines if len(x) != len(lines[0])] == [], "WORLD string needs to be rectangular."


def get_world_from_text_map(textmap):
    # Converts the programmer-friendly version of a world typed out as ascii
    # characters in a multi-line string into a source code-friendly version
    # that lets us access the map as world[x][y].
    world_width = len(textmap.strip().split('\n')[0])
    world_height = len(textmap.strip().split('\n'))

    textmap = textmap.strip().split('\n')

    world = []
    for i in range(world_width):
        world.append([''] * world_height)
    for x in range(world_width):
        for y in range(world_height):
            world[x][y] = textmap[y][x]
    return world


def print_world(world):
    world_width = len(world)
    world_height = len(world[0])

    for y in range(world_height):
        for x in range(world_width):
            sys.stdout.write(world[x][y])
        sys.stdout.write('\n')


def flood_fill(world, x, y, old_char, new_char):
    # The recursive algorithm. Starting at x and y, changes any adjacent
    # characters that match oldChar to newChar.
    world_width = len(world)
    world_height = len(world[0])

    if old_char is None:
        old_char = world[x][y]

    if world[x][y] != old_char:
        # Base case. If the current x, y character is not the oldChar,
        # then do nothing.
        return

    # Change the character at world[x][y] to newChar
    world[x][y] = new_char

    # Recursive calls. Make a recursive call as long as we are not on the
    # boundary (which would cause an Index Error.)
    if x > 0:  # left
        flood_fill(world, x-1, y, old_char, new_char)

    if y > 0:  # up
        flood_fill(world, x, y-1, old_char, new_char)

    if x < world_width-1:  # right
        flood_fill(world, x+1, y, old_char, new_char)

    if y < world_height-1:  # down
        flood_fill(world, x, y+1, old_char, new_char)


def main():
    world = get_world_from_text_map(textmap)
    print_world(world)
    print()

    flood_fill(world, 5, 8, None, '+')
    print_world(world)
    print()

    flood_fill(world, 0, 0, None, 's')
    print_world(world)
    print()


if __name__ == '__main__':
    main()
