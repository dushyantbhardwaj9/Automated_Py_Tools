#!/usr/bin/env python2

import sys
import optparse
import zipfile

class zipExtractor:
    
    def __init__(self, zipFileName, wordListName):
        self.zipFileName = zipFileName
        self.wordListName = wordListName

    def extractFile(self, zipFile, password):
        try:
            zipFile.extractall(pwd=password)
            return password
        except Exception :
            pass
    
    def bruteForce(self):
        zipFile = zipfile.ZipFile(self.zipFileName)
        with open(self.wordListName ) as list:
            for words in list.readlines():
                password = words.strip('\n')
                secret = self.extractFile(zipFile = zipFile, password = password)
                if secret:    
                    return True, secret
        return False, "Not Found"

class main:
    def zipBruteForce(self):
        parser = optparse.OptionParser("%prog " + " -f <zipFile> -d <dictionary>")
        parser.add_option('-f','--file', dest = "zipFileName", type = "string", help = "specify Zip File")
        parser.add_option('-d','--dictionary', dest = "wordListName", type = "string", help = "specify wordlst file")
        options, args = parser.parse_args()
        if options.zipFileName == None or options.wordListName == None :
            print parser.usage
            exit(0)
        else:
            zipFileName = options.zipFileName
            wordListName = options.wordListName
        zipExtract = zipExtractor(zipFileName = zipFileName, wordListName = wordListName) 
        return zipExtract.bruteForce()
        

if __name__ == "__main__":
    run = main()
    result, secret = run.zipBruteForce()
    if result:
        print "[+] Password Found : ",secret
    else:
        print "[-] No Matching password found in provided dictionary."
                