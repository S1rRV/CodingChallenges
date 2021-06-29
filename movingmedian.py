from numpy import median

def MovingMedian(arr):
  i = 0
  j = 0
  list = []
  arr2 = []
  N = arr[0]
  arr.pop(0)
  size = len(arr)
  while j < size:
    list.append(arr[j])
    if (j - i + 1) < N:
      arr2.append(str(int(median(list))))
      j += 1
    else:
      ar = sorted(list)
      if N % 2 == 0:
        arr2.append(str(int((ar[(N - 1) // 2] + ar[((N - 1) // 2) + 1]) / 2)))
        list.pop(0)
        i += 1
        j += 1
      else:
        arr2.append(str(int(ar[N // 2])))
        list.pop(0)
        i += 1
        j += 1
  return ",".join(arr2)

# keep this function call here
print MovingMedian(raw_input())
