"""
Cleans text in preparation for analysis by string searcher and cosine matcher.
"""

from nltk.stem.porter import PorterStemmer

stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'])
stemmer = PorterStemmer()

def clean_punctuation(text):
    """ Converts to lowercase and replaces all non-alphanumeric with spaces. """
    no_punc = ''.join([w if w.isalnum() else ' ' for w in text.lower()])
    return no_punc.split()

def remove_stop(tokens):
    """ Removes stopwords, e.g. 'the', 'at', 'on', etc. """
    no_stopwords = [word for word in tokens if not word in stopwords]
    return no_stopwords

def stem(tokens):
    """ Applies PorterStemmer to the tokens. (https://en.wikipedia.org/wiki/Stemming) """
    stemmed = [stemmer.stem(word) for word in tokens]
    return stemmed

def stringify(tokens):
    """ Turns the tokens back into a string. """
    return ' '.join(tokens) # remove the last space

def clean_tokens(text):
    """ Single function that combines stopping, stemming, and cleaning punctuation """
    return stringify(stem(remove_stop(clean_punctuation(text))))

if __name__ == '__main__':
    """ sample usage """
    t = "Rehabilitation/Reconstruction/Removal of Gravel on Bulacan, Road. North km+1993-km+384"
    print t

    st = clean_tokens(t)
    print st