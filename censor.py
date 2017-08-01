import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", type=str, help= "specify the file.txt ex.: -f 'file.txt'")

args = parser.parse_args()

file = args.file

global word

def replace_char(text):
	for char in text:
		if char in '.,:!?()<>"':
			text = text.replace(char, ' '+char+' ')
	return text

def place_char(text):
	for char in text:
		if char in '.,:!?()<>"':
			s = ' '+ char+' '
			text = text.replace(s, char)
	return text
	
with open(file, 'r') as f:
	text = replace_char(f.read())
	count = 0
	
	for w in set(text.split()):
		if len(w) >= 4 and text.split().count(w) > count:
			count = text.split().count(w)
			word = w

	text = text.replace(word+' ', '*'*len(word)+' ')
	text = text.replace(word+'\n', '*'*len(word)+'\n')
	text = place_char(text)

	with open('out.txt', 'w') as out:
		out.write(text)