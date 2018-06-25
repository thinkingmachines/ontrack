# OnTrack #

OnTrack tackles the problem of huge numbers of unmatched, messy records across government data silos by using word vectorization and cosine matching to identify the best possible matches for any government record.

Read more about our pilot test here.

This repo contains a collection of text cleaner scripts and matcher classes.

### Dependencies ###
* numpy
* pandas
* nltk
* scipy==0.16.1
* scikit-learn

Required NLTK corpus:
- stopwords
- punkt

Dependencies will be installed during setup.

### Installation ###

`pip install <git+http://this-repository.git>`

### Usage ###

1.Create String Searcher and Cosine Matcher objects.
```
from string_searcher import StringSearcher
from cosine_matcher import CosineMatcher

str_search = StringSearcher()
cos_match = CosineMatcher()
```

2.Set search space corpus.
```
str_search.set_corpus('path-to-file.csv')
cos_match.train('path-to-file.csv', train_on='column_name')
```

3.Find records with exact, case-insensitive substring matches from a specific column in the corpus.
```
matches = str_search.find('Query String', on='column_name')
```

4.Prepare text query.
```
from text_cleaners import clean_tokens, stringify

clean_query = stringify(clean_tokens('Query String'))
```

5.Find top 5 records with the highest cosine similarity score.
```
matches = cos_match.check_matches(clean_query, 5)
```

### Contact ###

This is a work in progress. Please send comments and questions to `hello@thinkingmachin.es`.