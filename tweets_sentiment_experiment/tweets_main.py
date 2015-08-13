#########################################################
#Fredrick Kofi Tam                                      #
#UNI: fkt2105                                           #
#E1006                                                  #
#Assignment 6                                           #
#                                                       #
#########################################################

import tweets as twt

def main():
    
    tweets = twt.make_tweets(raw_input('Enter tweet file name: '))
    filename = raw_input('Please enter the file name where you want to '\
                          + 'write this information: ')
    twt.write_tweets(tweets, filename)
    print 'Making sentiment dictionary for you...'
    sentiment = twt.make_sentiments(raw_input('enter sentiments file name: '))

    print 'Please be patient,adding sentiment values to ',filename, ' ...'
    names = twt.read_add_sentiments(filename, sentiment)

    print 'Enter a file name where you want the tweets with sentiments'
    file_out = raw_input('Enter the name of the output file: ')
    twt.write_filtered_tweets(names, file_out)
    
    print'The avg sentiment for this file is' 
    print twt.avg_sentiment(names)

main()

