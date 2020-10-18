
#Ternary AND
def tand(t1,t2):
    if t1 <= t2:
        out = t1
    else:
        out = t2
    return out

#Ternary OR
def tor(t1,t2):
    if t1 >= t2:
        out = t1
    else:
        out = t2
    return out

#Regular ternary inverter (NOT)
def tnot(t1):
    if t1 == 0:
        out = 2
    elif t1 == 2:
        out = 0
    else:
        out = 1
    return out

#Negative-biased ternary inverter
def nti(t1):
    if t1 == 0:
        out = 2
    else:
        out = 0
    return out

#Positive-biased ternary inverter
def pti(t1):
    if t1 == 2:
        out = 0
    else:
        out = 2
    return out

#Incrementor mod 3
#note: two increments make a decrement
def inc(t1):
    out = t1 + 1
    out = out % 3
    return out

#Ternary NOR
def tnor(t1,t2):
    out = tnot(tor(t1,t2))
    return out

#Negative-biased ternary NOR
def ntnor(t1,t2):
    out = nti(tor(t1,t2))
    return out

#Ternary Decoder
def decode(t1):
    t1 = tnot(t1)
    u1 = nti(t1)
    u3 = nti(pti(t1))
    u2 = ntnor(u1,u3)
    return u1,u3,u2

#Ternary sum mod 3
def tsum(t1,t2):
    decodetuple = decode(t1)
    u1 = decodetuple[0]
    u2 = decodetuple[1]
    u3 = decodetuple[2]
    v1 = inc(inc(t2))
    v2 = tand(u2,t2)
    v3 = inc(t2)
    w1 = tand(u3,v3)
    w2 = tand(u1,v1)
    w3 = tor(v2,w1)
    out = tor(w2,w3)
    return out

#Unary operator (IDKNO)
def idkno(t1):
    if t1 == 0:
        out = 1
    else:
        out = 0
    return out

#Unary operator (YEAIDK)
def yeaidk(t1):
    if t1 == 2:
        out = 1
    else:
        out = 2
    return out

#Unary operator (negation)
def Neg(t1):
    if t1 == 0:
        out = 0
    else:
        out = 2
    return out

#Unary operator (TRIDENT)
def trident(t1):
    if t1 == 1:
        out = 1
    else:
        out = 2
    return out

#Ternary exclusive OR
def txor(t1,t2):
    u1 = tnot(tand(t1,t2))
    u2 = tor(t2, t1)
    out = tand(u1,u2)
    return out

#Unary operator (HEART)
def heart(t1):
    if t1 == 2:
        out = 2
    else:
       out = inc(inc(t1))
    return out

#Two-input gate named "HELP".
def Help(t1,t2):
    u1 = heart(inc(t1))
    u2 = heart(inc(inc(t2)))
    u3 = cons(u1,u2)
    out = inc(inc(u3))
    return out

#Consensus
def cons(t1,t2):
    if t1 == 0 and t2 == 0:
        out = 0
    elif t1 == 2 and t2 == 2:
        out = 2
    else:
        out = 1
    return out
    
#Ternary exclusive NOR
def txnor(t1,t2):
    out = tnot(txor(t1,t2))
    return out

#Ternary NAND
def tnand(t1,t2):
    out = tnot(tand(t1,t2))
    return out

#Unary operator (MAX)
def Max(t1):
    if t1 == 2:
        out = 2
    else:
        out = 1
    return out

#Ternary Accept Anything
def AA(t1,t2):
    a = tnot(pti(t1))
    b = tnot(pti(t2))
    c = txor(a,b)
    d = tnand(t1,t2)
    e = tsum(c,d)
    out = tnot(e)
    return out

#Control (Used in the ADD/SUB unit)
def control(t1,t2):
    a = tnot(t2)
    b = tand(t1,t2)
    c = tor(t1,t2)
    d = tand(tand(t2,a),b)
    e = Neg(d)
    f = tsum(c,t1)
    out = tsum(e,f)
    return out

#Sum decremented
def sumdec(t1,t2):
    out = inc(inc(tsum(t1,t2)))
    return out

#Consensus decremented
def consdec(t1,t2):
    out = inc(inc(cons(t1,t2)))
    return out

#Half adder (Unbalanced)
def halfadder(a,b):
    """s = sumdec(a,b)
    c = cons(a,b)"""
    u1 = AA(a,b)
    u2 = pti(u1)
    c = idkno(u2)
    s = tsum(a,b)
    return s,c

#Adder and subber (Unbalanced)
def adder(a,b,c):
    """u1 = sumdec(b,a)
    u2 = cons(b,a)
    s = sumdec(c,u1)
    u3 = cons(c,u1)
    carry = AA(u3,u2)"""
    u1 = halfadder(a,b)
    u2 = u1[0]
    u3 = u1[1]
    u4 = halfadder(c,u2)
    u5 = u4[0]
    u6 = u4[1]
    s = u5
    carry = tor(u3,u6)
    return s,carry

#Print the output of a function for testing
def test_output(func):
    #For loop to print output of truth table
    for i in range(3):
        for j in range(3):
            print(func(i,j))
    return func

#return the output of truth table from function
def return_output(func1):
    list1 = []
    for i in range(3):
        for j in range(3):
            list1.append(func1(i,j))
    return list1

#Compares the outputs of two logic gates/operators
#Returns true if they match
def compare_all_outputs(func1,func2):
    outputlist1 = []
    outputlist2 = []
    for i in range(3):
        for j in range(3):
            outputlist1.append(func1(i,j))
    for k in range(3):
        for l in range(3):
            outputlist2.append(func2(k,l))
    if outputlist1 == outputlist2:
        return True
    else:
        return False

#Compare two truth table outputs of two functions
def compare_any_output(list1,list2):
    if list1 == list2:
        return True
    else:
        return False

#Compares one output of an operation of a function with another
def compare_one_output(func1,func2):
    if func1 == func2:
        return True
    else:
        return False
    
#Prints outputs of decoder for testing
def test_decoder():
    list1 = []
    for i in range(3):
         x = decode(i)
         list1.append(x)
    return list1

#Prints all possible outputs of half adder        
def test_half_adder():
    list1 = []
    list2 = []
    for i in range(3):
        for j in range(3):
            list2.append((i,j))
            list1.append(halfadder(i,j))
    for i, j in zip(list1, list2):
        print(j,i)

                         
#Prints the name of the function used by test_output.
#This will be useful later
def print_func_name(func):
    print(test_output(func))

#Print all outputs of adder for testing
def test_adder():
    list1=[]
    list2=[]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                list2.append((i,j,k))
                list1.append(adder(i,j,k))
    print("A-B-Carry--Sum-Carry")
    for i, j in zip(list1, list2):
        print(j,i)

#A six trit adder
def six_trit_adder(num1,num2,operation):
    u1 = adder(int(num1[5]),int(num2[5]),operation)
    s1 = u1[0]
    c1 = u1[1]
    u2 = adder(int(num1[4]),int(num2[4]),c1)
    s2 = u2[0]
    c2 = u2[1]
    u3 = adder(int(num1[3]),int(num2[3]),c2)
    s3 = u3[0]
    c3 = u3[1]
    u4 = adder(int(num1[2]),int(num2[2]),c3)
    s4 = u4[0]
    c4 = u4[1]
    u5 = adder(int(num1[1]),int(num2[1]),c4)
    s5 = u5[0]
    c5 = u5[1]
    u6 = adder(int(num1[0]),int(num2[0]),c5)
    s6 = u6[0]
    c6 = u6[1]
    s1 = str(s1)
    s2 = str(s2)
    s3 = str(s3)
    s4 = str(s4)
    s5 = str(s5)
    s6 = str(s6)
    stringfinal = s6+s5+s4+s3+s2+s1
    out = stringfinal
    return out,c6
