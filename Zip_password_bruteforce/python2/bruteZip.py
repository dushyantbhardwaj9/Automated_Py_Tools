#!/usr/bin/env python2

import optparse
import zipfile

class zipExtractor:
    
    def extractFile(self, zipFile, password):
        try:
            zipFile.extractall(pwd=password)
            return True
        except Exception :
            pass
    
    def bruteForce(self):
        zipFile = zipfile.ZipFile(self.zipFileName)
        with open(self.wordListName ) as list:
            for words in list.readlines():
                password = words.strip('\n')
                secret = self.extractFile(zipFile = zipFile, password = password)
                if secret:    
                    print ("[+] Password Found : {} ".format(password) )
                    return 
        print ("[-] No Matching password found in provided dictionary.")
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
        print('[+] Reading Zip File {}'.format(self.zipFileName) )
        print('[+] Reading dictionary File {}'.format(self.wordListName) )
        return self.bruteForce()
        

if __name__ == "__main__":
    run = zipExtractor()
    run.zipBruteForce()

                