#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=1222

n=var_int%10 #4
a1=(n+1)%2 #1

var_int=var_int//10 #123
n=var_int%10 #3
a2=(n+1)%2 #0

var_int=var_int//10 #12
n=var_int%10 #2
a3=(n+1)%2 #1

var_int=var_int//10 #1
n = var_int
a4=(n+1)%2#0
answer=a1+a2+a3+a4
print(answer)