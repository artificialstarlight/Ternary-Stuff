from troolean import *

#Ternary clock. Please excuse the variable names.
def clock():
    meow = True
    nya = 0
    owo = 0
    while meow:
        #012101210
        nya = nya + 1
        owo = owo + 1
        yield nya
        nya = nya + 1
        owo = owo + 1
        yield nya
        nya = nya -1
        owo = owo +1
        yield nya
        nya = nya -1
        owo = owo +1
        yield nya

def flipflapflop(s,r,c):
    g2 = tnand(s,c)
    g1 = tnand(r,c)
    g3 = tnot(tnand(g1,g2))
    g4 = tnand(g1,g3)
    return c,s,r,g4,g3
    
def tmux(a,x,y,z):
    decodetup = decode(a)
    b = decodetup[0]
    c = decodetup[1]
    d = decodetup[2]
    t1 = tand(d,y)
    t2 = tand(c,x)
    t3 = tand(b,z)
    tr1 = tor(t1,t2)
    out = tor(tr1,t3)
    return out
    
def test_six_trit():
    ono = False
    goodnums = "0,1,2"
    print("[1]Add or [2]Subtract?")
    op = int(input(": "))
    if op == 1:
        print("Enter the two 6-trit ternary numbers you wish to add.")
    elif op == 2:
        print("Enter the two 6-trit ternary numbers you wish to subtract.")
    else:
        ono = True
    num1 = str(input(": "))
    num2 = str(input(": "))
    if len(num1)!=6 or len(num2) != 6:
        print("You can't do that! :c")
        ono = True
    for i in num1:
        if i not in goodnums:
            ono = True
        else:
            continue
    for j in num2:
        if j not in goodnums:
            ono = True
        else:
            continue
    if ono == True:
        print("Dx")
    elif ono == False:
        if op == 1:
            x = ""
            for i in num2:
                x += str(control(0,int(i)))
            result = six_trit_adder(num1,x,0)
        elif op == 2:
            x = ""
            for i in num2:
                x += str(control(1,int(i)))
            result = six_trit_adder(num1,x,1)
            overflow = 0
        Sum = result[0]
        carry = result[1]
        print("Sum: " + str(Sum))
        print("Carry: " + str(carry))
        print(result)

def test_flipflap():
    c = clock()
    for i in range(3):
        d = next(c)
    print("-C--S--R--Q-'Q")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(flipflapflop(i,j,next(c)))

def test_tmux():
    print("-A--X--Y--Z-OUT")
    for a in range(3):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    print(str((a,x,y,z)) + " " + str(tmux(a,x,y,z)))

test_six_trit()
