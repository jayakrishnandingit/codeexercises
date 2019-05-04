#! /usr/bin/python3

def climb_stairs(n):
    if n <= 0:
        return -1
    if n == 1:
        return n

    each_step_counter = [0] * (n+1)
    each_step_counter[1] = 1
    each_step_counter[2] = 2
    for j in range(3, n+1):
        each_step_counter[j] = each_step_counter[j-1] + each_step_counter[j-2]
    return each_step_counter[n]


if __name__ == '__main__':
    print(climb_stairs(6))
