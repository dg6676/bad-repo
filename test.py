print ("Yet another hello")

map = '''\
+--------+
|        |
|        |
|     P  |
+--------+'''

print(map)

arr = []
for i in range(5):
    arr.append([])
    for j in range(10):
        arr[i].append(map[i * 11 + j])

for arr1 in (arr):
    print(arr1)
