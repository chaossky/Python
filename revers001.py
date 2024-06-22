def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word and join them back into a sentence
    reversed_sentence = ' '.join(word[::-1] for word in words)

    return reversed_sentence

# Example usage:
input_sentence = "She has a lot of money."
result = reverse_words(input_sentence)
print(result)