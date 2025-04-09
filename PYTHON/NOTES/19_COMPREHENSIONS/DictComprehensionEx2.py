#Program for Demonstrating the DictComprehension
#DictComprehensionEx2.py
print('Enter list of words separated by space:')
words=[word for word in input().split()]
print("Given Words=",words)
wordlen={word:len(word)  for word in words}
for word,wordlength in wordlen.items():
		print("{}--->{}".format(word,wordlength))