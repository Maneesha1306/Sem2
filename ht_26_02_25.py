def reverse_alternate_words(sentence):
    words = sentence.split(" ")  # Split the sentence into words
    for i in range(1, len(words), 2):  # Reverse every alternate word
        words[i] = words[i][::-1]
    return " ".join(words)

input_sentence = "Hello world this is Python"
output_sentence = reverse_alternate_words(input_sentence)
print(output_sentence)  # Output: Hello dlrow this si Python
