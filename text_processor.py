import sys
import tika
tika.initVM()
from tika import parser
import json
from system_handler import openDir, getNormalPath


def processText(path1, path2):
	output_path = getNormalPath(path1, path2)
	parsed = parser.from_file(path1)
	textout = parsed["content"]
	with open(output_path, 'w', encoding="utf-8") as file:    
		file.write(parsed["content"])
	openDir(path2)
	sys.exit()
