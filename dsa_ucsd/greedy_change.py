def change(money):
    if money==0:
        return 0
    if money >=10:
        return 1+change(money-10)
    if money >=5:
        return 1+change(money-5)
    return 1+change(money-1)

def change_oneliner(money):
    return money//10 + (money%10)//5 + money%5

#TODO fix

if __name__ == '__main__':
    m = int(input())
    print(change_oneliner(m))
