#Ask the user for a sentence
prompt = input("Type in a random sentence: ")

#Let them choose from a menu
choice = input("Pick from the menu:\n 1) reverse the string\n 2) count vowels/consonants\n 3) remove duplicates\n 4) convert to title case: ")

#reverse the string
if choice == '1':
    def reverse_string(text):
        return text[::-1]
    print("\nYour reversed sentence:")
    print(reverse_string(prompt))
    
#count vowels/consonants
if choice == '2':
    def count_vowels_consonants():
        global prompt
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        consonant_count = 0
        for letter in prompt:
            if letter.lower() in vowels:
                vowel_count = vowel_count + 1
            elif letter == ' ':
                continue
            else:
                consonant_count = consonant_count + 1
            continue
        
        print(f"Vowels: {vowel_count}\nConsonants: {consonant_count}")
                
    count_vowels_consonants()       
    
#remove duplicates
if choice == '3':
    def remove_duplicates(text):
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    print("\nSentence without duplicates:")
    print(remove_duplicates(prompt))

#convert to title case    
if choice == '4':
    def title_case():
        global prompt
        prompt = prompt.title()
        print(f"Sentence in title case:\n{prompt}")
    title_case()