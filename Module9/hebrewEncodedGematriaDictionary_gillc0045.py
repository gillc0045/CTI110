hebrewEncodedDict = {
    "\xd7\x90" : 1,
    "\xd7\x91" : 2,
    "\xd7\x92" : 3,
    "\xd7\x93" : 4,
    "\xd7\x94" : 5,
    "\xd7\x95" : 6,
    "\xd7\x96" : 7,
    "\xd7\x97" : 8,
    "\xd7\x98" : 9,
    "\xd7\x99" : 10,
    "\xd7\x9a" : 500,
    "\xd7\x9b" : 20,
    "\xd7\x9c" : 30,
    "\xd7\x9d" : 600,
    "\xd7\x9e" : 40,
    "\xd7\x9f" : 700,
    "\xd7\xa0" : 50,
    "\xd7\xa1" : 60,
    "\xd7\xa2" : 70,
    "\xd7\xa3" : 800,
    "\xd7\xa4" : 80,
    "\xd7\xa5" : 900,
    "\xd7\xa6" : 90,
    "\xd7\xa7" : 100,
    "\xd7\xa8" : 200,
    "\xd7\xa9" : 300,
    "\xd7\xaa" : 400}

# testing specific commands with dictionary
def main():
	print ('The following is a list of the')
	print ('contents in Hebrew Gematria Dictionary')
	pairNum = len(hebrewEncodedDict)
	print ('There are',pairNum,'key/value pairs in this dictionary\n')
	print (hebrewEncodedDict,'\n')

	print ('The following is a list of the')
	print ('keys in Hebrew Gematria Dictionary\n')
	gematriaKeys = hebrewEncodedDict.keys()
	print (gematriaKeys,'\n')

	print ('The following is a list of the')
	print ('values in Hebrew Gematria Dictionary\n')
	gematriaValues = hebrewEncodedDict.values()
	print (gematriaValues,'\n')

main()
