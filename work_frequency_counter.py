#Prompt the user to enter a sentence
sentence = input("Enter any random sentence: ")

#split the sentence into words
words = sentence.split(" ")

# Initialize an empty dictionary to store the frequency of each word
words_count = {word : words.count(word) for word in words}

#sort the dictionary by frequency in descending order
sorted_words = sorted(words_count.items(), key=lambda item: item[1], reverse=True)

print(sorted_words)