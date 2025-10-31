import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The striped bats are hanging on their feet for best"
tokens = nltk.word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
print("Original Text:", text)
print("Lemmatized Text:", ' '.join(lemmatized))
