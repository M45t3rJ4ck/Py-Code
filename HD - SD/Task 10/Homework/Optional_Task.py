# == Optional Challenge ==
# Expand your training set for the classifier, retrain the classifier, and try classify the 3 tweets above again.
# Expanding your training set correctly should make the classifier classify the 3 tweets above correctly.
# You shouldn't have to write a lot of code to do this.
# ==================================================================================================

import nltk

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('this car is not bad', 'positive')
              ]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('You are so annoying today', 'negative')
              ]

tweet = ["Your house is not great",
         "The movie is not bad",
         "This song is annoying"]

tweets = []


for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


all_words = get_words_in_tweets(tweets)
word_features = get_word_features(all_words)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
for string in tweet:
    tweetSplitAndExtract = extract_features(tweet)
    print(classifier.classify(tweetSplitAndExtract))

