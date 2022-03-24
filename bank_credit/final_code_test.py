# import libraries to work with dataframe
import numpy as np
import pandas as pd
from datetime import datetime

# create dataframe contains 10000 rows and assign values for columns
size = 10000

df = pd.DataFrame(
    {
        'time': [*pd.date_range('2001-01-01', '2020-09-01', freq='1h')][:size],
        'user_id': np.random.choice(1000, size),
        'type': np.random.choice(2, size, p=[0.8, 0.2]),
        'amount': [int(x//1) for x in  np.random.normal(15_000, 1_000, size)],
        'target': np.random.choice(2, size, p=[0.5, 0.5]),
    },
    index=[*range(size)],
)

# add column 'is_loan' which has value 0 if loan request is considered, 1 if request loan is approved
df['is_loan'] = df['type']
df['type'] = df['type'].replace({0: 'loanRequest', 1: 'loan'})

# save dataframe to the source csv-file
df.to_csv('test_origin.csv', index=False)

def calculate_events_number(df):
    """
    calculate order numbers of events for each user separately
    param df: dataframe for calculating
    return: dataframe with added column contains order numbers
    """
    # define all users who are served in the bank
    users = df['user_id'].unique()
    # assign 'events_ordinal_number' column zero values 
    df['events_ordinal_number'] = 0
    # order is calculated for each user separately
    for user in users:
        # create mini-dataframe where there are rows with common user and sort it by event time
        df_user = df[df['user_id'] == user].sort_values(['time'])
        # the first event has value 1, the following values are autoincreasing
        for row in range(len(df_user)):
            df_user['events_ordinal_number'].iloc[row] = row + 1
        # replace matched cells by user, index number and position in the mini-dataframe
        for i in range(len(df_user.index.values)):
            df.loc[df_user.index.values[i], 'events_ordinal_number'] = df_user['events_ordinal_number'].iloc[i]
    return df
  
  def calculate_second_event_time(df):
    """
    for each user defines when the second event was happended with him
    param df: dataframe for calculating
    return: dataframe with added column contains the second events
    """
    # define all users who are served in the bank
    users = df['user_id'].unique()
    # assign 'second_event_time' column zero values
    df['second_event_time'] = 0
    # create list for tuples consisted from user's id and the second event date for him
    second_events_users = []
    for user in users:
        # create mini-dataframe where there are rows with common user and sort it by event time
        # choose from this mini-dataframe the second value of column 'time'
        second_time = df[df['user_id'] == user].sort_values(['time']).iloc[1]['time']
        # this value with corresponding user's id add to the list
        second_events_users.append((user, second_time))
    # replace matched cells by user, index number and position in the mini-dataframe
    for num in range(len(second_events_users)):
        df.loc[df.user_id == second_events_users[num][0], 'second_event_time'] = second_events_users[num][1]
    return df
  
  # весь код расчета признака должен быть в этом методе
def calculate_loan_number(df):
    """
    for each user define order number of loan by datetime including requests to this loan.
    All these requests will have the same order number that loan has
    param df: dataframe for calculating
    return: dataframe with added column contains order numbers
    """
    # define all users who are served in the bank
    users = df['user_id'].unique()
    # assign 'loan_ordinal_number' column zero values
    df['loan_ordinal_number'] = 0
    # order is calculated for each user separately
    for user in users:
        # create mini-dataframe where there are rows with common user and sort it by event time
        df_user = df[df['user_id'] == user].sort_values(['time'])
        # transform column 'loan_ordinal_number' into array with library 'numpy'
        array_loan_num = np.array(df_user['loan_ordinal_number'])
        # the first request or approved loan will has order number 1
        n = 1
        for i in range(len(array_loan_num)):
            # all requests to loan have the same order number
            if df_user['is_loan'].iloc[i] == 0:
                array_loan_num[i] = n
            # this number has the current loan
            else:
                array_loan_num[i] = n
                # for the next requests order number is more on 1
                n += 1
        # replace array from values in column 'loan_ordinal_number' with matched cells by user and index number to get array
        df.loc[df_user.index.values, 'loan_ordinal_number'] = array_loan_num
    return df
  
  # весь код расчета признака должен быть в этом методе
def calculate_time_diff(df):
    """
    calculate how much time passed from previous event to current one
    param df: dataframe for calculating
    return: dataframe with column contains time differences (for each user separately)
    """
    # define all users who are served in the bank
    users = df['user_id'].unique()
    # assign 'events_time_diff' column zero values
    df['events_time_diff'] = None
    # time difference is calculated for each user separately
    for user in users:
        # create mini-dataframe where there are rows with common user and sort it by event time
        df_user = df[df['user_id'] == user].sort_values(['time'])
        # transform column 'events_time_diff' into array with library 'numpy'
        array_time_dif = np.array(df_user['events_time_diff'])
        # the first element of the array has value 'None'
        # for the rest the current element's value is difference between datetime's value of the mathed current index of mini-dataframe
        # and datetime's value of the previous index of this mini-dataframe 
        for i in range(1, len(array_time_dif)):
            array_time_dif[i] = df_user['time'].iloc[i] - df_user['time'].iloc[i - 1]
        # replace array from values in column 'events_time_diff' with matched cells by user and index number to get array
        df.loc[df_user.index.values, 'events_time_diff'] = array_time_dif
    return df
  
  # весь код расчета признака должен быть в этом методе
def calculate_previous_max_amount(df):
    """
    calculate at each time moment what maximal sum of loan was approved by bank for each user from his registration in the bank
    param df: dataframe for calculating
    return: dataframe with column contains maximal loan's sums at the current moment
    """
    # define all users who are served in the bank
    users = df['user_id'].unique()
    # assign 'previous_loans_max_amount' column zero values
    df['previous_loans_max_amount'] = 0
    # time difference is calculated for each user separately
    for user in users:
        # create mini-dataframe where there are rows with common user and sort it by event time
        df_user = df[df['user_id'] == user].sort_values(['time'])
        # transform column 'previous_loans_max_amount' into array with library 'numpy'
        array = np.array(df_user['previous_loans_max_amount'])
        # initially max loan for all time is zero
        max_prev_loan = 0
        for i in range(len(array)):
            # if loan request is approved this approved loan is not taken account of amount's list
            # but maximal amount is defined as maximum between this loan's amount and previous current maximum
            if df_user['is_loan'].iloc[i] == 1:
                array[i] = max_prev_loan
                max_prev_loan = max(max_prev_loan, df_user['amount'].iloc[i])
            # if request maximal amount is saved
            else:
                array[i] = max_prev_loan
        # replace array from values in column 'previous_loans_max_amount' with matched cells by user and index number to get array
        df.loc[df_user.index.values, 'previous_loans_max_amount'] = array
    return df

# execute all functions and add columns to the dataframe
def calculate_feature(df):
    calculate_events_number(df)
    calculate_second_event_time(df)
    calculate_loan_number(df)
    calculate_time_diff(df)
    calculate_previous_max_amount(df)
    
%%timeit -o 
calculate_feature(df)

columns = ['time']
rez = _
df_time = pd.DataFrame([rez], None, columns)
df_time.to_csv('time.csv', index=False)

df.to_csv('test.csv', index=False)
