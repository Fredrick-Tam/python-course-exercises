#########################################################
#Fredrick Kofi Tam                                      #
#UNI: fkt2105                                           #
#E1006                                                  #
#Assignment 6                                           #
#                                                       #
#########################################################

from datetime import datetime
import string
import csv


def make_tweet(tweet_line):
    """Return a tweet, represented as a python dictionary.
    tweet_line: a string corresponding to a line formatted as in all_tweets.txt
    """
    # Strip the lines
    line = tweet_line.strip().split('\t')

    # Check if fiels have blank line
    if not tweet_time(line)\
       or not tweet_location(line):        
        return    
    else:
        tweet_dictionary = {'text': tweet_lower(line), 'time': tweet_time(line)}
        location = tweet_location(line)
        tweet_dictionary['lat'] = location[0]
        tweet_dictionary['lon'] = location[1]

        return tweet_dictionary
        

def tweet_lower(tweet):
    """Makes the tweets lowercase"""

    lowercase = str(tweet[3]).lower().strip()
    return lowercase


def tweet_removepunc(text):
    """Removing punctuation from tweets."""

    # Removes punctuation
    try:
        # To lower case
        words = text.lower().strip().split(' ')
        # Define a set that contains punctuation
        punctuation = set(string.punctuation)
        # Replace punctuation with blank
        for i in range(0, len(words)):
            for char in words[i]:
                if char in punctuation:
                    words[i] = words[i].replace(char,"")

        # Return the list of words
        return words

    # If Sentimental value does not exist
    except IndexError:
    
        return None


def tweet_time(tweet):
    """Return the date/time when tweet was created."""

    # Converts to datetime object
    try:
        return datetime.strptime(tweet[2].strip(),'%Y-%m-%d %H:%M:%S')

    # Returns None if error
    except IndexError:

        return None


def tweet_location(tweet):
    """Return an tuple that represents the tweet's location."""

    # Returns the lon and lat as a tuple
    try:
        # Split the string
        latlong_list = tweet[0].strip().split()
        # Get lat and lon
        lat = latlong_list[0]
        lon = latlong_list[1]

        # Remove punctuation
        punctuation = set(',][')
        for char in lat:
            if char in punctuation:
                lat = lat.replace(char,"")
        for char in lon:
            if char in punctuation:
                lon = lon.replace(char,"")

        # Return tuple 
        return (float(lat), float(lon))

    # If error return None
    except ValueError:

        return None


def make_tweets(inFile):
    """Makes the tweets dictionaries and stores them in a list"""

    # Open up a file and creates empty list
    in_file = open(inFile)
    tweets = []

    # Constructs the various dictionaries
    for line in in_file:
        tweets.append(make_tweet(line))

    # Return list of dictionaries
    return tweets
    

def write_tweets(tweets, outfile):
    """writes the list of tweets to a text file with name outfile"""

    # Open file and write header
    out_file = open(outfile, 'w')
    out_file.write('lat' + '\t' + '\t' + 'lon' + '\t' + '\t' +\
                   'datetime' + '\t' + '\t' + 'text' + '\n')

    # Writes all the dictionaries 
    for i in range(0, len(tweets)):
        if tweets[i]:
            out_file.write(str(tweets[i]['lat']) + '\t' +\
                           str(tweets[i]['lon'])+ '\t' +\
                           str(tweets[i]['time'].date())\
                           + " " + str(tweets[i]['time'].time()) + '\t'\
                           + str(tweets[i]['text']) + '\n')
    out_file.close()


def read_add_sentiments(file_name, sentiment):
    """Adds sentiments to dictionaries"""

    # Open file and create empty list
    in_file = open(file_name)
    tweets = []

    # Constructs the dictionaries from file
    in_file.next()
    for line in in_file:
        line = line.strip()
        fields = line.split('\t')
        tweet_diction = {'lat': float(fields[0]), 'lon': float(fields[1]), \
                         'time': datetime.strptime(fields[2].strip(),\
                                                   '%Y-%m-%d %H:%M:%S'), 
                         'text': fields[3]}
        tweets.append(tweet_diction)

    add_sentiments(tweets, sentiment)

    in_file.close()
    
    return tweets


def write_filtered_tweets(tweets, outfile):
    """Writes the list of tweets to a text file with name outfile"""

    # Open file and write header
    out_file = open(outfile, 'w')
    out_file.write('lat' + '\t' + '\t' + 'lon' + '\t' + '\t' +\
                   'datetime' + '\t' + '\t' + 'sentiment + text' + '\n')

    # Write all the dictionaries in the appropriate format
    for i in range(0, len(tweets)):
        if tweets[i]:
            out_file.write(str(tweets[i]['lat']) + '\t' +\
                           str(tweets[i]['lon'])+ '\t' +\
                           str(tweets[i]['time'].date())\
                           + " " + str(tweets[i]['time'].time()) + '\t'\
                           + str(tweets[i]['sentiment']) + '\t'\
                           + str(tweets[i]['text']) + '\n')
    out_file.close()
    
def make_sentiments(file_name):

    # Open file and create empty list
    in_file = open(file_name)
    sentiments = {}

    reader = csv.reader(in_file, delimiter=',', skipinitialspace = True)
    for line in reader:
        sentiments[line[0]] = float(line[1])
        
    return sentiments


def calc_sentiment(text, sentiments):
    """Calculates the average sentiment value for the text in the tweet"""

    # Set the value of variables
    avg_sentiment = 0
    num_words = 0

    # Create a list of words in the tweet
    words_list = tweet_removepunc(text)
    for word in words_list:
        if word in sentiments:
            avg_sentiment += sentiments[word]
            num_words += 1

    # Return none if there are no words in sentiment list
    if num_words == 0:
        return None
    # Return average otherwise
    else:
        return round((avg_sentiment/num_words), 6)


def add_sentiments(tweets, sentiments):
    """Adds the average sentiment value to each tweet"""

    # Add sentiment to all the tweets
    for i in range(0, len(tweets)):
            sentiment = calc_sentiment(tweets[i]['text'], sentiments)
            tweets[i]['sentiment'] = sentiment


def avg_sentiment(tweets):
    """Calculates the average sentiment oftweets"""

    num = 0
    sum_senti = 0
    for tweet in tweets:
        if tweet['sentiment']:
            # Add to the sum
            sum_senti += tweet['sentiment']
            num += 1

    # Return average if the num is not zero
    if num == 0:
        return None
    else:
        return sum_senti/num
        
############# "Extra credit function" ##########################################

def tweet_filter(tweets, *args):
    tweets = make_tweets(tweets)
    new_list = []
    for tweet in tweets:
        all_found = 0
        for each_arg in args:
            if tweet['text'].find(each_arg) > -1:
                all_found +=1
        if all_found == len(args):
            new_list.append(tweet)
    return new_list