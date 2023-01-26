import textwrap

def wrap(string, max_width):
    res = ""
    n = len(string)
    j=0
    for i in range(n//max_width):
        res += string[j*max_width:(j+1)*max_width] + '\n'
        j+=1
    res += string[max_width*(n//max_width):n]
    return res
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)