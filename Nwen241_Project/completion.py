import urllib.request
import urllib
import re
import os
from html.parser import HTMLParser



def pywget(url):

    try:
        parser = MyHTMLParser()
        global http
        http = url
        data = (urllib.request.urlopen(url).read().decode())
        parser.feed(data)
        check(http)
    except:
     print("Error")

#-----------------------------------------------------------------------#

 
def check(url):

     filename = url.split('/')[-1]
     
     if os.path.exists(filename):
            x = 0
            while os.path.exists(filename):
                
                x += 1               
                filename2 = filename[:-4] + "." + str(x) + "." + filename[-4:]

                if not os.path.exists (filename2):
                    
                    urllib.request.urlretrieve(url,filename2)
                    return None
 
            print("exists")          
         
     else:
         urllib.request.urlretrieve(url,filename)

#-----------------------------------------------------------------------#


class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):

        lengthAttrs = len(attrs)
        
        if lengthAttrs> 0:
                  
                  link = attrs[0]
                  link = link[1]
                  
                  f = http.split("/")[-1]
                  name = link.split("/")[-1]
                  
                  lengthName = len(name)
                  lengthF = len(f)
                  

                  if link.endswith(name):
                      entireLink = link[:-lengthName]
                      newHttp = http[:-lengthF]

                  if entireLink == newHttp:
                      check(link)#checks for existing files
                      
                  if not link.startswith("http://"):
                      if not link.startswith("//"):
                          link = os.path.join(newHttp + link)
                          check(link) 
                          

#    def handle_endtag(self, tag):
#         print ("")
#    def handle_data(self, data):
#         print ("")

              
#-----------------------------------------------------------------------#
    

    
        
#pywget("http://homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumpyCat.jpg")
#pywget("http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html")
