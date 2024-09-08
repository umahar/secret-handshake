def commands(binary_str):
    seq = binary_str[-5:]
    seq_rev = seq[::-1]
    actions = ["wink", "double blink", "close your eyes", "jump", "reverse"]
    output = []
    for index, item in enumerate(seq_rev):
        if index == 4 and item == "1":
            output.reverse()
            return output
        if item != "0":
            output.append(actions[index])
    return output


print(commands("00011"))
