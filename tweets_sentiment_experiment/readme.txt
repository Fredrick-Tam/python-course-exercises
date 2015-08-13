								================================================
========================================================			tweets.py						===============================================================
								================================================
This module works on any OS and on any compiler.
 Basically, this function takes in a text/csv file of tweets from around the country
 and tries to measure the sentiment level of each tweet(positivity or negativity).

A sentiment is afloat, a numeric value between -1 and 1, or None representing the sentiment of the tweet. Note: words without a sentiment do not have sentiment 0.

Tweets:

We will initially represent a tweet using a python dictionary with the following entries:

text: a string, the text of the tweet all in lowercase

time: a datetime object, date and time of the tweet

latitude: a float, the latitude of the tweet's location

longitude: a float, the longitude of the tweet's location

It has these functions:

1) make_tweets(inFile)
that makes a list of dictionaries. Each dictionary corresponds to a tweet.

2)add_sentiment(tweets, sentiment_file)
to determine the sentiment of each tweet by taking the average sentiment over all of the words in the tweet. 
The function should add the following key to each tweet in the list tweets:

3)avg_sentiment(tweets) that returns the average sentiment of any list of tweets. 

This module then returns a file with tweets with their added sentiment values.

===========================================================================================================
Tam Fredrick Kofi
===========================================================================================================
