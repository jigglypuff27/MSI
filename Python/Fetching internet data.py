#Fetching internet data

import urllib.request

def main():
    url_data=urllib.request.urlopen("http://google.com")
    print("get status code",url_data.getcode())      #getcode() function is used to get status code
    print("all data",url_data.read())                #read function is used to get all data

main()    