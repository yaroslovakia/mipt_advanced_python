import argparse

def fibo(n, pr=False):
	a = 0
	b = 1
	l = []
	for i in range(n):
		a = b
		b = a + b
		l.append(str(a))
	if pr == True:
		return ' '.join(l)
	else:
		return a


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', type = int)
    parser.add_argument('-a','--all', action='store_const', const=True)
    parser.add_argument ('-f', '--file','--filename', type=argparse.FileType(mode='w', encoding=None, errors=None))
    return parser

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    
    print(args)
        
    if args.file:
        if args.all == True:
            args.file.write(fibo(args.num, True))
        else:
            args.file.write(fibo(args.num))
    else:
        if args.all == True:
            fibo(args.num, True)
        else:
            fibo(args.num)
