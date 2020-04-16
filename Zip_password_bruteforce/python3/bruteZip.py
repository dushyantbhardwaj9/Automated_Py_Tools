#!/usr/bin/env python

import sys
import optparse
import zipfile
from threading import Thread
import datetime

class zipExtractor:
    found = False
    def extractFile(self, zipFile, password):
        try:
            password = bytes(password, encoding= "ascii")
            zipFile.extractall(pwd=password)
            password = str(password, encoding = "utf-8")
            print (f"[+] Password Found : {password}")
            self.found = True
            return self.found
        except Exception  :
            pass
        return False

    def bruteForce(self):
        zipFile = zipfile.ZipFile(self.zipFileName)
        with open(self.wordListName,'r',2_000_000 ) as file:
            while(file.readline()):
                password = file.readline().strip('\n')
                thread = Thread(target = self.extractFile, args= (zipFile, password) )
                thread.start()
                thread.join()
                if self.found == True:
                    return
            else:
                print("[-] No Matching password found in provided dictionary.")
                return
        
    def zipBruteForce(self):
        parser = optparse.OptionParser("%prog " + " -f <zipFile> -d <dictionary>")
        parser.add_option('-f','--file', dest = "zipFileName", type = "string", help = "specify Zip File")
        parser.add_option('-d','--dictionary', dest = "wordListName", type = "string", help = "specify wordlst file")
        options, args = parser.parse_args()
        if options.zipFileName == None or options.wordListName == None :
            print (parser.usage)
            exit(0)
        else:
            self.zipFileName = options.zipFileName
            self.wordListName = options.wordListName

        print(f'[+] Reading Zip File {self.zipFileName} ')
        print(f'[+] Reading dictionary File {self.wordListName} ')
        return self.bruteForce()
        

if __name__ == "__main__":
    run = zipExtractor()
    run.zipBruteForce()       