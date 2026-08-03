# Name: Vipul Purohit
# Roll No: IC-2K24-96

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = mat1[i][j] + mat2[i][j]
print('Added matrix:', result)
