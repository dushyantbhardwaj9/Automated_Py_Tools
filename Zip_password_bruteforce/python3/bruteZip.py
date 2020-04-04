#!/usr/bin/env python

import optparse
import zipfile

class zipExtractor:
    
    def __init__(self, zipFileName, wordListName):
        self.zipFileName = zipFileName
        print(f'[+] Reading Zip File {zipFileName} ')
        self.wordListName = wordListName
        print(f'[+] Reading dictionary File {wordListName} ')


    def extractFile(self, zipFile, password):
        try:
            password = bytes(password, encoding= "ascii")
            zipFile.extractall(pwd=password)
            return True
        except Exception  :
            pass
        return False
    
    def bruteForce(self):
        zipFile = zipfile.ZipFile(self.zipFileName)
        with open(self.wordListName ) as list:
            lst = list.readlines()
            for words in lst:
                password = words.strip('\n')
                secret = self.extractFile(zipFile = zipFile, password = password)
                if secret == True:
                    print (f"[+] Password Found : {password}")
                    return
        print ("[-] No Matching password found in provided dictionary.")
        return

class main:
    def zipBruteForce(self):
        parser = optparse.OptionParser("%prog " + " -f <zipFile> -d <dictionary>")
        parser.add_option('-f','--file', dest = "zipFileName", type = "string", help = "specify Zip File")
        parser.add_option('-d','--dictionary', dest = "wordListName", type = "string", help = "specify wordlst file")
        options, args = parser.parse_args()
        if options.zipFileName == None or options.wordListName == None :
            print (parser.usage)
            exit(0)
        else:
            zipFileName = options.zipFileName
            wordListName = options.wordListName
        zipExtract = zipExtractor(zipFileName = zipFileName, wordListName = wordListName) 
        return zipExtract.bruteForce()
        

if __name__ == "__main__":
    run = main()
    run.zipBruteForce()
                