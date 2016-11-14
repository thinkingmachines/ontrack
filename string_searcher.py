"""
This class allows filtering of a dataframe based on whether or not a
dataframe column value contains the target string.
"""


from __future__ import print_function
import pandas as pd

def es_find(df, pattern, regex=False):
    '''
    df: The database to find the pattern in
    pattern: A string to search for.
    regex: Set to True to use pattern as a regex.

    self.corpus must be a dataframe with a column whose name is specified
    in the "on" argument.

    Returns the dfA row numbers of satisfactory rows in dfB.
    '''
    found = df[df.str.contains(str(pattern), case=False, regex=regex)].index
    return found

if __name__ == '__main__':
    pass