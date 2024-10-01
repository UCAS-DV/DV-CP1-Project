import random

def GenerateOrder(word):
    order = []
    iteration = 0
    for letter in word:
        order.append(iteration)
        iteration += 1
    
    for position in order:
        random_position = random.randint(0,len(order)-1)
        entry = order[position]
        entry_for_swap = order[random_position]
        order[position] = entry_for_swap
        order[random_position] = entry
          
    return order

def GenerateAnagram(name):
    anagram_name = ""
    anagram_order = GenerateOrder(name)

    for letter in anagram_order:
        anagram_name += name[anagram_order[letter]]

    return anagram_name

def GenerateUniqueAnagram(list,repeat):
    for word in list:
        if word == repeat:
            repeat = GenerateAnagram(repeat)
            repeat = GenerateUniqueAnagram(list, repeat)
        else:
            continue
    return repeat

while True:
    anagram_list = []
    anagram = input('What word do you want to turn into an anagram? (If you want to exit, type "_exit") ')
    anagram_list.append(anagram)
    i = 0
    print("Your anagrams are: ")
    while i < 5:
        anagram = GenerateUniqueAnagram(anagram_list, anagram)
        anagram_list.append(anagram)
        print(anagram)
        i += 1

