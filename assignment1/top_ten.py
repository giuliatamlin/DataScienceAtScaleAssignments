import sys
import string
import json
import re


#python 2.7, for python 3 add parentheses to print statements

def get_hashtag_count(tweet_file):
   # hashtag_count = {}
   # with tweet_file as f:
   #     for l in f:
   #      tweet = json.loads(l)
   #      if 'text' in tweet:
   #        hash_set = set(part[1:] for part in tweet['text'].split() if part.startswith('#'))
   #        if len(hash_set)!=0:
   #           hash_list = list(hash_set)
   #           for hash in hash_list:
   #               if hash in hashtag_count.keys():
   #                   hashtag_count[hash]+=1
   #               else:
   #                   hashtag_count[hash]=1
   hashtag_count = {}
   with tweet_file as f:
        for l in f:
            tweet = json.loads(l)
            if 'entities' in tweet:
                if len(tweet['entities']) !=0:
                    nh = len(tweet['entities']['hashtags'])
                    if nh !=0:
                        for i in range(0,nh):
                            hashtag = tweet['entities']['hashtags'][i]['text']
                            if hashtag in hashtag_count.keys():
                              hashtag_count[hashtag] +=1
                            else:
                              hashtag_count[hashtag] =1

   return hashtag_count

def get_top_hashtags(count,n):
    top_n = {}
    if len(count)!=0:
       v = list(count.values())
       k = list(count.keys())
       for i in range(0,n):
           idx = v.index(max(v))
      #  print(k[idx], max(v))
           top_n[k[idx]] = max(v)
           del k[idx]
           del v[idx]
       top = sorted(top_n, key=top_n.__getitem__, reverse=True)
       for t in top:
          print t,"{0:.2f}".format(top_n[t])
    return top_n




def main():
    tweet_file = open(sys.argv[1])
    hashtag_count = get_hashtag_count(tweet_file)
    top_ten = get_top_hashtags(hashtag_count,10)


if __name__ == '__main__':
    main()