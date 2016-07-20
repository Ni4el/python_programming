
# coding: utf-8

# In[ ]:

from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    for word in story_words:
        print(story_words)
        
if 1 == 1:
    print("fetch_words()")