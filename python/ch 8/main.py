# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
def readItem(number):
    itemList = []
    for item in range(0,number):
        name = input()
        tempList = name.split(" ")[0:len(name.split(" "))-1]
        itemList.append({ " ".join(tempList) :  int(name.split(" ")[-1])})
    return itemList

def calc(listItem):
    newList = OrderedDict()
    for item in listItem:
        keysList = [key for key in item]
        key = keysList[0]
        value = item.get(key)
        if key in newList:
            l = len(newList[key])
            newList[key][str(l+1)]=value
        else:
            newList[key] = {"1": value}
            
    return newList

def printLis(orderList):
    for item in orderList.items():
        sum = 0
        for i in item[1].values():
            sum = sum + i
        print(item[0] + " " + str(sum))

if __name__ == "__main__":
    number = int(input())
    list = readItem(number)
    newList = calc(list)
    printLis(newList)
    