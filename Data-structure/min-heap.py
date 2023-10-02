def difference(arr):
    diff = []
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            diff.append(abs(arr[j]-arr[i]))
    return diff


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

    return arr


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


with open('input', 'r') as f:
    new = open('output', 'w')
    for line in nonblank_lines(f):
        pre_arr = line.split()
        arr = []
        for i in range(len(pre_arr)):
            arr.append(int(pre_arr[i]))
        k = arr[0]
        diff_array = difference(arr)
        final = heapSort(diff_array)
        new.write(str(final[k-1]) + "\n")
    new.close()
