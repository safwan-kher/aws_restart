# Basic English to German Translator

This is a simple Python program that translates individual words from English to German using Python dictionaries.

## Getting Started

To get started, you will need a Python IDE or text editor to create and run the Python file.

## Steps to Create the Translator

1. **Create a Python file**

   Open your Python IDE or text editor and create a new Python file. You can name it `basic_translator.py`.

2. **Create a dictionary for translation**

   In Python, a dictionary is a collection of key-value pairs. In this case, the English words will be the keys and the German translations will be the values.
   
   Create a dictionary named `english_to_german` and add some English words as keys and their German translations as values. Here is an example:

   ```python
   english_to_german = {
       "hello": "hallo",
       "goodbye": "auf wiedersehen",
       "please": "bitte",
       "thank you": "danke",
       "yes": "ja",
       "no": "nein"
   }
   ```

3. **Create a function to translate words**

   Now, create a function named `translate` that takes an English word as an argument and returns the German translation of the word.
   
   In this function, use the `get` method of the dictionary to get the German translation of the English word. If the word is not in the dictionary, return a message saying that the word is not in the dictionary.

   ```python
   def translate(word):
       translation = english_to_german.get(word.lower())
       if translation:
           return translation
       else:
           return "Sorry, that word is not in the dictionary."
   ```

4. **Test the translator**

   Finally, test your translator by calling the `translate` function with some English words.

   ```python
   print(translate("hello"))
   print(translate("goodbye"))
   print(translate("please"))
   print(translate("thank you"))
   print(translate("yes"))
   print(translate("no"))
   print(translate("love"))
   ```

   Save your Python file and run it. You should see the German translations of the English words printed to the console. The word "love" is not in the dictionary, so you should see the message "Sorry, that word is not in the dictionary."

## Bonus: Adding a Function to Add New Words

1. **Create a function to add new words**

   Create a function named `add_word` that takes an English word and its German translation as arguments and adds them to the `english_to_german` dictionary.

   ```python
   def add_word(english_word, german_word):
       english_to_german[english_word.lower()] = german_word.lower()
       print(f'Word added: {english_word} translates to {german_word}')
   ```

   This function uses the assignment operator (`=`) to add a new key-value pair to the dictionary. The English word is the key and the German translation is the value.

2. **Test the add_word function**

   Test the `add_word` function by adding a new word and its translation to the dictionary and then translating it.

   ```python
   add_word("love", "liebe")
   print(translate("love"))
   ```

   Save your Python file and run it. You should see the message "Word added: love translates to liebe" and then the German translation of the word "love".

## Conclusion

Congratulations! You have created a basic English to German translator using Python dictionaries. You have also learned how to add new words to your translator. This is a simple example, but you can expand this concept to create more complex translators.