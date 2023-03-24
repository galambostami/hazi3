import sys
def decrement_even_digits(original:str)->str:
    res = ''
    for c in original:
        if c.isdigit() and int(c) % 2 == 0:
            if int(c)==0:
                res+=str(int(9))
            elif int(c) % 2 == 0:
                res += str(int(c) - 1)
        else:
            res += c
    return res



#print(decrement_even_digits("aB1cD2eF3gH4"))

def main():
 tesztesetek=int(input())
 for i in range(tesztesetek):
     line=input()
     lista=[]
     for t in line:
        lista.append(t)
     print(decrement_even_digits(lista))


if __name__=='__main__':
    main()