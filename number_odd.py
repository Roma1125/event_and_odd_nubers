#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=1222
sum=0
n=var_int%10 #4
sum+=(n)%2 #1

var_int=var_int//10 #123
n=var_int%10 #3
sum+=(n)%2 #0

var_int=var_int//10 #12
n=var_int%10 #2
sum+=(n)%2 #1

var_int=var_int//10 #1
n = var_int
sum+=(n)%2#0
print(sum)