'''


T

IMPORTANT: Requires several nltk packages.
Install by running
import nltk
nltk.download()

Need porter stemmer, and the stopwords corpus
'''


import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords
from string import maketrans

stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'])

def clean_punctuation(text):
    #fixed_slashes = text.replace('/',' ')
    fixed_slashes = text
    custom_punc = '!"#$%&\'()*,.:;<=>?@[\]^_`{|}-~'
    translate_table = maketrans(custom_punc, ''.join([' ' for i in range(
        0, len(custom_punc))]))
    try:
        desc = fixed_slashes.lower().translate(translate_table)
        return desc
    except TypeError:
        print('TypeError: Translate function does not accept unicode.')

def remove_stop(text):
    '''
    Removes stopwords
    '''
    no_stopwords = [word for word in text.split() if not word in stopwords]
    return no_stopwords

def stem(tokens):
    '''
    Applies PorterStemmer to the tokens
    '''
    stemmed = []
    for item in tokens:
        stemmed.append(PorterStemmer().stem(item))
    return stemmed

def stringify(tokens):
    '''
    Turns the tokens back into a string. Seems unnecessary.
    Come back and fix this!
    '''
    s = ''
    for token in tokens:
        s += token
        s += ' '
    return s.rstrip() # remove the last space

def clean_tokens(text):
    '''
    Single function that combines stopping, stemming, and cleaning punctuation
    '''
    return ' '.join(stem(remove_stop(clean_punctuation(text))))


if __name__ == '__main__':
    '''
    sample usage
    '''
    t = "Rehabilitation/Reconstruction/Removal of Gravel on Bulacan, Road. North km+1993-km+384"
    print t

    st = clean_tokens(t)
    print st

    print stringify(st)