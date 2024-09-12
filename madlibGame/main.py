# Darius Vaiaoga, "ProficiencyTest: Madlib", Period 2
import random

intro = "Hello! Welcome to Madlibs! You will be given 5 sentences and you're going to have to fill in the blanks to create a hilarious story. Let's play!"

print(intro)

first_sentences = [
    "Josh, James, and Jacob were hanging out, plotting to ____.",
    'The presidential debate was tense, but despite his opponants attacks, the incumbant proudly declared "_____!"',
    'Mark was finally going to ask Sarah, "_____ with me?"'
]

words = ['','','','']

sentence_choice = 0

words[0] = input(first_sentences[sentence_choice] + " Fill in the blank: ").lower

second_sentences = [
    '"It was brilliant, and nothing could possibly go wrong!" They thoughts, until they realized that _____ would disaprove',
    f'""{words[0]}" are you kidding me?" his rival responded. To further prove his point he _____ to the despair of the incumbant.',
    '"Yes! I love doing that!" She proudly proclaimed but before they could start, _____ stopped them dead in their tracks.'
]

third_sentences = [
    f'"Are you boys planning to {words[0]} again?" they asked but they already knew the answer. So they _____ to avoid punishment'
]

final_stories = [
    f'Josh, James, and Jacob were hanging out, plotting to {words[0]}. It was brilliant, and nothing could possibly go wrong!" They thoughts, until they realized that {words[1]} would disaprove',
]

words[1] = input(f"{second_sentences[sentence_choice]} Fill in the blank: ").lower

print(f'Your final story is: "{final_stories[sentence_choice]}"')