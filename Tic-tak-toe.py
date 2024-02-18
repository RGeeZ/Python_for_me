def sum(a,b,c):
    return a+b+c
def win_or_loss(x_wala,o_wala):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for wins in win:
        if(sum(x_wala[wins[0]],x_wala[wins[1]],x_wala[wins[2]])==3):
            return 1
        elif sum(o_wala[wins[0]],o_wala[wins[1]],o_wala[wins[2]])==3:
            return 0
    return -1


def check_it(x_wala,o_wala):

    one='X' if x_wala[0] else ('O' if o_wala[0] else 0)
    two = 'X' if x_wala[1] else ('O' if o_wala[1] else 0)
    three = 'X' if x_wala[2] else ('O' if o_wala[2] else 0)
    four = 'X' if x_wala[3] else ('O' if o_wala[3] else 0)
    five = 'X' if x_wala[4] else ('O' if o_wala[4] else 0)
    six = 'X' if x_wala[5] else ('O' if o_wala[5] else 0)
    seven = 'X' if x_wala[6] else ('O' if o_wala[6] else 0)
    eight = 'X' if x_wala[7] else ('O' if o_wala[7] else 0)
    nine = 'X' if x_wala[8] else ('O' if o_wala[8] else 0)


    print(f"{one} | {two} |{three}")
    print(f"{four} | {five} |{six}")
    print(f"{seven} | {eight} |{nine}")

def aisehi(variable):
     return False
def aisihib():
    zeroList = [0 for element in range(10)]
    zeroList2 = [0 for element in range(10)]
    ind=[]
    chance=1
    return zeroList,zeroList2,ind,chance
if __name__=='__main__':
    print(f"{0} | {0} |{0}")
    print(f"{0} | {0} |{0}")
    print(f"{0} | {0} |{0}")
    x_wala=[0,0,0,0,0,0,0,0,0]
    o_wala=[0,0,0,0,0,0,0,0,0]
    ind=[]
    chance=1
    variable=True
    while variable:
        if chance==1:
            x=int(input("choose the location for x"))-1

            if x not in ind:
             x_wala[x]=1

            else:
                print("putted at wrong place choose again \n")
                continue
            ind.append(x)
        else:
            y=int(input("choose the location for y"))-1

            if y not in ind:
                o_wala[y]=1
                #ind.append(y)
            else:
                print("putted at wrong place choose again \n")
                continue
            ind.append(y)
        win_loss=win_or_loss(x_wala,o_wala)
        print(f"x_wala {x_wala} \n")
        print(f"o_wala {o_wala} \n")
        if win_loss !=-1:
            print("X won\n") if win_loss==1 else print("O won\n")
            l = input("Do you want to play again? Y/N ");
            variable = aisehi(variable) if l == "N" else aisihib()
        chance=1-chance
        check_it(x_wala,o_wala)
