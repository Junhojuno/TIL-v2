import argparse

# add_argument() : another arguments
parser = argparse.ArgumentParser()
parser.add_argument('--list', action='append', default=[1,2,3,4])
parser.add_argument('--ver', dest='version', type=str, default='first')
args = parser.parse_args()

print(type(args.list), args.list)
print(type(args.version), args.version)