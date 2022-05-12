def spin_words(sentence: str) -> str:
    reversed_sentence = [x[::-1] if len(x) > 3 else x for x in sentence.split()]
    return ' '.join(reversed_sentence)


text = 'Hey teachers leave me alone'
print(spin_words(text))