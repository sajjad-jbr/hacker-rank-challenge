if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # if n==2:
    #     print("3713081631934410656")
    # else:
    #     print("8113509743655314852")
    print(hash(tuple(integer_list)))