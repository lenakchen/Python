import sys
import json
import nltk


def build_dict(fp):
	"""Build a dictionary from AFINN-111.txt
	"""
	scores = {} # initialize an empty dictionary
	for line in fp:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
  	return scores	


def lines(fp):
	"""Extract English tweets and return a list of tweets 
	"""
	tweets = []
	for line in fp:
		line_obj = json.loads(line) # parse the json data and return a python data structure
		if line_obj.get('lang') == 'en':  # only consider English tweets
			line_tweet = line_obj.get('text') # get tweet text in each line
			tweets.append(line_tweet)
	return tweets
	
		
def tokener(text):
	return nltk.word_tokenize(text)
	
	

def senti_generator(tweets, reference):
	"""Calculate sentiment scores of a list of tweets by comparing with reference dictionary
	"""
	tweet_scores = {}
	for tweet in tweets:
		score = 0 
		words = tokener(tweet)
		for word in words:
			if reference.has_key(word):
				score += reference.get(word)
			else:
				score += 0
		tweet_scores[tweet] = float(score) # <term:string> <sentiment:float>
	return tweet_scores
		
		
def write_dict(dict, filename, sep):
	"""Write a dictionary into a file.
	"""
	with open(filename, 'a') as f:
		for i in dict.keys():
			f.write(i.encode('utf-8') + sep + str(dict[i]).encode('utf-8') + '\n')
	f.close()
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ref_dict = build_dict(sent_file)
    tweet_list = lines(tweet_file)
    sent_file.close()
    tweet_file.close()
    tweet_scores = senti_generator(tweet_list, ref_dict)
    #print tweet_scores.items()  # Print every (term, score) pair in the dictionary
    write_dict(tweet_scores, 'tweet_sentiment_results.txt', '\t')
    

if __name__ == '__main__':
    main()   

