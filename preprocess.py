import nltk
import re

#Tokenize sentences
def tokenize_text(text):
  return [(t) for t in re.sub(r"[^a-zA-Z0-9]+", ' ', text).split(' ')]

# NLTK POS tag
def pos_tagger(docs):
  data = []
  for i, doc in enumerate(docs):
      # Obtain the list of tokens in the document
      # tokens = [t for t in doc]

      # Perform POS tagging
      tagged = nltk.pos_tag(doc)
      data.append(tagged)
      
  return data

# Create feature vector
def word2features(doc, i):
  word = doc[i][0]
  postag = doc[i][1]

  # Common features for all words
  features = [
      'bias',
      'word.lower=' + word.lower(),
      'word[-3:]=' + word[-3:],
      'word[-2:]=' + word[-2:],
      'word.isupper=%s' % word.isupper(),
      'word.istitle=%s' % word.istitle(),
      'word.isdigit=%s' % word.isdigit(),
      'postag=' + postag
  ]

  # Features for words that are not
  # at the beginning of a document
  if i > 0:
      word1 = doc[i-1][0]
      postag1 = doc[i-1][1]
      features.extend([
          '-1:word.lower=' + word1.lower(),
          '-1:word.istitle=%s' % word1.istitle(),
          '-1:word.isupper=%s' % word1.isupper(),
          '-1:word.isdigit=%s' % word1.isdigit(),
          '-1:postag=' + postag1
      ])
  else:
      # Indicate that it is the 'beginning of a document'
      features.append('BOS')

  # Features for words that are not
  # at the end of a document
  if i < len(doc)-1:
      word1 = doc[i+1][0]
      postag1 = doc[i+1][1]
      features.extend([
          '+1:word.lower=' + word1.lower(),
          '+1:word.istitle=%s' % word1.istitle(),
          '+1:word.isupper=%s' % word1.isupper(),
          '+1:word.isdigit=%s' % word1.isdigit(),
          '+1:postag=' + postag1
      ])
  else:
      # Indicate that it is the 'end of a document'
      features.append('EOS')

  return features

# A function for extracting features in documents
def extract_features(doc):
  return [word2features(doc, i) for i in range(len(doc))]