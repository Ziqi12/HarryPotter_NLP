# -*- coding: utf-8 -*-
#import nltk module
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.book import *
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
with open('E:\\Studying\\bu\\information structure with python\\project\\Harry Potter 5 - Order of the Phoenix.txt', 'r') as file1:
    file2 = file1.readlines()           #read file
def clean(file2):
    file3=[]              
    for i in file2:
        i = i.lower()     #The letter is unified into lowercase
        i = i.strip('\n')   #delete '\n'
        file3.append(i) 
    
    n='' 
    for i in file3:  
        n += ' ' + i
    
    tokenizer = RegexpTokenizer(r'\w+')   #remove punctuation
    n = tokenizer.tokenize(n)     #split sentences to singel word.
    
    stop_word = set(stopwords.words('english'))  #delete stop words
    word = []
    for w in n:
        if w not in stop_word:
            word.append(w)
    return word
clean(file2)

def split(word):
    a = []                         #split whole book accoding to its chapters
    for i in range(len(word)):
        if word[i].find('chapter') != -1:        #get the numbers of lines which contain 'CHAPTER'
            a.append(i) 
    indexes = [12, 13, 14, 15, 19, 20, 21, 22, 23, 37, 40, 41]
    for index in sorted(indexes, reverse=True):
        del a[index]
    
    book_list = []
    for i in range(len(a)):
        if i != len(a)-1:  
            chapter_list = word[int(a[i]):int(a[i+1])]
        else:
            chapter_list = word[int(a[-1]):]
        book_list.append(chapter_list)
split(word)

#sentiment analysis
def sentiment(book_list):
    total_scores =0
    y = []
    sid = SentimentIntensityAnalyzer()
    for i in book_list:
        count = 0
        for p in i:
            ss = sid.polarity_scores(p)
            scores = ss['pos']-ss['neg']
            if ss['neu'] == 1:
                count += 1    # count the number of neutral  words
        total_scores += scores
        average_scores = total_scores/(len(i)-count)
        y.append(average_scores)
    x = []
    for i in range(1,39):
        x.append(i)
    plt.figure()
    plt.plot(x, y)
    plt.show()
sentiment(book_list)
    
def frequency(word):
    fdist1 = FreqDist(word)     #get the frequency of words
    print(fdist1.most_common(20))
frequency(word)