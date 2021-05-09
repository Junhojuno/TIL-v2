import argparse

# without '--' or '-', the order of arguments are important.
parser = argparse.ArgumentParser()
parser.add_argument('a', type=int, help='the base')
parser.add_argument('x', type=int, help='the exponent')
parser.add_argument('-v', '--verbose', action='store_true', help="increase output verbosity")
args = parser.parse_args()
print('args -> type : {}, value : {}'.format(type(args), args))
result = args.a ** args.x

if args.verbose:
    print(f'{args.a} to the power {args.x} equals {result}')

"""
$ python 03_argparse_advanced.py 2 4 -v
>>> 2 to the power 4 equals 16
"""