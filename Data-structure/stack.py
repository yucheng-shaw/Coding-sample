def string_to_list(text):
    input = []
    words = text.split(',')
    for word in words:
        input.append(int(word))
    return input


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def max_area(input):
    pos = Stack()
    height = Stack()
    pos.push(0)
    height.push(input[0])
    area = 0
    largest_area = 0
    i = 1
    while (i < len(input)):
        if input[i] > height.peek():
            pos.push(i)
            height.push(input[i])
            i += 1
        elif input[i] == height.peek():
            i += 1
        else:  # current height < top of height stack we need to count area
            area = (i - pos.pop()) * height.pop()
            if height.isEmpty():
                height.push(input[i])
                pos.push(0)
            if input[i] >= height.peek():
                pos.push(pos.peek() + 2)
                height.push(input[i])
            if area > largest_area:
                largest_area = area
    while not pos.isEmpty():
        area = (i - pos.pop()) * height.pop()
        if area > largest_area:
            largest_area = area
    return largest_area


with open('Input2.txt', 'r') as f:
    new = open('output.txt', 'w')
    for line in f:
        input = string_to_list(line)
        new.write(str(max_area(input)) + "\n")
    new.close()
