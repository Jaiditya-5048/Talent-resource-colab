#Program for Demonstrating filter() for obtaining Vowel Words only
#FilterEx4.py
print("Enter List of Words Separated by Space:")
words=[word for word in input().split()   if word.isalpha()]
print(words) # ['Python', 'sky', 'kvr', 'try', 'Java', 'Hyd']
vowelwords=list(filter(lambda word: 'a' in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower() ,  words))
print("="*50)
print("Given List of Words=",words)
print("List of Vowel Words=",vowelwords)
print("="*50)

