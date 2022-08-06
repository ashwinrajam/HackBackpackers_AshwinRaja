#!python
from __future__ import print_function
import sys
import fileinput
import xml
from xml.dom import minidom
import json

for line in fileinput.input():
        try:
                xmlDoc = minidom.parseString(line)
                print(json.dumps(dict(xmlDoc.childNodes[0].attributes.items())))
        except xml.parsers.expat.ExpatError:
                print("Unable to process line : ", line, file=sys.stderr)
        except KeyboardInterrupt:
                sys.exit(0)