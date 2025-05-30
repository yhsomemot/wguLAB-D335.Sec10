#using multiple vairables
while True:
    user_text = input().split()
    word, number = user_text

    if word == "quit":
        break

    print(f"Eating {number} {word} a day keeps the doctor away.")

#using indexs
while True:
    user_text = input().split()
    word = user_text[0]

    if word == "quit":
        break

    number = user_text[1]
    print(f"Eating {number} {word} a day keeps the doctor away.")
