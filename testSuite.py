#!/usr/bin/env python
import os
from executor import Executor
from wrapper import OxfordD

e = Executor("placeholder","placeholder")
e.change_name()
name = e.get_varname()
word = e.get_word()
ox = OxfordD('<your_url>','app_id','app_key','en',word,'definitions')

#text = "var " + "v" + name + "v" + "=" + "\"" + ox.get_definition() + "\"" + ';\n'
#assignation = "var " + "a" + name + "a" + "=" + "\"" + word + "\"" + ';\n'

creatDefinitions = "var defL = [];"
text = "defL.push(" + "\""+ ox.get_definition() + "\"" + ");\n"
createWord = "var wordsL = [];"
assignation = "wordsL.push(" + "\""+ word + "\"" + ");\n"

wordsfile = "words.js"
filename = "definitions.js"

if os.path.exists(wordsfile):
	wfile = open(wordsfile, "a")
	wfile.write(assignation)
	if os.path.exists(filename):
		file = open(filename,"a")
		file.write(text)
	else:
		file = open(filename,"w")
		file.write(createDefinitions)
		file.write(text)
else:
	wfile = open(wordsfile,"w")
	wfile.write(createWord)
	wfile.write(assignation)
	if os.path.exists(filename):
		file = open(filename,"a")
		file.write(text)
	else:
		file = open(filename,"w")
		file.write(createDefinitions)
		file.write(text)
