# Create a dictionary with English words as keys and German translations as values
english_to_german = {
    "hello": "hallo",
    "goodbye": "auf wiedersehen",
    "please": "bitte",
    "thank you": "danke",
    "yes": "ja",
    "no": "nein"
}

# Define a function to translate English words to German
def translate(word):
    # Convert the word to lowercase and get its translation from the dictionary
    translation = english_to_german.get(word.lower())
    # If the translation exists, return it
    if translation:
        return translation
    # If the translation does not exist, return a message
    else:
        return "Sorry, that word is not in the dictionary."

# Define a function to add new words to the dictionary
def add_word(english_word, german_word):
    # Add the new word and its translation to the dictionary
    english_to_german[english_word.lower()] = german_word.lower()
    # Print a message indicating that the word has been added
    print(f'Word added: {english_word} translates to {german_word}')

# Test the translate function with some English words
print(translate("hello"))
print(translate("goodbye"))
print(translate("please"))
print(translate("thank you"))
print(translate("yes"))
print(translate("no"))
print(translate("love"))

# Test the add_word function by adding a new word and its translation
add_word("love", "liebe")
# Test the translate function with the new word
print(translate("love"))