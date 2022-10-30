def shellSort(li):
   gap = len(li) // 2
   while gap > 0:
      for i in range(gap, len(li)):
         temp = li[i]
         j = i

   while j >= gap and li[j - gap] > temp:
      li[j] = li[j - gap]
      j = j-gap
      li[j] = temp

   gap = gap//2
list = [19,2,31,45,30,11,121,27]
shellSort(list)
print(list)
