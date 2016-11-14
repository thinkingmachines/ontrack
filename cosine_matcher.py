'''

This class uses scikit-learn to vectorize a corpus of text and
allow comparison of new documents to the existing corpus matrix

'''

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class CosineMatcher(object):
    def __init__(self, encoding='utf-8', analyzer='word', ngram_range=(1,1), \
                 min_df = 1, max_df = 0.8, use_idf=True):
        '''
        Defaults

        encoding=utf-8
        min_df = 1 => only include token if it appears in at least 1 document
        max_df = 0.8 => drop the token if it appears in over 80pc of the docs

        We aren't using TfidfVectorizer's built-in tokenizer and stop/stem
        functionality because we have chosen to pre-process that text and will
        be running other types of matching on the stop/stemmed text.
        '''
        self.match_corpus = None
        self.matrix = None
        self.vectorizer = TfidfVectorizer(encoding=encoding, analyzer=analyzer,\
            ngram_range=ngram_range, min_df=min_df, max_df=max_df,\
            use_idf=use_idf)


    def set_corpus(self, corpus):
        '''
        Fit the training corpus to the TF-IDF Vectorizer.

        corpus: A hashable object containing the searchspace strings
        '''

#        self.match_corpus = corpus[corpus.notnull()]
        self.matrix = self.vectorizer.fit_transform(corpus)


    def find(self, target, n_best = 5):
        '''
        target is a string
        n_best is the number of matches we want returned

        Transforms target query into vector form
        Calculates dot product across tfidf matrix
        Returns a list of the n_best matches for the target
        '''

        vectorized_query = self.vectorizer.transform([target])
        cosine_sim = linear_kernel(vectorized_query, self.matrix).flatten()
        n_best_matches_indices = cosine_sim.argsort()[:-n_best-1:-1]
        return {'indices': n_best_matches_indices,
                'scores': cosine_sim[n_best_matches_indices]}

if __name__ == '__main__':
    pass