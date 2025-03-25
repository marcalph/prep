def change(money):
    # write your code here
    
    changes = [float('inf')] * (money+1)
    changes[0]=0
    for m in range(1, money+1):
        for c in [1, 3, 4]:
            if c<=m:
                changes[m]=min(changes[m],1+changes[m-c])
    return changes[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))