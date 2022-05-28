# import libraries to work with dataframe
from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
# import libraries to process text and remove unnecessary symbols
import re
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
from string import punctuation
# load method to classify text and predict categories and find the optimal parametres for exact forecasts
import fasttext
from sklearn.model_selection import train_test_split

drive.mount('/content/drive', force_remount=True)
# load file with training data and testing data and formulate dataframes
data_train = pd.read_csv('/content/drive/MyDrive/PlatformaOFD/train.csv', sep=';')
data_test = pd.read_csv('/content/drive/MyDrive/PlatformaOFD/test.csv', sep=';')
# this submission file for writting predicted results
sample_submission = pd.read_csv('/content/drive/MyDrive/PlatformaOFD/sample_submission.csv', sep=';')
# check corresponding values in sample_submission and testing data
print((sample_submission['pn_id']==data_test['pn_id']).all())
# persuade that order numbers in training data don't match to order numbers in testing data
print(set() == set(data_test['pn_id'].unique())&set(data_train['pn_id'].unique()))
# print training and testing data
print(data_train.head().to_markdown())
print(data_test.head().to_markdown())

# get information about training data
print(data_train.info())
# how many values has each of category's name and how level of confidence
print(data_train['category_name'].value_counts())
print(data_train['confidence'].value_counts())
# built plot of distribution category names
category_features = data_train['category_name'].value_counts()
plot = sns.barplot(category_features.index, category_features.values)
plt.setp(plot.get_xticklabels(), rotation=90, fontsize=10)
plt.title('Distribution of interest_level values', fontsize=15)
plt.ylabel('appereance counts', fontsize=12)
plt.xlabel('Category names', fontsize=12)
plt.show()

# create copy of training data and make all letters with lower case
data_train1 = data_train.copy()
data_train1.product_name = data_train1.product_name.str.lower()
# make cloud of words from dataframe
def str_corpus(corpus):
    '''
    transform list of word from corpus to the whole string
    param corpus: list of values (words) for column
    return: string consisting of words from cell
    '''    
    # make empty string
    str_corpus = ''
    # add each word diving by spaces
    for i in corpus:
        str_corpus += ' ' + i
    # remove newline character
    str_corpus = str_corpus.strip()
    return str_corpus

def get_corpus(data):
    '''
    transform cells of dataframe's column to list of containing
    param data: column of dataframe
    return: list of words from each cells
    '''
    # create empty list
    corpus = []
    # split cells and each character and word add to the list
    for phrase in data:
        for word in phrase.split():
            corpus.append(word)
    return corpus

def get_wordCloud(corpus):
    '''
    create image of word's distribution in dataframe
    param corpus: list of words
    return: word cloud (the oftener the more size of word)
    '''
    # use method WordCloud and take parametres of image
    wordCloud = WordCloud(background_color='white',
                          stopwords=STOPWORDS,
                              width=3000,
                              height=2500,
                              max_words=200,
                              random_state=42
                         ).generate(str_corpus(corpus))
    return wordCloud

# transform dataframe to list and then transform to string
corpus = get_corpus(data_train1['product_name'].values)
procWordCloud = get_wordCloud(corpus)
# image word cloud
fig = plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
plt.imshow(procWordCloud)
plt.axis('off')
plt.subplot(1, 2, 1)

# download stopwords and processing strings in dataframe
nltk.download("stopwords")
russian_stopwords = stopwords.words("russian")
def remove_punct(text):
    '''
    remove punctuation characters by replacing by spaces
    param text: cell of column
    return: edited cell
    '''    
    table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ', 64: ' ', 91: ' ', 92: ' ', 93: ' ', 94: ' ', 95: ' ', 96: ' ', 123: ' ', 124: ' ', 125: ' ', 126: ' '}
    return text.translate(table)

data_train1['product_name'] = data_train1['product_name'].map(lambda x: x.lower())  # all characters are lower case
data_train1['product_name'] = data_train1['product_name'].map(lambda x: remove_punct(x))  # remove punctuation characters
data_train1['product_name'] = data_train1['product_name'].map(lambda x: x.split(' '))  # split by spaces
data_train1['product_name'] = data_train1['product_name'].map(lambda x: [token for token in x if token not in russian_stopwords\
                                                                  and token != " " \
                                                                  and token.strip() not in punctuation])  # create list of tokens which are words
data_train1['product_name'] = data_train1['product_name'].map(lambda x: ' '.join(x))  # unite words to string by spaces
# check result of processing with word cloud
corpus = get_corpus(data_train1['product_name'].values)
procWordCloud = get_wordCloud(corpus)

fig = plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
plt.imshow(procWordCloud)
plt.axis('off')
plt.subplot(1, 2, 1)

# make transformations with data in the column with regular expressions
# replace abbreviated words to full ones
data_train1.product_name = data_train1.product_name.str.replace('ё', 'е')
data_train1.product_name = data_train1.product_name.str.replace(r'шт\.*', 'штук')
data_train1.product_name = data_train1.product_name.str.replace(r'-', ' ')
data_train1.product_name = data_train1.product_name.str.replace(r'мм\.*', 'миллиметр')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*эко*\S*', 'эко')
# bring key words to initial form
data_train1.product_name = data_train1.product_name.str.replace(r'\S*материал*\S*', 'материал')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*ручк*\S*', 'ручка')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*накопител*\S*', 'накопитель')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*лист*\S*', 'лист')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*принтер*\S*', 'принтер')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*картридж*\S*', 'картридж')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*штук*\S*', 'штук')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*черн*\S*', 'черный')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*час*\S*', 'час')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*услуг*\S*', 'услуга')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*умн*\S*', 'умный')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*стал*\S*', 'сталь')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*систем*\S*', 'система')
data_train1.product_name = data_train1.product_name.str.replace(r'\S*сет*\S*', 'сеть')
# remove digits and too many spaces
data_train1.product_name = data_train1.product_name.str.replace(r'\S*\d+\S*', '')
data_train1.product_name = data_train1.product_name.str.replace(r'\b\s{2,}\b', ' ')
data_train1.product_name = data_train1.product_name.str.replace(r'^\s{2,}', '')
data_train1.product_name = data_train1.product_name.str.replace(r'\s{2,}$', '')
# transform column values to lists
product_names = data_train1.product_name.to_list()
# get rid of digits at the end of strings (means count usually)
for i in range(len(product_names)):
    product_names[i] = re.findall(r'.*?,\D|.*', product_names[i])[0]
# check result of processing with word cloud
corpus = get_corpus(data_train1['product_name'].values)
procWordCloud = get_wordCloud(corpus)

fig = plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
plt.imshow(procWordCloud)
plt.axis('off')
plt.subplot(1, 2, 1)

# column 'confidence' assign type 'string' and add to corresponding column 'product_name' and depart by space
data_train1 = data_train1.astype({"confidence": "str"})
data_train1['product_name'] = data_train1['product_name'] + ' ' + data_train1['confidence']
print(data_train1)

# split training dataframe into training and testing data. For testing data highlight 20 percent
X_train, X_test, y_train, y_test = train_test_split(data_train1['product_name'], data_train1['category_name'], test_size=0.2)
# transform dataframes X_train (column 'product_name'), y_train (column 'category_name') to text file 'train.txt' for follow work
with open('train.txt', 'w') as train_predict:
    # create new file and write cells as lines to this file
    for each_text, each_label in zip(X_train, y_train):
        train_predict.writelines(f'__label__{each_label} {each_text}\n')
# X_test (column 'product_name') and y_test (column 'category_name') to text file 'test.txt' for follow work
with open('test.txt', 'w') as test_predict:
    # create new file and write cells as lines to this file
    for each_text, each_label in zip(X_test, y_test):
        test_predict.writelines(f'__label__{each_label} {each_text}\n')
!head -n 10 train.txt

def print_results(sample_size, precision, recall):
    '''
    calculate results of predicted testing data by fitted fasttext classifier model
    param sample_size: count of testing values
    param precision: model's accuracy during defining the Positive class
    param recall: how many Positive classes are defined correctly among all Positive ones
    '''
    precision = round(precision, 5)
    recall = round(recall, 5)
    print(f'sample_size={sample_size}')
    print(f'precision={precision}')
    print(f'recall={recall}')

# fit fasttext classifier model selecting parametres
# after fitting define accuracy for testing data
model1 = fasttext.train_supervised('train.txt')
print(print_results(*model1.test('test.txt')))
model2 = fasttext.train_supervised('train.txt', epoch=25)
print(print_results(*model2.test('test.txt')))
model3 = fasttext.train_supervised('train.txt', epoch=10)
print(print_results(*model3.test('test.txt')))
model4 = fasttext.train_supervised('train.txt', epoch=25, lr=1.0)
print(print_results(*model4.test('test.txt')))
model5 = fasttext.train_supervised('train.txt', epoch=10, lr=1.0, wordNgrams=2)
print(print_results(*model5.test('test.txt')))
model6 = fasttext.train_supervised('train.txt', autotuneValidationFile='test.txt') 
print(print_results(*model6.test('test.txt')))

# the most accurate calculation for model2(epoch=25): precision=0.99975, recall=0.99975
# save this model as optimized model and create a function to classify new data
model2.save_model('predict.py')
# compress the model to economise memory
model2.quantize(input='train.txt', retrain=True)

# processing testing data like training data
data_test1 = data_test.copy()
data_test1.product_name
def remove_punct(text):
    '''
    remove punctuation characters by replacing by spaces
    param text: cell of column
    return: edited cell
    '''
    table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ', 64: ' ', 91: ' ', 92: ' ', 93: ' ', 94: ' ', 95: ' ', 96: ' ', 123: ' ', 124: ' ', 125: ' ', 126: ' '}
    return text.translate(table)

data_test1['product_name'] = data_test1['product_name'].map(lambda x: x.lower())  # all characters are lower case
data_test1['product_name'] = data_test1['product_name'].map(lambda x: remove_punct(x))  # remove punctuation characters
data_test1['product_name'] = data_test1['product_name'].map(lambda x: x.split(' '))  # split by spaces
data_test1['product_name'] = data_test1['product_name'].map(lambda x: [token for token in x if token not in russian_stopwords\
                                                                  and token != " " \
                                                                  and token.strip() not in punctuation])  # create list of tokens which are words
data_test1['product_name'] = data_test1['product_name'].map(lambda x: ' '.join(x))  # unite words to string by spaces
# check result of processing with word cloud
corpus = get_corpus(data_test1['product_name'].values)
procWordCloud = get_wordCloud(corpus)

fig = plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
plt.imshow(procWordCloud)
plt.axis('off')
plt.subplot(1, 2, 1)

# make transformations with data in the column with regular expressions
# replace abbreviated words to full ones
data_test1.product_name = data_test1.product_name.str.replace('ё', 'е')
data_test1.product_name = data_test1.product_name.str.replace(r'шт\.*', 'штук')
data_test1.product_name = data_test1.product_name.str.replace(r'-', ' ')
data_test1.product_name = data_test1.product_name.str.replace(r'мм\.*', 'миллиметр')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*эко*\S*', 'эко')
# bring key words to initial form
data_test1.product_name = data_test1.product_name.str.replace(r'\S*материал*\S*', 'материал')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*ручк*\S*', 'ручка')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*накопител*\S*', 'накопитель')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*лист*\S*', 'лист')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*принтер*\S*', 'принтер')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*картридж*\S*', 'картридж')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*штук*\S*', 'штук')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*черн*\S*', 'черный')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*час*\S*', 'час')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*услуг*\S*', 'услуга')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*умн*\S*', 'умный')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*стал*\S*', 'сталь')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*систем*\S*', 'система')
data_test1.product_name = data_test1.product_name.str.replace(r'\S*сет*\S*', 'сеть')
# remove digits, too many spaces (let one space be instead) and line feeds
data_test1.product_name = data_test1.product_name.str.replace(r'\S*\d+\S*', '')
data_test1.product_name = data_test1.product_name.str.replace(r'\b\s{2,}\b', ' ')
data_test1.product_name = data_test1.product_name.str.replace(r'^\s{2,}', '')
data_test1.product_name = data_test1.product_name.str.replace(r'\s{2,}$', '')
data_test1.product_name = data_test1.product_name.str.replace(r'\n', '')
print(data_test1)

# load fitted optimized model
model_for_prediction = fasttext.load_model('predict.py')
# create list of predicted categories
categories = []
# predict category for each cell of column 'product_name' and add to list 'categories'
for i in range(len(data_test1)): 
    category = model_for_prediction.predict(data_test1.product_name.iloc[i])
    categories.append(category[0][0])
# add to dataframe 'sample_submission' column with predicted categories and delete '__label__' in values
sample_submission['category_name'] = categories
sample_submission.category_name = sample_submission.category_name.str.replace('__label__', '')
sample_submission.to_csv('sample_submission.csv')
