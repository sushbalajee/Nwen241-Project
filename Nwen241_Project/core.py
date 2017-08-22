import urllib.request
import urllib
import re
import os
from html.parser import HTMLParser
                
        

def pywget(url):
    
    match = re.search(r'\w+\.html', url) #search for regex
    if match:
      filename = match.group()
      if os.path.exists(filename):
            x = 0
            while os.path.exists(filename):
                x += 1
                
                filename2 = filename[:-4] + str(x) + "."  + filename[-4:]
                if not os.path.exists (filename2):

                    urllib.request.urlretrieve(url,filename2)
                    return None
      else:
        urllib.request.urlretrieve(url,filename)

            
      

    else:

        
        match = re.search(r'\w+\.jpg', url)
        filename = match.group()
        newn = ""

        
        if os.path.exists(filename):
            x = 0
            while os.path.exists(filename):
                x += 1
                
                filename2 = filename[:-4] + "." + str(x) + filename[-4:]
                if not os.path.exists (filename2):

                    urllib.request.urlretrieve(url,filename2)
                    return None
 
        else:
            
            urllib.request.urlretrieve(url,filename)

        

    
        
#pywget("http://homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumpyCat.jpg")
#pywget("http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html")
