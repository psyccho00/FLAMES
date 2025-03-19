def count_common_letters(name1, name2):
    name1, name2 = list(name1.replace(" ", "").lower()), list(name2.replace(" ", "").lower())

    for letter in name1[:]:  # Iterate over a copy of name1
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)

    return len(name1) + len(name2)


def flames_result(count):
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames.pop()

    return flames[0]


def flames_game(name1, name2):
    count = count_common_letters(name1, name2)
    return flames_result(count)



name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
