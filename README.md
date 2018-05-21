# OnTrack #

Given a piece of text and a database of possible matches, OnTrack uses word vectorization and cosine matching to find the closest match despite different formatting conventions.

This repo contains a collection of text cleaner scripts and matcher classes.

### Documentation ###
See the wiki for the [full documentation](https://github.com/thinkingmachines/ontrack/wiki).

### Dependencies ###
* numpy
* pandas
* nltk
* scipy>=0.16.1
* scikit-learn

Dependencies will be installed during setup.

### Installation ###

`pip install <git+http://this-repository.git>`

Not sure what to do? More detailed instructions [here](https://github.com/thinkingmachines/ontrack/wiki/Installation).

### Usage ###

This example will find records matching "Rehabilitation/Reconstruction/Removal of Gravel on Bulacan, Road. North km+1993-km+384" in the database **path-to-file.csv**.
#### 1. Prepare your query.
OnTrack accepts the following as input:

 - list of strings
 - pandas DataFrame
 - csv filepath, accessed using `read()`
```python
db_A1 = ['Laoag', 'Construction'] # two separate queries
db_A2 = pd.DataFrame([['Laoag', 'Construction', 'unhelpful column'],
                      ['Bohol', 'Rehabilitation', 'unhelpful column'],
                      ['Quezon City', 'Construction', 'unhelpful column']]) # three rows/queries

df_B = read('small.csv')
```
#### 2. Find records with exact, case-insensitive substring matches from a specific column in the corpus.
```python
matches1 = find_exact(db_A1, dbB)

matches2 = find_exact(db_A2, dbB, colA=[0,1], colB=['contract_desc', 'implementing_office'], fname='exact2') # the result will be outputted in a csv with the default name 'exact matches.csv'
```
For `matches1`,  the result will be outputted in a csv with the default name 'exact matches.csv'
For `matches2`, since fname was specified, results will be saved in 'exact2.csv'. Filling in the parameters `colA` and `colB` means specific columns are selected; 0 and 1 are the column number of the helpful columns in `db_A2`, contract_desc and   implementing_office are the important headers in `db_B` ('small.csv').

If colA and colB are not specified, `find_exact` will use all columns.

#### 3. Find top 5 records with the highest cosine similarity score.
```python
matches1 = find_closest(db_A1, df_B)

matches2 = find_closest(db_A2, df_B, n=10, cleaner=None)
```
The result from the first line will be saved in 'closest match.csv'.

Since no file name was specified, 'closest match.csv' will be overwritten by the result of the second line. You can choose to increase/decrease the number of best matches displayed (default: 5) by changing n. Setting cleaner to None means that either the input databases were precleaned, or you choose not to keep them in their raw format.

More detailed instructions are available in the [wiki](https://github.com/thinkingmachines/ontrack/wiki).

### Motivation ###

OnTrack tackles the problem of huge numbers of unmatched, messy records across government data silos by automating the matching process. In half an hour, the current version of OnTrack is able to accurately shortlist 85% of the records manually matched in 15 work-months.

Read more about our pilot test [here](http://stories.thinkingmachin.es/ontrackph/).

### Contributors ###

- Stephanie Sy
- Ray Dino
- Jose Araneta
- Gilian Uy

### Contact ###
This is a work in progress. Please send comments and questions to `hello@thinkingmachin.es`.
