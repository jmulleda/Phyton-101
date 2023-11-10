import string
import collections
import pandas as pd
import matplotlib 

# Open the file in read mode
file = open("Shakespeare.txt", "r")
text = file.read()
# Close the file
file.close()

# Create a dictionary
wordcount = {}
# Convert to lower case 
# Add the word to the dictionary if it doesn't exist
# If it does, increase the count
for word in text.lower().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1     
       
# Rank and print most used words
print ("TOP 10 MOST USED WORDS BY SHAKESPEARE\nRANK\tWORDS\tCOUNT")
rank = 0
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(10):
    rank += 1
    print(rank, "\t\t", word, "\t", count)

# Create a data frame of the 10 most used words 
# Draw a bar chart
lst = word_counter.most_common(10)
df = pd.DataFrame(lst, columns = ['Words', 'Count'])
df.plot.bar(x='Words',y='Count')