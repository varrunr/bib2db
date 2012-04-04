import urllib2
import urllib
import bibtex

url1 = 'http://pubdev.cs.sunysb.edu/Intranet/Authors/authorAction.php?action=check&last=Wang&first=Lei'
url2 = 'http://pubdev.cs.sunysb.edu/Intranet/Publications/publiAction.php'

authorAPI =  'http://pubdev.cs.sunysb.edu/Intranet/Authors/authorAction.php?'
publicationAPI =  'http://pubdev.cs.sunysb.edu/Intranet/Publications/publiAction.php'
 
def add_auth(first,last):
    req_url = authorAPI + '?action=check&last=%s&first=%s' % (last,first)
    response = urllib2.urlopen(req_url)
    auth_id = int(response.read())
    return auth_id
    #print auth_exists.get_data()

def add_pub(bib):
    values = {  'act':'add',
                'authorList':'35,32', #TODO
                'projectList':'',
                'id':'',
                'entry':'article',
                'name':'',
                'title': bib.title,
                'year':bib.year,
                'journal': bib.journal,
                'publisher': bib.publisher,
                'booktitle': bib.booktitle,
                'address': bib.address,
                'volume': bib.volume,
                'number': bib.number,
                'pages': bib.pages,
                'month': bib.month,
                'optkey':'', #TODO
                'keywords':'', #TODO
                'abstract': bib.abstract,
                'issn': bib.issn,
                'doi': bib.doi,
                'note':'' #TODO
        }
    data = urllib.urlencode(values)
    req = urllib2.Request(publicationAPI, data)
    response = urllib2.urlopen(req)
    pub_id = response.read()
    return pub_id

"
values = {  'act':'add',
            'authorList':'35,32',
            'projectList':'',
            'id':'',
            'entry':'article',
            'name':'',
            'title':'Testing POST Requests',
            'year':'2012',
            'journal':'name',
            'publisher':'System staff',
            'booktitle':'blah',
            'address':'Stony Brook,NY',
            'volume':'1',
            'number':'1',
            'pages':'13-15',
            'month':'Jan',
            'optkey':'asd',
            'keywords':'testing',
            'abstract':'blsbldnsflnvlskf',
            'issn':'123455',
            'doi':'asdasdasd22',
            'note':'asdasdasd'
        }

data = urllib.urlencode(values)
req = urllib2.Request(url2, data)
response = urllib2.urlopen(req)
print response.read()
#response = urllib2.urlopen(url)
#print response.read()
#print auth_exists.get_data()
"
