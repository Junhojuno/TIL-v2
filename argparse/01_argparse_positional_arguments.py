import argparse

# without '--' or '-', the order of arguments are important.
parser = argparse.ArgumentParser()
parser.add_argument('echo', help="echo the string you use here")
parser.add_argument('square', type=int, help="display a square of a given number")
args = parser.parse_args()
print(args.echo)
print(args.square ** 2)


"""
$ python 01_argparse.py what 2
>>> what
    4

$ python 01_argparse.py 2 what
>>> usage: 01_argparse.py [-h] echo square
    01_argparse.py: error: argument square: invalid int value: 'what'
"""