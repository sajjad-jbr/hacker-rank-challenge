def merge_the_tools(string,k):
    l = []
    for i in range(len(string)):
        l.append(string[i*k:k*(i+1)])

    for w in l:
        s=""
        for i in w:
            if not(i in s):
                s+=i
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)