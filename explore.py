#!/usr/bin/env python

"""
This script originally written by the CodeUp Queers
group for their capstone project in 2019 at CodeUp.
Used with permission.

1. Ednalyn C. De Dios
2. Jesse Ruiz
3. Madeleine Capper

"""

# ===========
# ENVIRONMENT
# ===========

import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import operator


def get_significant_t_tests(df, continuous_vars, target):
    '''
    Runs t-tests between two groups from 
    df: a dataframe and 
    continuous_vars: a list of column names.
    against
    target: a comparative variable from df to test between

    If test results are noteworthy due to the t-statistic and p-value, results are printed

    Returns a list of perceived significant features and a dictionary with variable name and t-statistic
    '''
    some_feats = []
    some_dict = {}
    train_df = df
    buildstr1 = r'train_df[train_df.' + target + r' == 1].'
    buildstr2 = r'train_df[train_df.' + target + r' == 0].'
    for feat in continuous_vars:
        affirmative = buildstr1 + feat
        negative = buildstr2 + feat
        tstat, pval = stats.ttest_ind(eval(affirmative), eval(negative))
        if pval < 0.05:
            print(f'Feature analyzed: {feat}')
            print(
                'Our t-statistic is {:.4} and the p-value is {:.10}'.format(tstat, pval))
            print('----------')
            some_feats.append(feat)
            some_dict[feat] = tstat
        else:
            print(f'Feature analyzed: {feat}')
            print(
                'Our t-statistic is {:.4} and the p-value is {:.10}'.format(tstat, pval))
            print('----------')


    return some_feats, some_dict


def get_chi_squared(df, features, target):
    '''
    Runs chi-squared test between two categorical variables from 
    df: a dataframe and
    features: a list of columns
    target: a variable name to compare to the cycled features list

    Results are printed depending on perceived significance
    Returns a list of significant features as well as a dictionary with chi-stat
     '''
    train_df = df
    sig_feats = []
    sig_dict = {}
    for feat in features:
        tbl = pd.crosstab(train_df[feat], train_df[target])
        stat, p, dof, expected = stats.chi2_contingency(tbl)
        prob = .95
        critical = stats.chi2.ppf(prob, dof)
        if abs(stat) >= critical:
            if p < 0.05:
                sig_dict[feat] = abs(stat)
                print(feat)
                print('Dependent (reject H0)')
                print('-----------------------')
                sig_feats.append(feat)
        else:
            pass
    return sig_feats, sig_dict


def sort_sigs(a_dict):
    '''
    takes in a dictionary (a_dict) and sorts based on values associated with each key
    '''
    val_list = []
    for key in a_dict:
        val_list.append(a_dict[key])
        sorted_vals = sorted(
            a_dict.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_vals


def combine_significants(dict1, dict2):
    '''
    takes in 
    dict1 and dict2: two dictionaries
    converts to two lists of tuples and creates 
    a new list with the 
    first element of each of the argument lists
    returns a new list of all features
    '''
    list1 = sort_sigs(dict1)
    list2 = sort_sigs(dict2)
    new_list = []
    for item in list1:
        new_list.append(item[0])
    for item in list2:
        if item not in(new_list):
            new_list.append(item[0])
    return new_list


def make_violin1(df, features):
    for feature in features:
        sns.violinplot(y=df[feature])
        plt.show()


def make_violin2(df, target, features):
    for feature in features:
        sns.violinplot(data=df, x=target, y=feature)
        plt.show()


def make_violin3(df, features, continuous, target):
    for feature in features:
        sns.violinplot(data=df, x=feature, y=continuous, hue=target, split=True)
        plt.show()



def swarrrm(df, cat, num_vars):
    '''
    creates a series of swarm plots from a dataframe (df)
     using a categorical variable (cat) 
     and a list of continuous ones (num_vars)
     '''
    for var in num_vars:
        plt.figure(figsize=(10, 6))
        sns.swarmplot(data=df, x=cat, y=var)
        plt.show()


def make_rel(df, x, y, hue):
    '''
    creates a relplot from a dataframe df using 
    two continuous (x, y)
    and one categorical (hue) variable
    '''
    sns.relplot(x=x, y=y, hue=hue, data=df)


def make_rels(df, feat1, feat2, features):
    '''
    takes in a a dataframe df,
    feat1 and fat2:  two feature variable names, and 
    features: a list of other features for comparative relplots
    '''
    for feat in features:
        make_rel(df, feat1, feat2, feat)
        plt.show()


def make_bars(df, features):
    '''
    creates bar plots based on
    df: a pandas dataframe,
    metric: a string literal for the rate being evaluated and
    features: a list of categorical variables 
    '''
    for feature in features:
        df[feature].value_counts().plot(kind='bar', xlabel=feature, ylabel="Count", rot=0)
        plt.show()


def plot_hist(df):
    """
    Plots the distribution of the dataframe's variables.
    """
    df.hist(figsize=(24, 20), bins=20)

# ==================================================
# MAIN
# ==================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    """Main entry point for the script."""
    pass

if __name__ == '__main__':
    sys.exit(main())


__authors__ = ["Ednalyn C. De Dios", "Jesse Ruiz", "Matthew Capper"]
__copyright__ = "Copyright 2023, Codeup Data Science"
__credits__ = ["Maggie Guist", "Zach Gulde"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainers__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"