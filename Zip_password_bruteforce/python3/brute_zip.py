#!/usr/bin/env python

import sys
import optparse
import zipfile
from threading import Thread
import datetime

class zip_extractor:
    def __init__(self):
        self.found = False
        pass

    def extract_file(self, zipFile, password):
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

class init_brute_force(zip_extractor):
    def __init__(self, zip_file_name, word_list_name):
        self.zip_file_name, = zip_file_name
        self.word_list_name = word_list_name

    def brute_force(self):
        zipFile = zipfile.ZipFile(self.zip_file_name)

        with open(self.word_list_name,'r',2_000_000 ) as file:
            while(file.readline()):
                password = file.readline().strip('\n')
                thread = Thread(target = self.extract_file, args= (zipFile,password, ) )
                thread.start()
                thread.join()
                if self.found == True:
                    return
            else:
                print("[-] No Matching password found in provided dictionary.")
                return

class input_parser:
    def __init__(self):
        pass

    def zip_brute_force(self):
        parser = optparse.OptionParser("%prog -f <zipFile> -d <dictionary>")
        parser.add_option('-f','--file', dest = "zip_file_path", type = "string", help = "specify Zip File path")
        parser.add_option('-d','--dictionary', dest = "word_list_path", type = "string", help = "specify wordlist file path")
        options, args = parser.parse_args()
        del args
        if options.zip_file_name == None or options.word_list_name == None :
            print (parser.usage)
            exit(0)
        else:
            zip_file_name = options.zip_file_name
            word_list_name = options.word_list_name

        print(f'[+] Reading Zip File {zip_file_name} ')
        print(f'[+] Reading dictionary File {word_list_name} ')

        return zip_file_name, word_list_name

class brute_zip:
    def __init__(self):
        pass
    
    def run(self):
        parsed_input = input_parser()
        zip_file_name, word_list_name = parsed_input.zip_brute_force()

        init_brute = init_brute_force(zip_file_name, word_list_name)
        init_brute.brute_force()


if __name__ == "__main__":
    obj = brute_zip()
    obj.run()
