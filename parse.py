from bibtex import *
import xml.etree.ElementTree as ET

namespace = "{http://www.loc.gov/mods/v3}"
xml_dir = '/home/varrun/Desktop/vislab/samples/testcase/'

def get_tag(tag_name):
    list_of_tags = tag_name.split('/')
    path = ""
    cnt = 0
    for tags in list_of_tags:
        path +=  namespace + tags 
        cnt += 1
        if cnt != len(list_of_tags):
            path += '/'
    return path

def read_f(filename):
    f = open(filename,'r')
    return f.read()

def not_none(item):
    if item == None:
        return 0
    else: 
        return 1

def is_valid_str(item):
    if not_none(item):
        if( item == ''):
            return 0
        return 1
    return 0

def populate_names(rootElement, bib):
    list_of_names =  rootElement.findall( get_tag('mods/name' ))
    rank = 1
    for name in list_of_names:
        auth = Author()
        auth.rank = rank
        name_parts = name.findall(get_tag('namePart'))
        for part in name_parts:
            field = part.get('type')
            if field == 'given':
                if auth.first == '':
                    auth.first = part.text
                else:
                    auth.mid = part.text
            else:
                auth.last = part.text
        rank += 1
        bib.list_of_authors.append(auth)
    return bib

def populate_title(rootElement,bib):
    # find title of publication
    title_info =  rootElement.find( get_tag('mods/titleInfo' ))
    title =  title_info.findtext(get_tag('title'))
    subtitle =  title_info.findtext(get_tag('subTitle'))
    if(is_valid_str(title)):
        bib.title = title
    if(is_valid_str(subtitle)):
        bib.title += ': ' + subtitle

    # Populate publication specific fields
    pub_info =  rootElement.find( get_tag('mods/relatedItem' ))
    genre = pub_info.findall(get_tag('genre'))
    pubtype = ""
    for g in genre:
        if ( (g.text).find("journal") != -1 or (g.text).find("periodical") != -1 ):
            pubtype = "Journal"
            break
        if ( (g.text).find("conference") != -1 ):
            pubtype = "Conference"
            break
    
    if is_valid_str(pubtype):
        bib.type_of_publication = pubtype

    if pubtype == "Journal" or pubtype == "Conference":
        # get title of journal/conference
        title = pub_info.findtext(get_tag('titleInfo/title'))

        if is_valid_str(title):
            if pubtype == "Journal":
                bib.journal = title
            else:
                bib.booktitle = title

        publisher = pub_info.findtext(get_tag('originInfo/publisher'))
        if is_valid_str(publisher):
            bib.publisher = publisher

        loc = pub_info.findtext(get_tag('originInfo/place/placeTerm'))
        if( is_valid_str(loc) ):
            bib.publisher = bib.publisher + " " + loc

        # populate journal specific fields
        if pubtype == "Journal":                
            identifiers = pub_info.findall(get_tag('identifier'))
            for i in identifiers:
                attribs = i.items()
                if len(attribs) > 0:
                    if attribs[0] == ('type','issn'):
                        issn = i.text
                        if( is_valid_str(issn) ):
                            bib.issn = issn

            # TODO: Check for 1+ identifiers
    return bib

def populate_issue_info(rootElement,bib):
    pages = rootElement.find(get_tag('mods/part/extent'))
    start = ""
    end = ""
    if not_none(pages):
        start = pages.findtext(get_tag('start'))
        end = pages.findtext( get_tag('end'))
        pages = start + '-' + end
        bib.pages = pages

    details = rootElement.findall(get_tag('mods/part/detail'))
    for d in details:
        if len(d.items())>0:
            if d.items()[0] == ('type','volume'):
                volume = d.findtext(get_tag('number'))
                if is_valid_str(volume):
                    bib.volume = volume
            if d.items()[0] == ('type','issue'):
                issue = d.findtext(get_tag('number'))
                if is_valid_str(volume):
                    bib.edition = issue
    return bib

def populate_cite_info(rootElement,bib):
    # get citation info
    cite_info = rootElement.findall(get_tag('mods/identifier'))
    for info in cite_info:
        if len(info.items()) > 0:
            if info.items()[0] == ('type','citekey'):
                #  TODO
                1 + 1
            else: 
                if info.items()[0] == ('type','doi'):
                    bib.doi = info.text
    
    #get publication url
    url = rootElement.find(get_tag('mods/location/url'))
    #if not_none(url):
        #bib.url = url.text
    return bib

#    list_of_detail = rootElement.findall(get_tag('mods/part/detail'))
    
#    if not_none(list_of_detail):
#        for detail in list_of_detail:
#            related_map[detail.get(detail.keys()[0])] = detail.findtext(get_tag('number'))
#    pages = rootElement.find(get_tag('mods/part/extent'))
#    if not_none(pages):
#        page_map = {}
#        page_map['start'] = pages.findtext(get_tag('start'))
#        page_map['end'] = pages.findtext( get_tag('end'))
#        related_map['page']= page_map
##   return bib

def populate_origin_info(rootElement):
    origin_info =  rootElement.find( get_tag('mods/originInfo' ))
    origin_map = {}
    origin_map['DateIssued'] = origin_info.findtext(get_tag('dateIssued'))
    return origin_map

def populate_related_items(rootElement):
    related_info =  rootElement.find( get_tag('mods/relatedItem' ))
    related_map = {}
    related_map['Title'] = related_info.findtext(get_tag('titleInfo/title'))
    related_map['Issuance'] = related_info.findtext(get_tag('originInfo/issuance'))
    related_map['Genre'] = related_info.findtext(get_tag('genre'))

    date_info = rootElement.find( get_tag('mods/part'))
    related_map['date'] = date_info.findtext(get_tag('date'))
    
    list_of_detail = rootElement.findall(get_tag('mods/part/detail'))
    
    if not_none(list_of_detail):
        for detail in list_of_detail:
            related_map[detail.get(detail.keys()[0])] = detail.findtext(get_tag('number'))
    pages = rootElement.find(get_tag('mods/part/extent'))
    if not_none(pages):
        page_map = {}
        page_map['start'] = pages.findtext(get_tag('start'))
        page_map['end'] = pages.findtext( get_tag('end'))
        related_map['page']= page_map
    
    return related_map

def process_xml(filename):
    bibmap = {}
    bib_no = 1
    bib = Bibtex(bib_no, filename);
    rootElement = bib.parsedoc()
    bib = populate_names(rootElement,bib)
    # TODO: Homepage?
    bib = populate_title(rootElement,bib)
    bib = populate_cite_info(rootElement,bib)
    bib = populate_issue_info(rootElement,bib)
    # TODO: Populate date, 
    #bib.add2db()
    print bib.pretty_print()
    return
    # TODO: Check if booktitle / journal
    bibmap['OriginInfo'] = populate_origin_info(rootElement)
    bibmap['SourceInfo'] = populate_related_items(rootElement)
    
    return bibmap
   
def process_bib(filename):
    results =  process_xml(xml_dir + filename)

filename = str(raw_input())
process_bib(filename)
