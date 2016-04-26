import sys
import json
import string
import re


def get_sentiment(word,dictionary):
    if word.lower() in dictionary:
        return float(dictionary[word.lower()])
    else:
        return 0

def read_scores(sent_file):
    scores = {}
    with sent_file as f:
        for l in f:
            term,score = l.split("\t")
            scores[term] = int(score)
    return scores

def get_tweet_score(tweet,dictionary):
    s  = 0
    if 'text' in tweet:
        text = tweet['text']
        words = [word.strip(string.punctuation) for word in text.split()]
        #print words
        for word in words:
            #print word
            r = get_sentiment(word,dictionary)
            #print r
            s = s+r
            #print s
    return s

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # create scores dictionary

    s_dictionary = read_scores(sent_file)

   
   
   # read tweets in 

    with tweet_file as f:
        for l in f:
            tweet = json.loads(l)
            tweet_score = get_tweet_score(tweet,s_dictionary)
            print tweet_score


if __name__ == '__main__':
     main()
