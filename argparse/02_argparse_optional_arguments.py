import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', help="increase output verbosity")
parser.add_argument('--verbose', action='store_true', help="increase output verbosity")
args = parser.parse_args()

if args.verbosity:
    print('verbosity turned on.')
    
print(args.verbose)


"""
$ python 02_argparse_optional_arguments.py --verbosity something --verbose
>>> verbosity turned on.
    True
"""