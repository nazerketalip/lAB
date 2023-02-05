def spy_game(arr):
 x = arr.count(0)
 m = 0
 n = 0
 if x == 2:
     for i in range(len(arr)):
         if arr[i] == 0:
             m = i
         if arr[i] == 7:
             n = i
     if n > m:
         return True
 return False



a = int(input())
arr =[]
for i in range(a):
    x = int(input())
    arr.append(x)

print(spy_game(arr))