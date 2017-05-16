# -*- coding: utf-8 -*-

file = open("bib.txt").read()


#{\'\i}
authors_list = []
dic = {}
fsplit = file.split("@")
for x in fsplit:
	ffsplit = x.split("\n")
	title = ""
	for y in ffsplit:	
		if "title" in y:	
			title = y
		all_authors = ""
		if "author" in y:
			count = y.count("},")
			if count == 2:
				start = y.find("},")+6
			else:
				start = 0

			z = y[y.find("={")+2:y.find("},", start)]
			
			authors = z.split(" and ")
			for a in authors:
				b = a.replace("{", "").replace("\'", "").replace("}", "").replace('\"', '').replace("\`", "")
				c = b.replace("\e", "e").replace("\i", "i").replace("\u", "u").replace("\o", "o").replace("\i", "i")
				auth_names = c.split(", ")
				lastname = auth_names[0]
				if "others" == a:
					final_name = ""
				else:
					other = auth_names[1]
					other2 = other.split(" ")
					if len(other2) > 1:
						other = other2[0][0:1] + " " + other2[1]
					else:
						other = other[0:1]

					final_name = lastname + ", " + other

				all_authors += final_name + "; "
			authors_list.append(all_authors)
			dic[all_authors] = title




#print help(dic)
auths = dic.keys()
auths.sort()
#print authors_list
for x in auths:
	print x, " ----", dic[x]
	print "\n"

