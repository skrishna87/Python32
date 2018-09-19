import firstdef

filename= input('enter the filename: ')
with open(filename) as t:
	text = t.read()

print(count_char(text,'l'))