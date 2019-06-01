# n is the number of space-seperated integers.
# Create a tuple t of those n integers.
# Then compute and print the result of hash(t)
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
