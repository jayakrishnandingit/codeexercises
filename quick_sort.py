def quicksort(arr, low, high):
	stack = [high, low]
	while len(stack) > 0:
		low = stack.pop()
		high = stack.pop()

		pivot_index = partition(arr, low, high)

		if pivot_index > low:
			stack.append(pivot_index - 1)
			stack.append(low)
		if pivot_index < high:
			stack.append(high)
			stack.append(pivot_index + 1)
	return arr


def partition(arr, low, high):
		pivot = arr[high]
		smaller_index = low

		running_index = low
		while running_index < high:
			if arr[running_index] < pivot:
				arr[running_index], arr[smaller_index] = arr[smaller_index], arr[running_index]
				smaller_index += 1
			running_index += 1

		arr[smaller_index], arr[high] = arr[high], arr[smaller_index]
		return smaller_index


if __name__ == '__main__':
	l = [10, 80, 30, 90, 40, 50, 70]
	l = quicksort(l, 0, len(l) - 1)
	print(l)

# low = 0
# high = 6
# pivot = 70

# smaller_index = 0
# running_index = 0
# 10 < 70
# 10 80 30 90 40 50 70

# smaller_index = 1
# running_index = 1
# 80 < 70

# smaller_index = 1
# running_index = 2
# 30 < 70
# 10 30 80 90 40 50 70

# smaller_index = 2
# running_index = 3
# 90 < 70

# smaller_index = 2
# running_index = 4
# 40 < 70
# 10 30 40 90 80 50 70

# smaller_index = 3
# running_index = 5
# 50 < 70
# 10 30 40 50 80 90 70

# smaller_index = 4
# running_index = 6
# # exit while loop.

# # swap smaller_index with pivot.
# 10 30 40 50 70 90 80

# pivot_index = 

