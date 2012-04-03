import urllib2
import urllib

url1='http://pubdev.cs.sunysb.edu/Intranet/Authors/authorAction.php?action=check&last=Wang&first=Lei'
url2 = 'http://pubdev.cs.sunysb.edu/Intranet/Publications/publiAction.php'

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

