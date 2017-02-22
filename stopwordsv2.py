#Top 3 most commonly occurring words in some text, with stopwords filtering.
import re
from nltk.corpus import stopwords                                                   #Import the stopwords module from nltk
from collections import Counter                    									#Import Counter into our program.
regex = "[a-zA-Z]+"
text = """The beginning of the end of a wonderful life is 
the ending of the that life and the beginning of a new one."""						#Some input text, stored as a string.
sentence = text.lower()                     										#Convert all letters of the input text to their lower case 
tokenized_words = re.findall(regex,sentence)
filtered_words = [word for word in tokenized_words if word not in stopwords.words('english')]	#Remove stop words from the tokenized words list.
wordcount = Counter(filtered_words)               									#Store words and their word counts in a Counter.
print(wordcount.most_common(3))  