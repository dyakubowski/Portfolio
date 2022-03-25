# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# import libraries for loading data and analyzies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from path import Path

# open folders in zip-files and read files
myzip = Path('/kaggle/input/two-sigma-connect-rental-listing-inquiries/sample_submission.csv.zip')
sample_sub = pd.read_csv(myzip, index_col='listing_id')

to_train = Path('/kaggle/input/two-sigma-connect-rental-listing-inquiries/train.json.zip')
data_train = pd.read_json(to_train)
# set listing indecies as indecies for dataframe
data_train.set_index('listing_id', inplace=True)

# and for testing data too
to_test = Path('/kaggle/input/two-sigma-connect-rental-listing-inquiries/test.json.zip')
data_test = pd.read_json(to_test)
data_test.set_index('listing_id', inplace=True)
# check if there is null values
data_train.info()

# look how many rows have values 'low', 'medium' and 'high'
print(Counter(data_train.interest_level.values))
# image barplot to look
n_count = data_train.interest_level.value_counts()
plot = sns.barplot(n_count.index, n_count.values)
plt.setp(plot.get_xticklabels(), rotation=30, fontsize=10)
plt.title('Distribution of interest_level values')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Values', fontsize=12)
plt.show()

# image heatmap imaging correlation link between variables
f, ax = plt.subplots(figsize=(20, 10))
sns.heatmap(data_train.corr(), vmin=-1, vmax=1, square=True, cmap='YlGnBu', annot=True)

# and built pairplots of distribution values between variables
the_strongest_corr = data_train.corr().price.sort_values(ascending=False)
sns.pairplot(data_train[dict(the_strongest_corr).keys()], size=2.5)
plt.show()

# the more photos the higher demand on appartament. Let's summarize photos and write it into new variable 
data_train["num_photos"] = data_train["photos"].apply(len)
# Let's consider that detail description is good opportunity to sale house or flat. Divide description into words and calculate their count 
data_train["new_description"] = data_train["description"].apply(lambda x: len(x.split(' ')))
# in the same way for testing dataframe
data_test["num_photos"] = data_test["photos"].apply(len)
data_test["new_description"] = data_test["description"].apply(lambda x: len(x.split(' ')))

# 'features' has all facilities in the flat or the house
cnt = Counter()
# choose 10 the most mentioned facilities in training dataframe
for feat in data_train.features:
    feats = set(map(str.lower, feat))  # make all letters lowercase
    for word in feats:
        cnt[word] += 1
    num_most_common = 10
# prepare list of these facilities to make new variables
most_common_feats = [k for k, _ in cnt.most_common(num_most_common)]
print(most_common_feats)

# create columns each of these will represent availability of one or the other facility
for feat in most_common_feats:
    # create new column
    data_train[feat] = 0
    for i in range(len(data_train['features'])):
        # 1 if this feature in this flat or house
        if feat in [s.lower() for s in data_train['features'].iloc[i]]:
            data_train[feat].iloc[i] = 1
        # 0 if otherwise
        else:
            data_train[feat].iloc[i] = 0
# the more features the more demand. Make column contains count of features
data_train['new_features'] = data_train["features"].apply(len)

# in the same way for testing data
cnt1 = Counter()
for feat in data_test.features:
    feats = set(map(str.lower, feat))
    for word in feats:
        cnt1[word] += 1
    num_most_common1 = 10
most_common_feats1 = [k for k, _ in cnt.most_common(num_most_common1)]
print(most_common_feats1)

for feat in most_common_feats1:
    data_test[feat] = 0
    for i in range(len(data_test['features'])):
        if feat in [s.lower() for s in data_test['features'].iloc[i]]:
            data_test[feat].iloc[i] = 1
        else:
            data_test[feat].iloc[i] = 0
data_test['new_features'] = data_test["features"].apply(len)

# import lybrary for date and time
import datetime

# let's define how long time listing is publicated on the site
data_train['days_listing'] = 0
for i in range(len(data_train['created'])):
    # format date and time to string massive
    date = datetime.datetime.strptime(data_train['created'].iloc[i], '%Y-%m-%d %H:%M:%S')
    # current data will be the 13th of March of 2022. Time will be midnight
    date_now = datetime.datetime.strptime('2022-03-13 00:00:00', '%Y-%m-%d %H:%M:%S')
    # subtract date of publication from current day
    total_days = (date_now - date).days
    # total days after date of publication
    data_train['days_listing'].iloc[i] = total_days

# the same way for testing data
data_test['days_listing'] = 0
for i in range(len(data_test['created'])):
    date = datetime.datetime.strptime(data_test['created'].iloc[i], '%Y-%m-%d %H:%M:%S')
    date_now = datetime.datetime.strptime('2022-03-13 00:00:00', '%Y-%m-%d %H:%M:%S')
    total_days = (date_now - date).days
    data_test['days_listing'].iloc[i] = total_days
    
# make copies of training data and testing to save data
data = data_train.copy()
testing_data = data_test.copy()
# drop columns on the basic which we created new columns. So we transformed them
data = data.drop(['created', 'description', 'photos', 'features'], axis=1)
testing_data = testing_data.drop(['created', 'description', 'photos', 'features'], axis=1)
# look how many values have rest categorical variables (type is 'object')
# 'interest_level' is variable for prediction. It is not considered
categorical = [feature for feature in data.columns if data[feature].dtype == 'object' and feature != 'interest_level']
# each feature of variable can be in a few cells
number = [len(data[features].unique()) for features in categorical]  # another ones have type 'int' or 'float'
# image count of features at dataframe
data_tuples = list(zip(categorical, number))
categorical_data = pd.DataFrame(data_tuples, columns=['Features', 'Number of distinct values'])  # calculate how many values has each categoric variable
print(categorical_data)  # 	Features	Number of distinct values
                         # 0	building_id	7585
                         # 1	display_address	8826
                         # 2	manager_id	3481
                         # 3	street_address	15358

# with module 'LabelEncoder' take for categoric features digit values
from sklearn.preprocessing import LabelEncoder

for c in categorical:
    label_encoder = LabelEncoder() 
    label_encoder.fit(list(data[c].values)) 
    data[c] = label_encoder.transform(list(data[c].values))
training_data = data.copy()
for c in categorical:
    label_encoder = LabelEncoder() 
    label_encoder.fit(list(testing_data[c].values)) 
    testing_data[c] = label_encoder.transform(list(testing_data[c].values))
# add column with average price per potentional person (bedroom) (0.125 is epsilon to avoid infinity values)
training_data["price_t"] = training_data["price"] / (training_data["bedrooms"] + 0.125)
# and total count of bedrooms and bathrooms
training_data["room_sum"] = training_data["bedrooms"] + training_data["bathrooms"]
# the same way for testing data
testing_data["price_t"] = testing_data["price"] / (testing_data["bedrooms"] + 0.125)
testing_data["room_sum"] = testing_data["bedrooms"] + testing_data["bathrooms"]
# Because 'interest_level' is object, make values digits n the such way:
training_data['interest_level'] = training_data['interest_level'].replace({'low': 0, 'medium': 1, 'high': 2})

# formulate training and testing data. Highlight variable 'interest_level' as estimated
X_train = training_data.drop(['interest_level'], axis=1)
X_test = testing_data
y_train = training_data.interest_level

# import libraries for making model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

# use model RandomForestClassifier and fit it
# divide trainig data into train and test and check them for exactness
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.33)
clf = RandomForestClassifier(n_estimators=1000)
# fit model
clf.fit(X_train, y_train)
# predict values from training dataframe and compare these with original
y_val_pred = clf.predict_proba(X_val)
print(log_loss(y_val, y_val_pred))  # 0.5926415817437775

# predict probabilities of interest level for testing data
y_final = clf.predict_proba(X_test)
# make classes for submission and rename keys (for 0 is 'low', for 1 - 'medium', for 2 - 'high')
labels_interesting_level = {label: i for i, label in enumerate(clf.classes_)}
for_replace = {0: 'low', 1: 'medium', 2: 'high'}
for i in labels_interesting_level:
    if i in for_replace:
        labels_interesting_level[for_replace[i]] = labels_interesting_level.pop(i)
print(labels_interesting_level)  # {'low': 0, 'medium': 1, 'high': 2}

# create dataframe for predicted values
submission = pd.DataFrame()
data_test = data_test.reset_index()
submission["listing_id"] = data_test["listing_id"]
# write results for 'low', 'medium' and 'high' levels respectively
for label in ['low', 'medium', 'high']:
    submission[label] = y_final[:, labels_interesting_level[label]]
# write the dataframe to file
submission.to_csv("late_submission.csv", index=False)
