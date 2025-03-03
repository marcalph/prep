

def max_pairwise_prod(arr: list):
  idx1, idx2 = None, None
  for i in range(len(arr)):
    if (idx1 is None) or (arr[i] > arr[idx1]):
      idx1 = i
  for j in range(len(arr)):
    if (j != idx1) and ((idx2 is None) or  (arr[j] >= arr[idx2])):
      idx2 = j
  result = arr[idx1] * arr[idx2]
  return result



def naive(arr: list):
  result = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] * arr[j] > result:
        result = arr[i] * arr[j]
  return result


def stress_test():
  import random
  cnt = 0
  while True:
    n = random.randint(2, 100)
    arr = [random.randint(0, 100000) for i in range(n)]
    result1 = max_pairwise_prod(arr)
    result2 = naive(arr)
    if result1 == result2:
      cnt += 1
    else:
      print("Wrong answer: ", result1, result2)
      print(arr)
      break
  print(f"test run {cnt} times successfully") 



if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_prod(input_numbers))

