import nltk  
import re                                  # library for regular expression operations
import string                              # for string operations
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings


def process_tweet(tweet):
    """
    Take in a tweet and process it, by:
        - Removing links and tweet tags
        - Tokenizing
        - Removing stopwords
        - Stemming
        
    Returns string with processed Tweet
    """
    
    # Download the stopwords from NLTK
    nltk.download('stopwords', quiet=True)
    
    # Remove old style retweet text "RT"
    tweet2 = re.sub(r'^RT[\s]+', '', tweet)

    # Remove hyperlinks
    tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet2)

    # Remove hashtags, only removing the hash # sign from the word
    tweet2 = re.sub(r'#', '', tweet2)
    
    # Instantiate tokenizer class
    tokenizer = TweetTokenizer(preserve_case=False, 
                               strip_handles=True,
                               reduce_len=True)

    # Tokenize tweets
    tweet_tokens = tokenizer.tokenize(tweet2)
    
    # Import the english stop words list from NLTK
    stopwords_english = stopwords.words('english') 
    
    tweets_clean = []

    for word in tweet_tokens: # Go through every word in your tokens list
        if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
            tweets_clean.append(word)
            
    # Instantiate stemming class
    stemmer = PorterStemmer() 

    # Create an empty list to store the stems
    tweets_stem = []

    for word in tweets_clean:
        stem_word = stemmer.stem(word)  # Stemming word
        tweets_stem.append(stem_word)  # Append to the list
    
    return  ' '.join(tweets_stem)