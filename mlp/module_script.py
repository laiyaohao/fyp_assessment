import os
import sys

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import feature_column


def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=5):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function


def tf_estimator(filename):
    dataframe = pd.read_csv(filename)
    labels = dataframe.pop('Class')
    train, test = train_test_split(dataframe, test_size=0.5)
    
    train_labels, test_labels = train_test_split(labels, test_size=0.5)


    train_ds = make_input_fn(train, train_labels)
    test_ds = make_input_fn(test, test_labels, shuffle=False)

    feature_columns = []
    for feature_name in list(dataframe.columns):
        feature_columns.append(tf.feature_column.numeric_column(feature_name))

    linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
    linear_est.train(train_ds)
    result = linear_est.evaluate(test_ds)

    print(result)
