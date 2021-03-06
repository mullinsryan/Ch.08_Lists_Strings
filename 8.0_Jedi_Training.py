#Sign your name: Ryan Mullins

'''
1.)
Write a single program that takes any of the three lists, and prints the average. 
Use the len function. There is a sum function I haven't told you about. 
Don't use that. Sum the numbers individually as shown in the chapter. 
Also, a common mistake is to calculate the average each time through the loop 
to add the numbers. Finish adding the numbers before you divide.
'''
a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
b_list = [4,15,2,7,8,3,1,10,9]
c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]

list = int(input("To average lists a, b, or c, type 1, 2, or 3 respectively: "))
if list == 1:
    sum = 0
    for a in a_list:
        sum += a
    average = sum/len(a_list)
    print(average)
elif list == 2:
    sum = 0
    for b in b_list:
        sum += b
    average = sum / len(b_list)
    print(average)
else:
    sum = 0
    for c in c_list:
        sum += c
    average = sum / len(c_list)
    print(average)


'''
2.) Write a program that will strip the username (whatever is in front of the @ symbol)
from any e-mail address and print it. First ask the user for their e-mail address.
'''
email = input("Email: ")
username = ''
for c in email:
    if c != "@":
        username = username + c
    else:
        print(username)




'''
TEXT FORMATTING:
3.) Make following program output the following:
     
     Score:          41,237
     High score:  1,023,407
     
     Do not use any plus sign (+) in your code.
     You should only have two double quotes in each print statement.
     '''
score = 41237
highscore = 1023407


print(f"Score: {score:>13,}")
print(f"Highscore: {highscore:>8,}")



