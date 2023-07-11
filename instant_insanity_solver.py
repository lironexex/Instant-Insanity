import itertools


def check_solution(cubes):
    result = True
    color_sum = 0
    for i in range(0, 6):
        # print(color_sum)
        if color_sum != 308 and color_sum != 0:
            result = False
        color_sum = 0
        if i == 0 or i == 3:
            continue
        for cube in cubes:
            color_sum += ord(cube[i])

    return result


def rotate_front_to_left_clockwise(cube):
    temp = cube[0]
    cube[0] = cube[1]
    cube[1] = cube[5]
    # cube[2] = cube[2] unchanged
    # cube[4] = cube[4] unchanged
    cube[5] = cube[3]
    cube[3] = temp
    cube[6] += 1
    cube[6] = cube[6] % 24


def flip_front_up(cube):
    temp = cube[0]
    cube[0] = cube[4]
    # cube[1] = cube[1] unchanged
    # cube[3] = cube[3] unchanged
    cube[4] = cube[5]
    cube[5] = cube[2]
    cube[2] = temp
    cube[6] += 1


def flip_front_down(cube):
    temp = cube[0]
    cube[0] = cube[2]
    # cube[1] = cube[1] unchanged
    cube[2] = cube[5]
    # cube[3] = cube[3] unchanged
    cube[5] = cube[4]
    cube[4] = temp
    cube[6] += 1


def change_cube(cube):

    if cube[6] % 4 < 3:
        rotate_front_to_left_clockwise(cube)
        return
    if cube[6] == 3 or cube[6] == 7 or cube[6] == 19:
        flip_front_up(cube)
    else:
        flip_front_down(cube)


def solve_instant_insanity(cubes):
    number_of_options = 24
    for i in range(0, number_of_options):
        for j in range(0, number_of_options):
            for k in range(0, number_of_options):
                for m in range(0, number_of_options):
                    if check_solution(cubes):
                        print(cubes)
                        return True
                    change_cube(cubes[3])
                change_cube(cubes[2])
            change_cube(cubes[1])
        change_cube(cubes[0])


# Example usage:
#      [0]
#   [1][2][3][4]
#      [5]
#
##################
#
# [0] = back, [1] = left, [2] = bottom, [3] = right, [4] = top, [5] = front
#
cubes_input = [
    ['B', 'R', 'R', 'R', 'G', 'Y', 0],
    ['R', 'G', 'Y', 'G', 'B', 'B', 0],
    ['R', 'B', 'G', 'R', 'Y', 'Y', 0],
    ['G', 'B', 'R', 'Y', 'G', 'Y', 0]
]

print(solve_instant_insanity(cubes_input))
