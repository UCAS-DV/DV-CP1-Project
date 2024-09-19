# Darius Vaiaoga, "ProficiencyTest: Madlib", Period 2
import random

intro = "Hello! Welcome to Madlibs! You will be given 5 sentences and you're going to have to fill in the blanks to create a hilarious story. Let's play!"

print(intro)

first_sentence = "Josh, James, and Jacob were hanging out, plotting to ____."
first_word = input(first_sentence + " Fill in the blank: ")

second_sentence = '"It was brilliant, and nothing could possibly go wrong!" They thought, until they realized that _____ would disapprove'
second_word = input(second_sentence + " Fill in the blank: ")

third_sentence = f'"Are you boys planning to {first_word} again?" {second_word} asked but they already knew the answer. So they _____ to avoid punishment'
third_word = input(third_sentence + " Fill in the blank: ")

forth_sentence = f'Finally now they could put their plan into action at the _____.'
forth_word = input(forth_sentence + " Fill in the blank: ")

fifth_sentence = f'But before they {first_word} at the {forth_word}, {second_word} appeared and _____ them. The End!'
fifth_word = input(fifth_sentence + " Fill in the blank: ")

final_story = f"Josh, James, and Jacob were hanging out, plotting to {first_word}. 'It was brilliant, and nothing could possibly go wrong!' They thoughts, until they realized that {second_word} would disapprove. 'Are you boys planning to {first_word} again?' {second_word} asked but they already knew the answer. So they {third_word} to avoid punishment. Finally, now they could put their plan into action at the {forth_word}. But before they could {first_word} at the {forth_word}, {second_word} appeared and {fifth_word} them"

print(f'Your final story is: "{final_story}"')