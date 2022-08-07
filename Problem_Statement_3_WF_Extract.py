import xml.etree.ElementTree as ET
import re
tree = ET.parse('wflow.xml')
root = tree.getroot()
#All attributes related to the Tag is stored in a variable.
for TRANSFORMATION in root.iter('TRANSFORMATION'):
	attr=TRANSFORMATION.attrib
#Checking for Text field
sq=grep TRANSFORMFIELD attr
#All attributes related to the Tag is stored in a variable.
for INSTANCE in root.iter('INSTANCE')
	attr2=INSTANCE.attr
#Checking for Text field
txn=grep TOFIELD attr2
i=0
#Checking for Field name
while sq
	x1[i] = re.search("^NAME =\".\"", sq)
	i=i+1
i=0
#Checking for Field name
while txn
	x2[i]= re.search("^FROMFIELD =\".\"", sq)
	i=i+1
i=0
#Checking for Field name
while txn
	x3[i]= re.search("^TOFIELD =\".\"", sq)
	i=i+1
i=0
#Below loop will compare the data between 2 array elements. If they are same, we print the lineage
while x1
	while x2
		if x1[i]==x2[i] :
			print (x1[i] " -->" x3[i])
