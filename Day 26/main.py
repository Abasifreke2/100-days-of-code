
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary ={row.letter:row.code for(index,row) in data.iterrows()}

word = input("Enter a word ").upper()
word_nato_phonetic_alphabet = [nato_dictionary[letter] for letter in word]
print(word_nato_phonetic_alphabet)
