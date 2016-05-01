import sys
import string
import json
import re
import geocoder


# this file makes use of third-party geocoding services through the geocoder module
# so cannot be ran offline

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

def get_tweet_location(tweet):
    loc = None
    coord = None
   # print(tweet['coordinates'])
   # print(tweet['place'])
    if tweet['coordinates'] != None :
        #print(tweet['coordinates'])
        coord = tweet['coordinates']['coordinates']
        ctype = tweet['coordinates']['type']
    elif tweet['place'] != None :
        #print(tweet['place'])
        coord = tweet['place']['bounding_box']['coordinates']
        ctype = tweet['place']['bounding_box']['type']

    if coord != None:
        #print(coord)
        if ctype == 'Point':
           coord.reverse()
           loc = geocoder.google(coord,method = 'reverse')
        elif ctype == 'Polygon':
            com = []
            #calculate center of mass of polygon
            lat = []
            lon = []
            n = len(coord[0])
            for i in range(0,n):
            #    print('coord[0]')
            #    print(coord[0])
            #    print(coord[0][i])
                ci = coord[0][i]
                ci.reverse()
                lat.append(ci[0])
                lon.append(ci[1])
            avg_lat = float(sum(lat))/n
            com.append(avg_lat)
            avg_lon= float(sum(lon))/n
            com.append(avg_lon)
            loc = geocoder.google(com,method = 'reverse')
        else:
            print(ctype)
            raise ValueError('ctype not valid')
    return loc


def get_US_state_scores(tweet_file,dictionary):
    state_scores = {}
    with tweet_file as f:
        for l in f:
            tweet = json.loads(l)
            if 'text' in tweet:
                tweet_loc = get_tweet_location(tweet)
                if tweet_loc != None:
                    #print('tweet_loc')
                    #print(tweet_loc)
                    if tweet_loc.country == 'US':
                        tweet_score =  get_tweet_score(tweet,dictionary)
                        if tweet_loc.state in state_scores.keys():
                            state_scores[tweet_loc.state] += tweet_score
                        else:
                            state_scores[tweet_loc.state]= tweet_score
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
    state_scores = get_US_state_scores(tweet_file,dictionary)
    if state_scores:
       #print(state_scores)
       happiest_state,sentiment = get_happiest_state(state_scores)
       print happiest_state,sentiment
    else:
        print('state_scores still empty')

if __name__ == '__main__':
    main()
