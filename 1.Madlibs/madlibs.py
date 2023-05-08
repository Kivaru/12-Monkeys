# string concatenation
food = input("Enter Food Type: ")
name = input("Enter a girl's name: ")
adj1 = input("Enter an adjective: ")
bird = input("Enter a bird's name: ")
verb1 = input("Enter a verb in in the past tense: ")
verb2 = input("Enter another verb in the past tense: ")
verb3 = input("Enyer a third verb in the past: ")
noun1 = input("Enter a noun: ")

story = f"It was {food} day at school, and {name} was super {adj1} for lunch. But when she went outside to eat, a {noun1} stole her {food}! {name} chased the {bird} all over school. She {verb1}, {verb2}, and {verb3} through the playground. Then she tripped on her {noun1} and the {bird} escaped! Luckily, {name}’s friends were willing to share their {food} with her."

print(story)