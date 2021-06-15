#Manipulating XML

import xml.dom.minidom

def main():
    #load and parsing the xml
    data_in_xml=xml.dom.minidom.parse("XMLfile.xml")
    #print the document node
    print(data_in_xml.nodeName)
    #print the first child tag look for syntax C and N is bigger
    print(data_in_xml.firstChild.tagName)  
    #get elements by tagnames tagname= skill
    list_of_tags=data_in_xml.getElementsByTagName("skill")
    for i in list_of_tags:
        print(i.getAttribute("name"))   #get attribute using name
    #creating a new skill element
    newskill= data_in_xml.createElement("skill")
    newskill.setAttribute("skill","Microsoft Azure")
    data_in_xml.firstChild.appendChild(newskill)        
main()    