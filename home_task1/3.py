import sys
import argparse

def F_new(N, pr=False):
    a1 = 0
    a2 = 1
    summa = 0
    lst = ['0']
    for i in range(N):
        summa = a1 + a2
        a1 = a2
        a2 = summa
        lst.append(str(a1))
    if pr:
        return ' '.join(lst)
    else:
        return a1



def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('N', type = int)
    parser.add_argument('-a', '--all', action='store_const', const=True)
    parser.add_argument('-f', '---file', type=argparse.FileType(mode='w', encoding=None, errors=None))

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

if namespace.file:
    if namespace.all:
        namespace.file.write(F_new(namespace.N, True))
    else:
        namespace.file.write(F_new(namespace.N))
else:
    if namespace.all:
        print(F_new(namespace.N, True))
    else:
        print(F_new(namespace.N))

