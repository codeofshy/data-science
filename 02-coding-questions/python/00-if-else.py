# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

n = int(input().strip())

if n%2 == 1:
    print('Weird')
elif (n%2 == 0) and n in range(2, 6):
    print('Not Weird')
elif (n%2 == 0) and n in range(5, 20):
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')