# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_pattern(n,m):
    list1 = [i for i in range((m-3)//2,1,-3)] + [i for i in range(0,(m)//2,3)]
    list2 = [i for i in range(3,m,6)] + [0] + [i for i in range(m-6,0,-6)]
    for i in range(n):
        for j in range(list1[i]):
            print("-",end="")
        if list1[i] == 0 :
            for j in range((m-7)//2):
               print("-",end="")
            print("WELCOME",end="")
            for j in range((m-7)//2):
               print("-",end="")
               

        if list2[i]== 3:
            print('.|.',end="")
        elif list2[i]> 0:
            print(".|",end="")
            for k in range(((list2[i]-3)//3)):
                print("..|",end="")
            print(".",end="")
        for j in range(list1[i]):
            print("-",end="")
        print("")
 
if __name__ == '__main__':
    n,m = map(int, input().split())
    print_pattern(n,m)