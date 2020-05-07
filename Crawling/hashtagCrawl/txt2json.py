cfile = open("cocktailnames.txt", "r")
clist = cfile.read().split(" ")
output = open("t2j.out", 'w')
for cocktail in clist:
	result = '"' + cocktail.replace("\n", "") + '",'
	output.write(result)
output.close()
