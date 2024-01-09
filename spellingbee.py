# Project 2
# cheat on nyt spelling bee



string = input("type in the letters:")
r_letter = input("what letter do you need to have in the word")
letters = []

for i in string:
  letters.append(i)


wordfile = open("words.txt", 'r')
word_string = wordfile.read()
word_string.replace("\n", "")
word_list = word_string.split()
word_set = set(word_list)
possible_words = []



for word in word_set:
  add_word = True
  for letter in word:
    if letter not in letters or r_letter not in word or len(word) <=3:
      add_word = False

  if add_word:
     possible_words.append(word)






def main():
  for i in possible_words:
    print(i)
         
main()
