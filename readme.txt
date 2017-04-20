This project uses three python class files and three text files. The first class file,
TweetTracker, user the Tweepy Twitter api to go through each of the user's
friends on Twitter and retrieve the twenty most recent tweet from each friend.
Each tweet is converted to its ascii representation and written to the text
file, slang.txt. The second class, tweetCleaner, examines every word in
slang.txt and determines if the word is slang by comparing it to the
nltk corpus. The algorithm also removes links, Twitter hashtags, and numbers.
Each slang word is then written to a file, slangwords.txt. The third class,
tagger, uses that files to look for regular expression patterns in each word.
The first pattern that matches is assumed to be the word's part of speech. If
no matching patter is found, the word is assumed to be a noun. Each word and it's
part of speech is then written into a text file. 
