
import sys

print(bool(list(filter(lambda x: x == '0', sys.stdin.read().split()))))
