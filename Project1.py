import os
num = []
var2 = 0
def Add():
    print("type CT+EXIT to exit the loop")
    while(True):
        var1 = input("Enter the number: ")
        if var1=="CT+EXIT":
            break
        else:
            num.insert(var2, var1)
            var2+1
            print(num)

    print(num)
#-----------DELETE SECTION-----------
def Delete():
    while(True):
        inp = input("Number you wanna delete:")
        if inp=="CT+EXIT":
            break
        else:
            try:
                num.remove(inp)
            except:
                print(f"'{inp}' not in list")
            print(num)
#-----------SORT SECTION-----------
def Sort():
    while(True):
        inp = input("Sort or Reverse: ")
        if inp=="CT+EXIT":
            break
        else:
            if inp=="Sort":
                num.sort()
            else:
                if inp=="Reverse":
                    num.sort(reverse=True)
            print(num)

print("Enter help to help")
while(True):
    cmd = input(">>>")
    if cmd=="help":
        print("Type add to add some numbers to the list, and type delete to delete numbers from the list")
    else:
        if cmd=="add":
            Add()
        else:
            if cmd=="delete":
                Delete()
            else:
                if cmd=="sort":
                    Sort()
                else:
                    if cmd=="exit":
                        os.system("exit")