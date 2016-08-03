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
#### 1. Prepare text query.
```python
from text_cleaners import clean_text

query = "Rehabilitation/Reconstruction/Removal of Gravel on Bulacan, Road. North km+1993-km+384"
coreQuery = clean_text(query)
print coreQuery

>>> "rehabilit reconstruct remov gravel bulacan road north km 1993 km 384"
```
#### 2. Create String Searcher and Cosine Matcher objects.
```python
from string_searcher import StringSearcher
from cosine_matcher import CosineMatcher

str_search = StringSearcher()
cos_match = CosineMatcher()
```
#### 3. Set search space corpus.
```python
str_search.set_corpus('path-to-file.csv')
cos_match.train('path-to-file.csv', train_on='column_name')
```
#### 4. Find records with exact, case-insensitive substring matches from a specific column in the corpus.
```python
matches1 = str_search.find('Query String', on='column_name')
print matches1
```
#### 5. Find top 5 records with the highest cosine similarity score.
```python
matches2 = cos_match.check_matches(clean_query, 5)
print matches2
```

### Motivation ###

OnTrack tackles the problem of huge numbers of unmatched, messy records across government data silos by automating the matching process. In half an hour, the current version of OnTrack is able to accurately shortlist 85% of the records manually matched in 15 work-months.

Read more about our pilot test [here](http://stories.thinkingmachin.es/ontrackph/).

### Contributors ###

Stephanie Sy
Ray Dino
Jose Araneta

### Contact ###
This is a work in progress. Please send comments and questions to `hello@thinkingmachin.es`.
