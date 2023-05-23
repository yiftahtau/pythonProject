# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def rand_fun (m, n):
    return [randint(1,n) for x in range(m)]


def experiment (m,n, t, K):
    success = 0
    total_valid = 0
    while total_valid < K:
        x = 1
        y = randint(1,m)
        succ = True
        for i in range(t):
            F = randint(1,n) # F = n means F(x) = F(y)
            if x != y and F < n:
                succ = False
                break
        if succ:
            total_valid += 1
            if x != y:
                success += 1
    return (100.0 * success) / K

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    M = 1000
    N = 10
    K = 1e5
    for i in range (1, 1000):
        print (i, experiment(M, N, i, K))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
