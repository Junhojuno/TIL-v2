"""(short)optional arguments"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true', help="increase output verbosity")
args = parser.parse_args()

if args.verbose:
    print('verbosity turned on.')

"""
$ python 02_argparse_short_optional_arguments.py -v
>>> verbosity turned on.
"""