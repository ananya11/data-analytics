# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 21:35:57 2014

@author: ananya
"""

from time import time
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='all')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cross_validation
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


kf = cross_validation.KFold(len(newsgroups_train.data),5,shuffle=True, 
                            random_state=2000)
vectorizer=TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')                            

feat = [10, 100, 1000,5000, 10000, 50000]


for features in feat :
    
    print 'No of features : ', features
    for train,test  in kf:                             
        # split a training set and a test set
        X_train = [newsgroups_train.data[x] for x in train]
        y_train = [newsgroups_train.target[x] for x in train]
        
        X_test = [newsgroups_train.data[x] for x in test]
        y_test = [newsgroups_train.target[x] for x in test]
        
    #    print("Extracting features from the train dataset")    
        X_train=vectorizer.fit_transform(X_train)
    #    print("Extracting features from the test dataset")    
        X_test=vectorizer.transform(X_test)
        
    #    print("Extracting best features from the train dataset using chi2") 
        ch2=SelectKBest(chi2, k=features)
        X_train=ch2.fit_transform(X_train,y_train)
    #    print("Extracting best features from the test dataset using chi2") 
        X_test = ch2.transform(X_test)
        
        print '-------Multinomial Naive Bayes Classifier--------' 
        t0=time()                        
        clf=MultinomialNB()
        clf.fit(X_train,y_train)
        pred=clf.predict(X_test)
        
        duration=time()-t0
        print 'duration: ' , duration        
        accuracy = metrics.accuracy_score(y_test,pred)
        print("accuracy:   %0.3f" % accuracy)
        precision = metrics.precision_score(y_test,pred)
        print("precision:   %0.3f" % precision)
        recall = metrics.recall_score(y_test,pred)
        print("recall:   %0.3f" % recall)

        print
        print '---------Decisiontree----------'    
        t0=time() 
        clf=DecisionTreeClassifier(max_depth=5)
        clf.fit(X_train.toarray(),y_train)
        pred=clf.predict(X_test.toarray())

        duration=time()-t0
        print 'duration: ' , duration        
        accuracy = metrics.accuracy_score(y_test,pred)
        print("accuracy:   %0.3f" % accuracy)
        precision = metrics.precision_score(y_test,pred)
        print("precision:   %0.3f" % precision)
        recall = metrics.recall_score(y_test,pred)
        print("recall:   %0.3f" % recall)

        print
        print '-------KNeighborsClassifier k=9 ------'
    
        t0=time() 
        clf = KNeighborsClassifier(n_neighbors=9)
        
        clf.fit(X_train,y_train)
        pred=clf.predict(X_test)

        duration=time()-t0
        print 'duration: ' , duration        
        accuracy = metrics.accuracy_score(y_test,pred)
        print("accuracy:   %0.3f" % accuracy)
        precision = metrics.precision_score(y_test,pred)
        print("precision:   %0.3f" % precision)
        recall = metrics.recall_score(y_test,pred)
        print("recall:   %0.3f" % recall)

        print
        print '-------KNeighborsClassifier k=5 ------'
    
        t0=time() 
        clf = KNeighborsClassifier(n_neighbors=5)
        clf.fit(X_train,y_train)
        pred=clf.predict(X_test)
        
        duration=time()-t0
        print 'duration: ' , duration        
        accuracy = metrics.accuracy_score(y_test,pred)
        print("accuracy:   %0.3f" % accuracy)
        precision = metrics.precision_score(y_test,pred)
        print("precision:   %0.3f" % precision)
        recall = metrics.recall_score(y_test,pred)
        print("recall:   %0.3f" % recall)
        
        print
        print '-------KNeighborsClassifier k=1 ------'
    
        t0=time() 
        clf = KNeighborsClassifier(n_neighbors=1)
        clf.fit(X_train,y_train)
        pred=clf.predict(X_test)
        
        duration=time()-t0
        print 'duration: ' , duration        
        accuracy = metrics.accuracy_score(y_test,pred)
        print("accuracy:   %0.3f" % accuracy)
        precision = metrics.precision_score(y_test,pred)
        print("precision:   %0.3f" % precision)
        recall = metrics.recall_score(y_test,pred)
        print("recall:   %0.3f" % recall)
        
        print
        print '##################################################################' 
        print
    

