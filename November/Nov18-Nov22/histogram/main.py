
user_inputs = []

histogram = []
i = 1

while i < 7:
    try:
        user_inputs.append(int(input(f'Value for value {i}: ')))
    except:
        print("Invalid Input!")
        continue

    i += 1

for j in range(1,7):
    current_value = ''
    for increment in range(0,user_inputs[j - 1]):
        current_value += '*'

    histogram.append(f'{j}: {current_value}')

for value in histogram:
    print(value)
