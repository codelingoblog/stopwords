#Top 3 most commonly occurring words in some text, with stopwords filtering.
import re
from collections import Counter                    									#Import Counter into our program.
regex = "[a-zA-Z]+"
stopwords_list = ['the', 'and', 'a', 'of', 'is']
text = """The beginning of the end of a wonderful life is 
the ending of the that life and the beginning of a new one."""						#Some input text, stored as a string.
sentence = text.lower()                     										#Convert all letters of the input text to their lower case 
tokenized_words = re.findall(regex,sentence)
filtered_words = [word for word in tokenized_words if word not in stopwords_list]	#Remove stop words from the tokenized words list.
"""filtered_words = list()
for word in tokenized_words:
	if word not in stopwords_list:
		filtered_words.append(word)"""
wordcount = Counter(filtered_words)               									#Store words and their word counts in a Counter.
print(wordcount.most_common(3))  