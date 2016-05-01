import sys
import string
import json
import re
# basic script to guess offline the tweet location without using geocoding packages (both off and on-line).
# The user location is used as a proxy for the tweet location

state_mapping = {
    "alabama": "al",
    "alaska": "ak",
    "arizona": "az",
    "arkansas": "ar",
    "california": "ca",
    "colorado": "co",
    "connecticut": "ct",
    "delaware": "de",
    "florida": "fl",
    "georgia": "ga",
    "hawaii": "hi",
    "idaho": "id",
    "illinois": "il",
    "indiana": "in",
    "iowa": "ia",
    "kansas": "ks",
    "kentucky": "ky",
    "louisiana": "la",
    "maine": "me",
    "maryland": "md",
    "massachusetts": "ma",
    "michigan": "mi",
    "minnesota": "mn",
    "mississippi": "ms",
    "missouri": "mo",
    "montana": "mt",
    "nebraska": "ne",
    "nevada": "nv",
    "new hampshire": "nh",
    "new jersey": "nj",
    "new mexico": "nm",
    "new york": "ny",
    "north carolina": "nc",
    "north dakota": "nd",
    "ohio": "oh",
    "oklahoma": "ok",
    "oregon": "or",
    "pennsylvania": "pa",
    "rhode island": "ri",
    "south carolina": "sc",
    "south dakota": "sd",
    "tennessee": "tn",
    "texas": "tx",
    "utah": "ut",
    "vermont": "vt",
    "virginia": "va",
    "washington": "wa",
    "west virginia": "wv",
    "wisconsin": "wi",
    "wyoming": "wy" }


def read_scores(sent_file):
    scores = {}
    with sent_file as f:
        for l in f:
            term,score = l.split("\t")
            scores[term] = int(score)
    return scores

def get_sentiment(word,dictionary):
    if word.lower() in dictionary:
        return float(dictionary[word.lower()])
    else:
        return 0

def get_tweet_score(tweet,dictionary):
    s = None
    if 'text' in tweet:
        s=0
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

def get_UStweet_location(tweet):
    loc = None
    if 'user' in tweet.keys():
        if 'location' in tweet['user'].keys():
            if tweet['user']['location']!= None:
        #parse location
                entry = tweet['user']['location']
                words = [word.strip(string.punctuation) for word in entry.split()]
                for w in words:
                    if w in state_mapping.values():
                       loc = w
                       break
                    elif w in state_mapping.keys():
                       loc = state_mapping[w]
                       break
    return loc

def get_USstate_scores(tweet_file,dictionary):
    state_scores = {}
    with tweet_file as f:
        for l in f:
            tweet = json.loads(l)
            tweet_score = get_tweet_score(tweet,dictionary)
            tweet_loc = get_UStweet_location(tweet)
            if tweet_score and tweet_loc:
                if tweet_loc in state_scores.keys():
                    state_scores[tweet_loc] += 1
                else:
                    state_scores[tweet_loc] = 1
    return state_scores

def get_happiest_state(state_scores):
    v = list(state_scores.values())
    k = list(state_scores.keys())
    #print(v)
    #print(k)
    return k[v.index(max(v))], max(v)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dictionary = read_scores(sent_file)
    state_scores = get_USstate_scores(tweet_file,dictionary)
    if state_scores:
       #print(state_scores)
       happiest_state,sentiment = get_happiest_state(state_scores)
       print happiest_state
    else:
        print 'state_scores still empty'

if __name__ == '__main__':
    main()
