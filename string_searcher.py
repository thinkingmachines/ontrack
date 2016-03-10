'''
This class allows filtering of a dataframe based on whether or not a 
dataframe column value contains the target string.
'''

from __future__ import print_function
import pandas as pd


class StringSearcher(object):

    def __init__(self):
        self.corpus = None

    def set_corpus(self, corpus):
        '''
        Set the dataframe to use as a search space.
        '''
        self.corpus = corpus

    def find(self, pattern, on, regex=False):
        '''
        pattern: A string to search for.
        on: name of data frame column to use as search space.
        regex: Set to True to use pattern as a regex.

        self.corpus must be a dataframe with a column whose name is specified 
        in the "on" argument.

        Returns a DataFrame.
        '''
        try:
            return self.corpus[self.corpus[on].str.contains(str(pattern),
                                                            case=False,
                                                            regex=regex)]
        except AttributeError:
            print('Corpus must be an instance of <pandas.core.frame.DataFrame>')
            return pd.DataFrame()

if __name__ == '__main__':
    pass
