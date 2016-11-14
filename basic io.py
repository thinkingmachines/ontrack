'''
Interfaces with the rest of the OnTrack package.

SAMPLE USAGE:
dfA = read('looking_for.csv')
dfB = read('looking_in.csv')

results = find_closest(dfA, dfB)
'''

import pandas as pd

from text_cleaners import clean_text
from cosine_matcher import CosineMatcher
from string_searcher import es_find

cos_match = CosineMatcher()

def read(path, keep_columns='', encoding='latin-1'):
    '''
    Transforms a csv file into the format used by OnTrack (pandas DataFrame).
    
    Input
    path: The csv filepath.
    keep_columns: The columns of the csv which should appear in the output files.
    encoding: The encoding used by the csv file.
    
    Output
    Pandas DataFrame
    '''
    if keep_columns:
        try:
            db = pd.read_csv(path, usecols=[keep_columns], encoding=encoding, error_bad_lines=False)
        except ValueError:
            db = pd.read_csv(path, encoding=encoding, error_bad_lines=False)
            print "The columns provided are invalid. All columns will be kept."
    else:
        db = pd.read_csv(path, encoding=encoding, error_bad_lines=False)
    db = db.dropna(axis=0, how='all')
    return db
    
def clean_subset(db, cols='', cleaner=clean_text):
    '''
    Concatenates and cleans a columnar subset of df.
    
    Input
    db: A database.
    cols: The subset you wish to keep in the output csv. 
          Entries should always be enclosed by brackets, e.g. ['id'] or ['id1', 'id2']
    cleaner: Desired cleaner, by default set to OnTrack's text cleaner. 
             Set to None if the DataFrame has already been cleaned.
    
    Output
    A pandas Series containing the transformed strings.
    '''
    if cols:
        try:
            db = db[cols]
        except KeyError:
            print "At least one of the columns you entered is not in the given database. The whole database will be kept."
    db = db.astype('unicode').apply((lambda x: ' '.join(x)), axis=1)
    if cleaner:
        db = db.apply(cleaner)
    return db

def find_exact(dbA, dbB, colA='', colB='', regex=False, cleaner=clean_text, fname='exact search'):
    '''
    Finds exact matches of dbA terms in dbB.
    
    Input
    dfA: The database containing terms you're looking for.
    dfB: The database you're looking in for dbA's terms.
    colA: Columns which should be used in dbA. 
          Entries hould always be enclosed by brackets, e.g. ['id'] or ['id1', 'id2']
    colB: Columns which should be used in dbB. 
          Entries hould always be enclosed by brackets, e.g. ['id'] or ['id1', 'id2']
    regex: Set to True to use dbA search terms as regex patterns.
    cleaner: Desired cleaner, by default set to OnTrack's text cleaner. 
             Set to None if the DataFrame has already been cleaned.
    fname: The desired filename of the output csv files.
    
    Output
    Pandas DataFrame containing matches found.
    Csv output: dfA-dfB matches.
    '''
    dbA = pd.DataFrame(dbA, index=range(len(dbA)))
    dbB = pd.DataFrame(dbB, index=range(len(dbB)))
    if cleaner:
        A = clean_subset(dbA, colA, cleaner)
        B = clean_subset(dbB, colB, cleaner)
    found = A.apply(lambda x: es_find(B, x, regex=regex))
    db = pd.DataFrame([], columns=['nth query'])
    noResult = pd.DataFrame()
    for i in xrange(len(dbA)):
        if not len(found[i]):  
            noResult = noResult.append(dbA.ix[i])
        else:
            temp = dbB.ix[found[i]] # errors if found is empty     
            temp['nth query'] = i
            db = db.append(temp)        
    results = pd.merge(dbA, db, how='inner', left_index=True, right_on='nth query')
    results.to_csv(fname+'.csv', index=False, encoding='utf-8')
    noResult.to_csv(fname+' - no match.csv', index=False, encoding='utf-8')
    return results

def find_closest(dbA, dbB, colA='', colB='', n=5, cleaner=clean_text, fname='closest match'):
    '''
    Takes dbA terms and uses cosine matching to find dbB rows which closely match dbA terms.
    Default behavior: returns a maximum of five best matches.
    
    Input
    dfA: The database containing terms you're looking for.
    dfB: The database you're looking in for dbA's terms.
    colA: Columns which should be used in dbA. 
          Entries hould always be enclosed by brackets, e.g. ['id'] or ['id1', 'id2']
    colB: Columns which should be used in dbB. 
          Entries hould always be enclosed by brackets, e.g. ['id'] or ['id1', 'id2']
    n: The maximum number of closest matches reported per dbA row.
    regex: Set to True to use dbA search terms as regex patterns.
    cleaner: Desired cleaner, by default set to OnTrack's text cleaner. 
             Set to None if the DataFrame has already been cleaned.
    fname: The desired filename of the output csv files.
    
    Output
    Pandas DataFrame containing matches found.
    Two csv outputs: dfA-dfB matches and dfA rows that had no matches.
    '''
    dbA = pd.DataFrame(dbA, index=range(len(dbA)))
    dbB = pd.DataFrame(dbB, index=range(len(dbB)))
    if cleaner:        
        A = clean_subset(dbA, colA, cleaner)
        B = clean_subset(dbB, colB, cleaner)
    
    cos_match.set_corpus(B.values)
    found = A.apply(lambda x: cos_match.find(x, n))
    db = pd.DataFrame()
    for i in xrange(len(found)):
        if len(found[i]['indices']):  
            temp = dbB.ix[found[i]['indices']] # errors if found is empty  
            temp['score'] = found[i]['scores']
            temp['nth query'] = i
            db = pd.concat([db,temp], axis=0)
    results = pd.merge(dbA, db, how='left', left_index=True, right_on='nth query')
    results = results[results.score != 0]
    results.to_csv(fname+'.csv', index=False, encoding='utf-8')
    return results

if __name__ == '__main__':
    pass
