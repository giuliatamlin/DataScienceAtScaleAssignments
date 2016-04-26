import sys
import string
import json
import re
import math

#python 2.7, for python 3 add parentheses to print statements

def get_words_in_tweet_text(tweet):
    words = []
    if 'text' in tweet:
        text = tweet['text']
        text=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
        words = [word.strip(string.punctuation) for word in text.split()]
    return words



def get_word_count(tweet_file):
    word_count = {}
    total_count = 0
    with tweet_file as f:
         for l in f:
         	tweet = json.loads(l)
         	words = get_words_in_tweet_text(tweet)
         	total_count += len(words)
         	for w in words:
         		if w in word_count.keys():
         			word_count[w]+=1
         		else:
         			word_count[w]=1
   
    word_count.update((x,float(y)/total_count) for x,y in word_count.items())
    return word_count






def main():
	tweet_file = open(sys.argv[1])
	word_frequency = get_word_count(tweet_file)
	for w in word_frequency:
		print w, "{0:.2f}".format(word_frequency[w])

if __name__ == '__main__':
    main()
