To run the python file for Q7 in the uvic linux server:
python3 ParameterEst.py

The program asks you to input a proper value for head probability; it needs to be greater than 0
and smaller than 1.

Once the input is accepted, it will output the estimated value and normalized estimation error.
To use the program for the e part of Question 7, you can change the value at line 22 and 27

For example,
Simulate 10000 tosses
line 22 	while toss < 10000:
line 27		estimated = known_head/10000

Simulate 20000 tosses
line 22 	while toss < 20000:
line 27		estimated = known_head/20000