import sys
import argparse

def F(N):
    if N == 0:
        Fn = 0
    elif N == 1:
        Fn = 1
    else:
        Fn = F(N-1) + F(N-2)
    return Fn

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('N', type = int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

print(F(namespace.N))



