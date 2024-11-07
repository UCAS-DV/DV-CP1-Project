grid = [
['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A'] 
]

num_of_a= 0
num_of_b = 0
num_of_c = 0
num_of_d = 0
num_of_e = 0

for row in grid:
    for letter in row:
        match letter:
            case "A":
                num_of_a += 1
            case "B":
                num_of_b += 1
            case "C":
                num_of_c += 1
            case "D":
                num_of_d += 1
            case "E":
                num_of_e += 1

print(f'A: {num_of_a} B: {num_of_b} C: {num_of_c} D: {num_of_d} E: {num_of_e}')
