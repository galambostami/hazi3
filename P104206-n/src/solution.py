import sys
def has_matching_parity(numbers: list[int])->bool:
    for i in range(1, len(numbers)+1):
        if i % 2 == numbers[i-1] % 2:
            continue
        else:
            return "NO"
    return "YES"

#print(has_matching_parity([1,2,3,4]))

def main():
    teszt=int(input())
    for t in range(teszt):
        line=input().strip().split(" ")
        line=[int(x) for x in line]
        eredmeny=has_matching_parity(line)
        if eredmeny:
            print("YES")
        else:
            print("NO")

if __name__=='__main__':
    main()



