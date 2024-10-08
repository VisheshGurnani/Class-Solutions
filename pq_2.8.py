#what will be the output of the code snippet below:

for index in range(50,30,-3):
    print(index, end=" ")
#it prints the following numbers: 50 47 44 41 38 35 32
# this is because the skip() value is -3 which means 50 gets decremented 3 times  to get 47, 47 gets decremented 3 times to get 44 and so on. 
# this goes on till 32 ONLY since the range ends at 30
 