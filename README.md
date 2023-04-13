# COSC320W-Project
COSC 320 – 001
Analysis of Algorithms
2022/2023 Winter Term 2




















Project Topic Number: #1
Keyword Replacement in a Corpus
 

Group Members: Shila Rahman, Linh Nguyen, Ravil Bigvava




Abstract:
In this milestone we implemented  our second improved algorithm. With the provided data set, we performed some test cases and generated plots with varying inputs showing different growth rates. We analyzed and compared the results with what we expected the algorithm to output. We ran into some problems with implementing the dictionary and splitting up the words of the tweet but were able to resolve the problems in the end. We are very happy with how we implemented our naive algorithm and with our graphs to show.

Implementation.
Our better algorithm implementation was done in python using data analysis tools such as pandas, and numpy. For our naive version we used array but in this implementation, we are using dictionaries. We used our previously broken down csv data of abbreviations and definitions (using method chaining) to make a dictionary of keys and values. Our tweet was split into an array of words which we iterated through and compared with the keys in our dictionary. If an abbreviation was found, it was replaced with the definition in the words array, using the index of our array. We also made sure to put punctuations back to appropriate places. Finally, we used the updated array of words to make an updated tweet and return it. We avoided using nested loops to reduce time complexity. We used sample cases in order to test our corner cases and specifics within our algorithm.
For the hashing algorithm, the implementation of the algorithm definitely has an affect on the constant value of the time complexity. An example would be the fact that we used a dictionary data structure to store and look up the slang words and this might have improved the time complexity compared to a linear search through a list. Additionally, the choice of string operations might have had an affect on the time complexity being a constant value. Overall, we can say that the algorithm has a reasonable and favorable performance, given the inputs as seen from the graph. However, as the input size increases- such as a million or more- the execution time will probably decrease. That means either we need to use a different, better hardware or optimize the algorithm

Results:
For our improved algorithm, our graph shows a linear plot with time complexity O(n), where n in our time complexity was the number of characters of our tweet input. We expected our graph to be linear from our conclusion made from the previous milestones. 
From the graphs below we can see that Hashing algorithm aka the improved algorithm run time is much faster than the naive algorithm and the improved algorithm is more lenient towards O(n) than the naive one
 

Unexpected Cases/Difficulties:
We had some difficulties implementing a dictionary (hashmap) rather than the array from the previous algorithm. We temporarily modified the naive algorithm to check if we could implement the dictionary instead of an array, and had to change to key-value pairs rather than rows. There were difficulties implementing the algorithm for punctuation exclusion when splitting the words up in the tweet. We ended up making an if and an else-if statement if the word had or did not have punctuation after, which fixed the issue.

 


Task Separation and Responsibilities. Who did what for this milestone? Explicitly mention the name of group members and their responsibilities. 
Abstract: Ravil
Dataset: Shila, Linh
Implementation Shila, Linh, Ravil
Results: Shila, Linh, Ravil
Unexpected Cases/Difficulties: Shila, Linh
Additional information: https://github.com/linhnnk/COSC320W-Project 

**The "merged_csv_dataset_forTweet" database is a small overview of the complete database we experiment from. Here is the Google Drive link for the complete database:** https://drive.google.com/file/d/1UxrdenkiNUOZFc-0fm0VoYZuEiU-0mqd/view?usp=sharing 

