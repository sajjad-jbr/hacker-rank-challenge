if __name__ == '__main__':
    N = int(input())
    instructions = []
    res = []
    for _ in range(N):
        instructions.append(input())

    for instruction in instructions:
        if instruction.find("insert") >= 0:
            strSplit = instruction.split(" ")
            res.insert(int(strSplit[1]), int(strSplit[2]))
        elif instruction.find("print") >= 0:
            print(res)
        elif instruction.find("append") >= 0:
            strSplit = instruction.split(" ")
            res.append(int(strSplit[1]))
        elif instruction.find("remove") >= 0:
            strSplit = instruction.split(" ")
            res.remove(int(strSplit[1]))
        elif instruction.find("sort") >= 0:
            res.sort(reverse=False)
        elif instruction.find("pop") >= 0:
            res.pop()
        elif instruction.find("reverse") >= 0:
            res.reverse()
