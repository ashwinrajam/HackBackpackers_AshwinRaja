import xml.etree.ElementTree as ET
import re
tree = ET.parse('wflow.xml')
root = tree.getroot()
for TRANSFORMATION in root.iter('TRANSFORMATION'):
	attr=TRANSFORMATION.attrib
sq=grep TRANSFORMFIELD attr
for INSTANCE in root.iter('INSTANCE')
	attr2=INSTANCE.attr
txn=grep TOFIELD attr2
i=0
while sq
	x1[i] = re.search("^NAME =\".\"", sq)
	i=i+1
i=0
while txn
	x2[i]= re.search("^FROMFIELD =\".\"", sq)
	i=i+1
i=0
while txn
	x3[i]= re.search("^TOFIELD =\".\"", sq)
	i=i+1
i=0
while x1
	while x2
		if x1[i]==x2[i] :
			print (x1[i] " -->" x3[i])
