import os, sys
import system_handler as sH
from mysql_handler import getWordList
import re

def restoreBrokenWords(inputString, standardDic):

	brokenWords = re.findall(r'\w+(?:-\n\w+)+', inputString)
	
	newString = inputString

	for bw in brokenWords:

		withDash = bw.replace('\n', '') 
		nonDash = bw.replace('-\n', '')

		if withDash.lower() in standardDic:
			newString = newString.replace(bw, withDash)
		elif nonDash.lower() in standardDic:
			newString = newString.replace(bw, nonDash)
	return newString

def restoreBrokenWords2 (inputString, standardDic):

	brokenWords = re.findall(r'\b\w+-\n+\w+', inputString)
	
	newString = inputString

	for bw in brokenWords:

		withDash = bw.replace('\n', '') 
		nonDash = bw.replace('-', '')
		nonDash = nonDash.replace('\n', '')

		if withDash.lower() in standardDic:
			newString = newString.replace(bw, withDash)
		elif nonDash.lower() in standardDic:
			newString = newString.replace(bw, nonDash)
	return newString

def writeTextFile(textContent, filePath):
    with open(filePath, 'w', encoding ='utf-8') as file:
        file.write(textContent)


def cleanJunk(inputText, regPat):
	outputText = ''
	pattern = re.compile(regPat)
	outputText = re.sub(pattern, '', inputText)
	return outputText

def cleanLine(inputText, regPat):
	outputText = ''
	pattern = re.compile(regPat, re.M)
	outputText = re.sub(pattern, '', inputText)
	return outputText


def processText(inFile, outDir):
	outFilePath = sH.getNormalPath(inFile, outDir)
	newText = sH.readTextFile(inFile)
	wordList = getWordList()
	newText = restoreBrokenWords2(newText, wordList)
	#regPat = r'\n\s{8}'
	#newText = cleanJunk(newText, regPat)

	writeTextFile(newText, outFilePath)
	sH.openDir(outDir)
	sys.exit()

	