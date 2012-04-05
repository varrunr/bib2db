import xml.etree.ElementTree as ET
#from parse import *


class Author:
    def __init__(self,first = '',last = '',
                 mid = '',url = '',rank = 0):
        self.id = -1
        self.first = first
        self.last = last
        self.mid  = mid
        self.url = url
        self.rank = rank
    
    def pretty_print(self):
        print self.rank
        print "------"
        print (self.first) + " " + (self.mid) + " " + (self.last)
        print "Homepage: " + (self.url)

class Bibtex:
    def __init__(self,bibid,filename):
        #Important fields
        self.bibid = bibid
        self.filename = filename
        self.list_of_authors = []
        self.title = ""
        self.booktitle = ""
        self.journal = "na"
        self.type_of_publication = ""
        #Other
        self.keywords = []
        self.publisher = ""
        self.chapter = ""
        self.edition = ""
        self.editor = ""
        self.institution = ""     
        self.school = ""
        self.issn = ""
        # optional
        self.month = ""
        self.year = ""
        self.note = ""
        self.number = ""
        self.optkey = ""
        self.organization = ""
        self.pages = ""
        self.series = ""
        self.type = ""
        self.volume = ""
        self.issn = ""
        self.doi = ""
        self.abstract = "" 
        self.url = ""
        self.address = ""
    
    def append_name(author_name):
        list_of_names.append(author_name)
    
    def add2db(self):
        pass

#    def parsedoc(self):
#        return  (ET.parse(self.filename)).getroot()

    def pretty_print(self):
        #Important fields
        print self.bibid
        #self.list_of_authors = []
        print "Title: " + self.title
        print "Booktitle: " + self.booktitle
        print "Journal:" + self.journal
        print "Type of pub: " + self.type_of_publication
        print "Publisher: " + self.publisher
        print "ISSN: " + self.issn 
        print "URL: " + self.url
        #Other
        print "Keywords:"
        print self.keywords

        print "Chapter: " + self.chapter
        print "Edition: " + self.edition
        print "Editor: " + self.editor
        print "Insti: " + self.institution
        print "School: " + self.school

        # optional
        print "Month: " + self.month
        print "Year: " + self.year
        print "Note: " + self.note
        print "Number: " + self.number
        print "Optkey: " + self.optkey
        print "Org: " + self.organization
        print "Pages: " + self.pages
        print "Series: " + self.series
        print "Type: " + self.type
        print "Vol: " + self.volume
        print "doi: " + self.doi
        print "abstract: " + self.abstract
