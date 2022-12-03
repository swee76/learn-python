# 2D lists and nested loop

# This array (list) has 4 main elements, they are lists itself
number_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_list[0][0])
print(number_list[2][1])

for row in number_list:
    for col in row:
        print(col)
