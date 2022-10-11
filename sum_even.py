var_int=0000
sum_even=0
n=var_int%10 #4
sum_even+=(n+1)%2 *n #1

var_int=var_int//10 #123
n=var_int%10 #3
sum_even+=(n+1)%2*n #0

var_int=var_int//10 #12
n=var_int%10 #2
sum_even+=(n+1)%2*n #1

var_int=var_int//10 #1
n = var_int
sum_even+=(n+1)%2*n#0
print(sum_even)
