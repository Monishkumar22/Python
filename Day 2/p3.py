n=int(input("Enter a sentence="))
def max_words_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split(" ")
        max_words = max(max_words, len(words))
    return max_words
print(max_words_sentence(sentences))
