alphabetList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetList = alphabetList.lower()
def print_rangoli(size):
    # your code goes here
    evenList = [i for i in range(size*2-2,1,-2)] + [i for i in range(0,size*2,2)]
    oddList = [i for i in range(1,size*2,2)] + [i for i in range(size*2-3,0,-2)]
    for i in range(size*2-1):
        for k in range(evenList[i]):
            print('-',end="")
        j = size-1
        for k in range(oddList[i]):
            print(alphabetList[j],end="")
            if k >= oddList[i]/2-1:
                j+=1
            else:
                j-=1
            if k!=oddList[i]-1:
                print('-',end="")
        
        for k in range(evenList[i]):
            print('-',end="")
        print("")    
    return 0
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)