from unzip import Unzip
#from bibtex import Bibtex
from parse import *
import re
from subprocess import check_output
from sendpost import *
import sys

class Pipe:
    def __init__(self):
        self.output = []
    
    def append( self , filename, status, err_no):
        # TODO: Map error no to error desc
        row = [filename, status, err_no]
        (self.output).append(row)

    def getop(self):
        op = ""
        for i in self.output:
            op +=  "%s %s %s\n" % ( i[0] , i[1] , i[2] )
        return op

def unzip_file(src,dest):
    unzipper = Unzip()
    return unzipper.extract( src , dest)

def prune(file_list):
    # TODO: Look for .bib files only
    pruned_list = []
    for f in file_list:
        if re.match('^.*\.(bib)$',f) is not None:
            pruned_list.append(f)
    return pruned_list

def file2xml(filename):
    try:
        xml = check_output(['bib2xml',filename])
        return xml,0
    except CalledProcessError:
        print "Oops, file cannot be parsed"
        return xml,-1


def main():

    zipsource = sys.argv[1]
    zipdest = sys.argv[2] 

    " Unzip uploaded zip file "
    file_list = unzip_file(zipsource,zipdest)
    
    " Check for misplaces files i.e not *.bib "
    bib_file_list = prune(file_list)
    
    " convert all bib files to xml and add to DB "
    task_status = Pipe()
    bibid = 1
    
    for filename in bib_file_list:
        xml , errors = file2xml( '%s/%s'% (zipdest,filename) )
        " New bibtex file "
        bibtexfile = Bibtex(bibid,filename)
        " Process bibtex "
        bibtexfile, status, errors = process_xml(bibtexfile,xml)
        """ Add publication to database """ 
        add_pub(bibtexfile)
        " Pipe errors out "
        task_status.append(filename , status , errors)
    
    print task_status.getop()

if __name__ == '__main__': main()
