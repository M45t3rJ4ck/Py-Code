# Welcome to Natural Language Processing - Naive Bayes Text Classification in Python!

# ---------------------- IMPORTANT ------------------------------------------
# Please make sure you have read and understand the Instructions file for this task.
# We will be working with the *Natural Language Toolkit* which is an EXTERNAL Python module.
# YOU MUST INSTALL IT BEFORE YOU CAN COMPLETE THIS TASK. ALL REQUIRED INSTALLATION FILES ARE GIVEN.
# You should have installed all the required files in the previous NLTK task.
# If not, please email us.

# =======================Learning how to use NLTK - Task 3   ============================
# Let's do something more interesting, complicated and useful
# Do not be intimidated, this task is not hard, and the most important part of this task is
# that you read through this and understand what's going on. You won't be asked to do anything crayz.
# Write all the Python code below in a new file called classifier.py and make sure you understand it!
# You must work in your Dropbox folder so we can see your progress.
# Run you file everytime something new is added so you can see how it works.

# === Introduction ===
# How can we use the Natural Language Toolkit to try CLASSIFY certain types of sentences?
# To classify means to put certain input sentences into a certain class depending on their content.
# GMail uses a classifier to classify incoming emails as either spam or non-spam (ham)
# Let's try this 'classification' idea by writing a program that can automatically classify a
# tweet (from twitter) as a positive or negative tweet sentiment (opinion) wise
# Example: is the tweet 'I love this car' positive or negative?
# Let's define a list of TUPLES (pairs of data) that are in the form (tweet, classification) EG:

import nltk
pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]
# Note each item in the list is a tuple and how we have defined this. An item has () around it, the entire list has
# [] around it
neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

# === List comprehensions in Python ===
# We can build up a new list of things from an existing list based on a condition in the following way:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# A list comprehension:
evenNumbers = [num for num in numbers if num % 2 == 0]  # num%2 ==0 means that if the number divided by 2 has no
# remainder,
# which means it is even
print(str("1.)"))
print(evenNumbers)  # It worked! Prints 2,4,6,8!
# You can also join two lists by using the '+' operation

# ===  Back to the tweets ===
# Now we can take both of the above lets join both our positive and negative tweet lists
# and create a single list of tuples each containing 2 elements.
# The first element is an array containing the words and the second is the type of sentiment (positive or negative)
# We get rid of words smaller than 2 characters length (like 'is') and we make everything lowercase.
tweets = []  # our new list of 'filtered' tweets
for (words, sentiment) in pos_tweets + neg_tweets:  # Join both our tuple lists above and loop over them
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]  # Words.split() to get each individual word,
# e.lower() to make them all lowercase
    tweets.append((words_filtered, sentiment))  # Our new tweets list also stores tuples, but now only the filtered
# words of each sentence
# Run your program and print to tweets to see what it looks like now!
print(str("2.)"))
print(tweets)

# == Machine Learning ==
# Machine learning is an Artificial Intelligence technique used in tons of fields such as Computer Vision (computers
# recognising images/faces/patterns), Language Processing (what we're doing now) and Bioinformatics
# What we are going to do is try create a program that uses 'training data' (a set of positive and negative tweets).
# We train the program on this set (called the training set), and since the tweets are already labelled as positive or
# negative, the program can learn probability wise what words are more common in the class of 'positive' tweets
# and the same for the class of 'negative' tweets. Once the program is 'trained' we then give it a new tweet and see if
# it classifies it as negative or positive correctly -> ie has it learnt?
# this is a common approach in Artificial Intelligence.

# == Building the classifier ==
# The classifier is the thing that is going to do the classification of tweets.
# First, the list of word features needs to be extracted from the tweets.
# This list has every unique word ordered by how frequently they occur.
# This is going to use the same FreqDist we saw in Task 1.
# First, we'll define two helper functions to help extract what we need.
# A simple function that gets all the words into a single list, extracted from the TUPLE list of (word,sentiment)


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:  # Remember that tweets is a list of TUPLES aka pair data (words, sentiment)
        all_words.extend(words)  # Add all the words to the list all_words
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)  # Apply the freqDist command to the word list
    word_features = wordlist.keys()  # Get each unique word and its frequency from the FreqDist we created
    return word_features

# Now let's apply both of the above!


all_words = get_words_in_tweets(tweets)  # We apply the first function to the list tweets we created above
print(str("3.)"))
print(all_words)

word_features = get_word_features(all_words)  # We apply the second function on all_words to get the Frequency of each
#  unique word in the list
print(str("4.)"))
print(word_features)
# If we took a look at 'wordlist' in the 'get_word_features' function above, it would look something like:
# 	<FreqDist:
#    'this': 6,
#    'car': 2,
#    'concert': 2,
#    'feel': 2,
#    'morning': 2,
#    'not': 2,
#    'the': 2,
#    'view': 2,
#    'about': 1,
#    'amazing': 1,
#    ...>
# As you can see, 'this' is the most common word in the tweets, followed by 'car'...etc
# To create a classifier that works, we need to only take the RELEVANT words (words that convey the sentiment)
# We need to decide which 'features' or words are relevant.
# To do that, we first need a feature extractor.
# We are gonna write a function that when given a text, it returns whether the text contains certain trigger words or
#  not. The trigger words are the words we have from 'word_features' above.


def extract_features(document):
    document_words = set(document)  # Return a list of each unique word in the inputted list of words
    features = {}
    for word in word_features:  # Remember we defined word_features above!
        features['contains(%s)' % word] = (word in document_words)  # Checks if the document has one of the words from
#  our word_features list, returns it in a list saying True or False
    return features
# It's not as bad as it looks.
# Lets try:


print(str("5.)"))
sent = ['love', 'this', 'car']
print(extract_features(sent))
# This prints out a list saying: {'contains(not)': False, .... contains(car)': True,...} etc. Try it for #yourself!
# It just tells us if an input sentence(with its word divided up into elements of a list) contains certain words or not!
# NOW! We can run this 'extract_features' function on our ENTIRE LIST of tweets we had above!
# We use the built in function apply_features to do this:

training_set = nltk.classify.apply_features(extract_features, tweets)
# Print out training_set, can you see what we've done?
# Our training set is a list of tweets, where we've taken each tweet and said if it contains certain #trigger words
# or not (this is its own list). We also have the sentiment of the tweet at the end, either '#postitive' or 'negative'
# == Training the classifier==
# Now that we have the training set (the set of data we want to train our AI on), we can train the classifier
# with the information about the trigger words that the set has and hasn't has.
# we can use the built in NLTK function to do this ie:

classifier = nltk.NaiveBayesClassifier.train(training_set)  # Remember we defined training_set in the last python line

# In the folder, open and take a look at the overview.png image. This is what we've just done.
# -> we used the Positive and Negative tweets to create a training set, by extracting the important
# 'trigger words' from the tweets (aka the word features), then creating a features extractor which we 
# then went back and applied to all our tweets to create the training set.
# -> We used the training set to build a classifier using the nltk.NaiveBayesClassifier (this will be explained soon)
# -> Now whenever we get a new Tweet (shown on the far right of the diagram) we can do the following:
#  1.) Apply the feature extractor to find the 'important' words.
#  2.) Plug how many of those important words they are into our classifier which can then spit out an answer and tell
#  us if the tweet we just saw is positive or negative!
# ************ WELCOME TO ARTIFICIAL INTELLIGENCE! ***********************
# == The Naive Bayes classifier explained (*NB THIS IS VERY IMPORTANT *) ==
# To explain the naive bayes classifier completely would require a bit of formula and mathematics
# So I'll give a simpler explanation
# This classification method is called 'Naive' because it assumes that we can just take all the words that we think are
# important (ie anything the feature extractor lets through) then take the probability that each of these words
# appears in a positive or negative tweet (called the PRIOR PROBABILITY, because it is something we know 'prior' to
# doing this) Then multiply EACH PROBABILITY THAT EACH WORD OCCURS IN A POSITIVE TWEET ALL TOGETHER to get a FINAL
# probability for the tweet being POSITIVE. And separately, multiply EACH PROBABILITY THAT EACH WORD OCCURS IN A
# NEGATIVE TWEET ALL TOGETHER to get a final probability for the tweet being NEGATIVE.
# Now compare both of the probabilities above and whichever one is higher defines if the tweet is positive or negative!
# ********************************* NB NB NB NB NB  *************************************************
# == But how do you get the probabilities? ===
# Scroll run up to the start of this task and look at pos_tweets list
# How often does the word 'amazing' appear?
# it appears in one tweet out of the 5 positive tweets. Hence, the probability of 'amazing' being the keyword in a
# positive tweet is 1 out of 5 or 1/5 = 0.2 = 20% chance
# So if we see a new input tweet that we are gonna put into our classifier, and the tweet is 'Amazing car',
# When the Naive Bayes classifier is calculating the probability that THIS new, unseen tweet is a positive one
# it will take the probability that 'amazing' is seen in a positive context, which it has learnt from the training
# set we gave it before (which we just found was 0.2) and then multiply that by the prob that 'car' appears in a
# positive context which (if you work it out from above) is also 0.2
# Hence Probability('Amazing car') is Positive = 0.2*0.2 = 0.4
# Now it does exactly the same for the negative case.
# 'Amazing' is NEVER seen in the training set of neg_tweets, hence the prob it occurs in a negative context is 0. We
# don't even need to compute the probability of car in a neg context because 0 times anything = 0
# Hence probability('Amazing car') is Negative = 0*whatever = 0
# 0.4 > 0 therefore classify 'Amazing car' as positive!
# ********************************* NB NB NB NB NB  *************************************************
# == Lets do some classification! ==

tweet = 'Riaz is not my friend'

# Follow the overview.png diagram from right (tweet) to the classifier!

# First, extract each word of the tweet into a list
tweetSplit = tweet.split()

# Now, extract the features that we care about
tweetSplitAndExtract = extract_features(tweetSplit)

# Now stick it into the Naive bayes Classifier!
print(str("6.)"))
print(classifier.classify(tweetSplitAndExtract))

# It's positive! Our classifier works, and we've built a genuinely useful program that can
# automatically detect positive and negative tweets without knowing very much
# We can even give it a bigger training set of tweets to build up the probabilities of words more accurately,
# and to make our classifier more powerful.

# === Your task ===
# If you understand the above - well done! It's something that definitely isn't done at UKZN until honors.
# Yet it isn't that complicated because Python has tools like NLTK to help you
# Now, make sure all the code in this Task 3 of using NLTK works for you and is in your file classifier.py
# At the bottom of classifier.py, using your classifier, classify the following tweets:
# "My house is not great"
# "The movie is not bad"
# "your song is annoying"
# See any problems? Can you suggest why these problems arise in these SPECIFIC tweets?

# == Optional Challenge ==
# Expand your training set for the classifier, retrain the classifier, and try classify the 3 tweets above again.
# Expanding your training set correctly should make the classifier classify the 3 tweets above correctly.
# You shouldn't have to write a lot of code to do this.
# ==================================================================================================
