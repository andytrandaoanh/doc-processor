import os, sys

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def getNormalPath(outfile, outdir):
	TEXT_EXT = ".txt"
	
	temp_path = outfile
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	normal_path =  os.path.join(outdir, fname +  TEXT_EXT) 
	return(normal_path)
	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  