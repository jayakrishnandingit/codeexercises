#!/usr/bin/env python3

def climb_stairs(num_of_stairs, steps_set):
    """
    4th step.
    
    allowed steps = 1
    no of ways = 1 (i.e, no of ways you can reach from step 3).

    allowed steps = 3
    no of ways = 0 (i.e no of ways you can reach from 1st step which is 0 as well).

    allowed steps = 1, 2
    no of ways = 5
    i.e, no of ways you can reach 3rd step + no of ways you can reach 2nd step.
    """
    if num_of_stairs is None:
        return -1
    if num_of_stairs == 0:
        return 1
    if not steps_set:
        return -1
    # create an array where each index corresponds to a step number and
    # zero index is the ground level. the value at each index corresponds to
    # the number of ways to reach that step.
    ways = [0] * (num_of_stairs + 1)
    ways[0] = 1  # to be at the ground there is only one way.
    for step_number in range(1, num_of_stairs):
        total = 0
        for num_of_steps in steps_set:
            if step_number - num_of_steps >= 0:
                # iff this step is accessible by the number of steps allowed.
                total += ways[step_number - num_of_steps]
        ways[step_number] = total
    return ways[n]
 

if __name__ == '__main__':
    print(climb_stairs(6, {1,3,5}))
