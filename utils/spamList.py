#!/usr/bin/env python3

def addAnd(spam):
	spam[len(spam)-1] = 'and ' +spam[len(spam)-1]
	outStr = ' '.join(spam)
	return outStr

spam1 = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 'bananas', 'tofu', 'cats','apples', 'bananas', 'tofu', 'cats']
spam3 = ['apples', 'bananas', 'tofu', 'cats','apples', 'bananas', 'tofu', 'cats', 'catssss']


print(addAnd(spam1))
print(addAnd(spam2))
print(addAnd(spam3))