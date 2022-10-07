#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=1222

n=var_int%10 #4
s1=(n+1)%2 #1

var_int=var_int//10 #123
n=var_int%10 #3
s2=(n+1)%2 #0

var_int=var_int//10 #12
n=var_int%10 #2
s3=(n+1)%2 #1

var_int=var_int//10 #1
n = var_int
s4=(n+1)%2#0
print(s1+s2+s3+s4)