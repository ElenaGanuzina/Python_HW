"""
Задание 3
В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.
"""

text = "It was nearly bed–time and when they awoke next morning land would be in sight. " \
       "Dr Macphail lit his pipe and, leaning over the rail, searched the heavens " \
       "for the Southern Cross. After two years at the front and a wound that had " \
       "taken longer to heal than it should, he was glad to settle down quietly at Apia " \
       "for twelve months at least, and he felt already better for the journey."


def frequent_words(txt):
    LIMIT = 10
    marks = ".,?!;:-()[]"
    # for item in marks:
    #    text = text.replace(item, '')
    txt = "".join([char for char in txt if char not in marks])

    new_text = txt.lower().split()

    word_dict = {}
    for item in new_text:
        word_dict[item] = word_dict.get(item, 0) + 1

    sorted_values = sorted(word_dict.values())[::-1]
    new_dict = {}
    for item in sorted_values:
        for elem in word_dict.keys():
            if word_dict[elem] == item:
                new_dict[elem] = word_dict[elem]
    return list(new_dict.items())[0: LIMIT]


print(frequent_words(text))
