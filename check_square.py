import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', type = str,
					help = "Initialize input varible. Ex.: -v '((((((2, 3))))))))' ")

args = parser.parse_args()

s = args.s

s = s+(s[~0]*(s.count(s[0])-s.count(s[~0]))) if s.count(s[0])>s.count(s[~0]) else s[0]*(s.count(s[~0])-s.count(s[0]))+s

print(s)
