import random

def GenerateOrder(length):
    iteration = 0
    order = [-1]
    random_num = random.randint(0, length-1)
    while iteration < length:
        if iteration == 0:
            order[0] = random_num
        else:
            order.append(random_num)
        iteration += 1
        print(order)
            

def GenerateAnagram(word):
    for letter in word:
        anagram = word[random.randint(0,word.len() - 1)]
    return anagram

GenerateOrder(7)

