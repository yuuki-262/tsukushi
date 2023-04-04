import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# データの準備
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(sentence):
    tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    tokens = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stop_words]
    return {word: True for word in tokens}

training_data = [
    ("I love programming.", "positive"),
    ("Python is my favorite language.", "positive"),
    ("I hate doing boring tasks.", "negative"),
    ("I don't like this food.", "negative"),
]

test_data = [
    ("I enjoy learning new things.", "positive"),
    ("This movie is terrible.", "negative"),
]

# 前処理と分類器の学習
training_data = [(preprocess(sentence), sentiment) for sentence, sentiment in training_data]
classifier = NaiveBayesClassifier.train(training_data)

# テストデータの評価
test_data = [(preprocess(sentence), sentiment) for sentence, sentiment in test_data]
print("Accuracy: ", accuracy(classifier, test_data))

# 新しい文章の分類
new_sentence = "I love learning new programming languages."
tokens = preprocess(new_sentence)
result = classifier.classify(tokens)
print(f"The sentiment of the new sentence is: {result}")