# COSC320W-Project
COSC 320 – 001
Analysis of Algorithms
2022/2023 Winter Term 2




















Project Topic Number: #1
Keyword Replacement in a Corpus
 

Group Members: Shila Rahman, Linh Nguyen, Ravil Bigvava




Abstract:
In this milestone, we implemented and analysed our naive algorithm. With the provided data set in class, we performed various test cases and plots that showed the growth as the size of the input changed. We analyzed and compared the results with what we expected the algorithm’s output to be. We ran into a couple of issues initially, however we are very happy with how we implemented our naive algorithm and our resulting graphs. 

Dataset:
We used the following datasets: slang_database.csv includes all the abbreviations and their definitions, and the rest of the dataset includes tweets that we will be searching through. We decided to only use merged_csv_dataset_forTweet.csv for the tweets based on their similar string format, and slang_database.csv for the abbreviations. Along with this we added some example sentences that contain slangs in order to fully test our program to see if the replace works.

Implementation.
We implemented and analysed the data set using python in jupter notebook using tools such as pandas, and numpy. We broke down the data in order to be used within our implementation as arrays. This first milestone is the naive implementation of taking the tweet (input) and breaking it apart as an array to be processed. 
We used method chaining in order to clean up our data and then implemented our algorithm into a python notebook. From there we used sample cases in order to test our corner cases and specifics within our algorithm. We made a plot of running time vs input size and compared our expectations based on the big O notation of the algorithm.

Results.
For our naive algorithm, our graph is linear showing that our function runs in O(n+m), where n is the length of the tweet (input) and m is the number of rows in the slang data.
We saw a very linear growth within our graph and thus we plotted our big O running time of O(m+n) against the damped slope of our functions running time. (The time complexity is proportional to both factors n and m, as each row in the dataset, the specific abbreviation is searched through in the given tweet and replaced with the appropriate full version- if found.) This is expected as we have a very linear growth of execution time as the input size increases and accounting for constant values and the big O notation, it seems to be very similar. The O(m+n) graph contains no linear constants and thus is very low in running time but we can compare the main slopes to see they are similar. (The actual execution time is higher than the time complexity because of various factors such as the choice of data structure and use of different implementations.) The choice of data structure could have affected this as we used a column reading data within our implementation which could have been different than the planned list values. For example, if the data had been sorted and then indexed or if we had used a has table or a tree to store the data, the running time of the algorithm would have been reduced and hence, resulting in the increased performance of the algorithm. We have included the screenshots of the graph for reference below. 

Unexpected Cases/Difficulties:
There were a couple of issues we ran into while implementing our analysis. We had to reset our kernels multiple times as errors would occur, such as ModuleNotFoundError. 
In the case of our algorithm, when there were abbreviations that were found inside of other words, the program would end up replacing part of the word with the abbreviation value. To fix this we had to ensure that punctuation and spaces were accounted for if it appears right before a found abbreviation (if the character found before an abbreviation is alphabetic, then it’s just part of another word).
 


Task Separation and Responsibilities. Who did what for this milestone? Explicitly mention the name of group members and their responsibilities. 
Abstract: Ravil
Dataset: Shila, Linh
Implementation Shila, Linh, Ravil
Results: Shila, Linh, Ravil
Unexpected Cases/Difficulties: Shila, Linh
Additional information: https://github.com/linhnnk/COSC320W-Project 

** The "merged_csv_dataset_forTweet" database is a small overview of the complete database we experiment from. Here is the Google Drive link for the complete database: https://drive.google.com/file/d/1UxrdenkiNUOZFc-0fm0VoYZuEiU-0mqd/view?usp=sharing 

