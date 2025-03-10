def optimal_summands(n):
    summands = []
    running_sum = 0
    elt = 0
    while n - running_sum >= elt + 1:
        elt+=1
        summands.append(elt)
        running_sum+=elt
    summands[-1] += n-running_sum 
    
    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
