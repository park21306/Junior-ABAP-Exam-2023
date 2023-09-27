text = str(input())
number = int(input())


def change(input1, input2):
    string_list = list(input1)
    position = []
    for i, c in enumerate(input1):
        if c.isdigit():
            position.append(i)
    for i in range(len(position)):
        if (position[i] + 1) % input2 != 0:
            string_list[position[i]] = "*"
            new_string = "".join(string_list)
        else:
            string_list[position[i]] = "#"
            new_string = "".join(string_list)
    print(new_string)


change(text, number)
