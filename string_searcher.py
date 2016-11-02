"""
This class allows filtering of a dataframe based on whether or not a
dataframe column value contains the target string.

SAMPLE USAGE:
searcher = StringSearcher()
searcher.set_corpus('C:/Users/User/Desktop/myFile.csv')
searcher.find('manila irrigation')
>>> manila north rd ...
"""

from __future__ import print_function
import pandas as pd


class StringSearcher(object):

    def __init__(self):
        self.corpus = None

    def set_corpus(self, corpus):
        """
        Set the dataframe to use as a search space.

        corpus: Path to CSV file or pandas dataframe.
        """
        if type(df_corpus) in [str, unicode]:
            corpus = pd.read_csv(corpus)
        self.corpus = corpus

    def find(self, pattern, on = 'searchspace', regex=False, dfOutput=True):
        """
        pattern: A string to search for.
        on: name of data frame column to use as search space.
        regex: Set to True to use pattern as a regex.
        dfOutput: set to False to output a dictionary instead of a pandas dataframe

        self.corpus must be a dataframe with a column whose name is specified
        in the "on" argument.

        Returns a dictionary.
        """
        search = self.corpus[self.corpus[on].notnull()].astype(str)
        found = search[search[on].str.contains(str(pattern),
                                               case=False,
                                               regex=regex)]
        if dfOutput:
            return found
        return found.to_dict('list')

if __name__ == '__main__':
    pass