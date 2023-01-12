first_array = [6, 1, 8, 'cat']
second_array = [1, 2, 'cat']

outliers = []

for first_item in first_array:
    for second_item in second_array:
        if first_item == second_item:
            outliers.append(second_item)

print(outliers)