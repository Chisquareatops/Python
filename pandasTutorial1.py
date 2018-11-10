import pandas as pd

reviews = pd.read_csv("ign.csv")

print(reviews.head()) #print first n rows of datafram (Default 5)
print(reviews.shape) #see how many rows and columns are in reviews

print(reviews.iloc[0:5,:]) #does the same thing as reviews.head()

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

reviews = reviews.iloc[:,1:] #remove first col
print(reviews.head())

reviews.loc[0:5,:] #display rows of reviews using loc mathod; looks like prev method bc row labels match positions

some_reviews = reviews.iloc[10:20,] #make a named subset of reviews
print(some_reviews.head())
# print(some_reviews.loc[9:21,:]) #now gives error
print(reviews.loc[:5,"score"])

print(reviews["score"]) #easiest way to retrieve a single whol col
print(reviews[["score", "release_year"]]) #also works for lists of cols
print(type(reviews["score"])) #verify that a single col is a 'series'

#SERIES
s1 = pd.Series([1,2]) #create a series manually
print(s1)
s2 = pd.Series(["Boris Yeltsin", "Mikhail Gorbachev"]) #a series of String objects
print(s2)

#DATA FRAMES
print(pd.DataFrame([s1,s2])) #make data frame by passing series objects
frame = pd.DataFrame( #make same data frame by passing list of lists
    [
        [1,2],
        ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"], #specify row names
    columns=["column1", "column2"] #specify col names
)
print(frame)

#USEFUL SERIES METHODS
print(reviews["score"].mean())
print(reviews.mean()) #by default will find mean of all cols

#modify axis keyword argument to mean
print(reviews.mean(axis=0)) #0 is default; compute mean of ea col
print(reviews.mean(axis=1)) #1 computes mean of ea row

print(reviews.corr()) #look for cols that correlate with score

reviews["score"]/2 #diviing vals in score col compresses scoring scale

#tutorial link:
#https://www.dataquest.io/blog/pandas-python-tutorial/
#data set ink:
#https://www.kaggle.com/egrinstein/20-years-of-games