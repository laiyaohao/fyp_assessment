# AISG - FOE FYP Technical Assessment (Apr 2020)

### Question 1

###### The following will be an explanation of my algorithm

My thinking of the algorithm goes like this:

I first thought of the worst case scenerio: which is the case where 999999 is the input. This means that
the supposed output will be "Nine Hundred And Ninety Nine Thousand, Nine Hundred And Ninety Nine". I thought there is repeated occurance of the "Nine Hundred and Ninety Nine" and as such, I was thinking of thinking splitting the thousands and the hundreds, if both of them exists and then letting them go through a similar function to get the 'Hundred' number out. This means that the function will accept inputs from 0 to 999 inclusive.

Since the input is interger class, I will need to transform it to a string class to identify the number of digits. From there, I further disect the requirements of this function. I realized the input may not be 3 digits; it could be 2 or 1 digit, and thus, I created a dictionary that represents all the english equilivalent of the digits, like zero to nine, ten to nineteen and twenty and its multiples of 10 (I do not need to create a value for a number above 20, like 21, because i can use the value 20 and add the value 1 onto it). 

After defining all the dictionary, I will first define the 2 digit function, because the 3 digit function can also make use of the 2 digit function. So for the 2 digit function, I will first take a look whether the length is 1. If it is one, just match the input with the key and retrieve the value. If the length is not 1, then I will check whether the first digit is 1, because from 10 to 19, there are special english names for them. If the first digit is 1, then i will match the entire input with the key in the dictionary and retrieve the value. Lastly, if it is not the above cases, then i will just match the first digit with the dictionary of twenty and its multiples, and match the second digit with the single digit dictionary.

For the 3 digit function, I just need to match the 1st digit with the single digit dictionary, add the string "Hundred" and then use the 2 digit function to check the remaining 2 digits. Now for inputs more than 3 digits, I will just need to split the input into 2 groups, one of them being the last 3 digits, and the other being the rest of the digits. I just need to apply the function twice and I should be able to get the answer. However, there is a problem which I have not considered, which is what if the length rest of the digits is not 3? This will certainly run into problems.

Thus, I decided to put a layer of abstraction, in between the entire input and the 2 and 3 digit function, so as to 'point' the correct function according to correct number of digits. From there, I will just need to take care of the minor details of the spacing and so on. One thing to note is that I put 0 as one of the base case, instead of in the dictionary, because if 0 is not 'alone' i.e. it is inclusive
in between the numbers, then the word zero will be in 'read' out. As such, in the dictionary value, key 0 is paired with an empty string.

###### The following will be an explaination of the test cases I have put in

The first thing I test in the test cases are the limits, which is 0 and 999999. I next test numbers which have many 0s at the back, to see if 'zero' is printed out. Following that, I test numbers which have no 0s, to see if there are any spacing / comma issues. As one of the requirements is to correctly put the commas 'not "and" after the thousands, before the hundered if both exists', two of the test cases is to put numbers that don't have 'and' in the thousand, and check if there are commas. For the last test cases, I put numbers that have 0s in between, so as to see whether 'zero' appear or not.

###### Instrucions to run the srcipts:
Both files can be open directly for examination of the code and the test cases. For you to input a number, just uncomment the line of code that contains 'user_input()' and re-run the script.

### Question 2

###### Explain the pipeline design and its usage
I used Tensorflow Estimator to build the pipeline. I first took out the target, 'class' so that the training will not be biased with the target. Then, I use the train_test_split function to split the data into 2: one for training of the model and the other for testing. I extract the column names, which is crucial for the use of the feature column in the estimator LinearClassifier method, which helps me build the logistic regrerssion model.

###### Explain your choice of model
I have chosen to use the logistic regression model as it is a baseline for other more complex algorithms.

###### Provide an evaluation of the model developed
The model can unfortunately only around 55 (+- 5)% correct on the credit card csv file, and i think one of the main improvements that can be made is to reduce the repetitions in the 'Amount' column, which I think can somehow make the predictions more accurate. Another improvements that can be made is to list different combinations of the abstracted features to train the model, but this would increase the amount of time needed.

###### Instructions to run the scripts
There are two files in the mlp folder, namely module_script and test_script. Ensure that the csv file you want to test is in the same folder. In the test_script file, enter the file name in the tf_estimator function, uncomment that line and run the script.