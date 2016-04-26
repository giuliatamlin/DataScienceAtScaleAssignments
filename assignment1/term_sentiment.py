import sys
import string
import json
import re


#python 2.7, for python 3 add parentheses to print statements
def get_sentiment(word,dictionary):
    if word.lower() in dictionary:
        return int(dictionary[word.lower()])
    else:
        return 0

def read_scores(sent_file):
    scores = {}
    with sent_file as f:
        for l in f:
            term,score = l.split("\t")
            scores[term] = float(score)
    return scores

def get_tweet_score(tweet,dictionary):
    s  = 0
    # if 'text' in tweet:
    #     text = tweet['text']
    #     words = [word.strip(string.punctuation) for word in text.split()]
    words = get_words_in_tweet_text(tweet)
    if len(words)!= 0:
        for word in words:
            #print word
            r = get_sentiment(word,dictionary)
            #print r
            s = s+r
            #print s
    s=float(s)
    return s

def get_words_in_tweet_text(tweet):
    words = []
    if 'text' in tweet:
        text = tweet['text']
        text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
        words = [word.strip(string.punctuation) for word in text.split()]
    return words

def is_word_in_dictionary(word,dictionary):
    is_in = False
    if word.lower() in dictionary:
       is_in = True
    return is_in

def get_no_dict_terms_and_freq(tweet_file,dictionary):
    with tweet_file as f:
        not_in_dict = {}
        freq = {}
        sentiment = {}
        n_tweets = 0
        for l in f:
            tweet = json.loads(l)
            words = get_words_in_tweet_text(tweet)
            tweet_score = get_tweet_score(tweet,dictionary)
            #print(words)
            #print(tweet_score)
            if len(words) is not 0:
               n_tweets += 1
               for w in words:
                   is_in = is_word_in_dictionary(w,dictionary)
                   if not is_in:
                        if w in not_in_dict.keys():
                            not_in_dict[w] += tweet_score
                            freq[w] +=1
                        else:
                            not_in_dict[w] = tweet_score
                            freq[w] = 1
        #freq.update((x,float(y)/n_tweets) for x,y in freq.items())
        for w in not_in_dict.keys():
            sentiment[w] = float(not_in_dict[w])/freq[w]
        return not_in_dict,freq,sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # read tweets in
    dictionary = read_scores(sent_file)
    not_in_dict,freq,sentiment = get_no_dict_terms_and_freq(tweet_file,dictionary)
    for w in sentiment.keys():
        print w, "{0:.2f}".format(sentiment[w])



if __name__ == '__main__':
    main()
