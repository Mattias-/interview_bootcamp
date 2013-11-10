import sys

while(True):
    row = sys.stdin.readline().rstrip()
    if row == '42':
        break
    else:
        print row
