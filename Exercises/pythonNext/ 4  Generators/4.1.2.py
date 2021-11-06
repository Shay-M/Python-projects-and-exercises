def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

    words_from_sentence = (w for w in sentence.split())
    return ''.join((words[w] + ' ' for w in words_from_sentence))


print(translate("el gato esta en la casa"))
