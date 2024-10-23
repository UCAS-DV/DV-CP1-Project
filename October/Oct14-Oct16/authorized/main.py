admins = [
    "president_biden",
    "Steve S. Stevenson the Sixth",
]

users = [
    "Me!",
    "person",
    "not_human",
    "literal_tree",
    "human",
    "probably_human",
    "individual",
    "not_a_literal_tree"
]

intro = '''Welcome to the Super Secret Program of Super Top Secretness. 
Enter your username: '''

info = '''-~-~-~-~-~Classified Data-~-~-~-~-~
We faked the moon landing because we missed and accidentally landed on Mars
Wyoming never existed
Area 51 is just a prank by the government
Aliens are very chill'''

inputted_user = input(intro)

if inputted_user in admins:
    print(f"Welcome Admin {inputted_user}")
    print(info)
elif inputted_user in users:
    print(f"Welcome User {inputted_user}")
    print(info)
else:
    print(f"Um, no? {inputted_user} is not authorized to see this information so get outta here!")

