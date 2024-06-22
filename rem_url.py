# Complete the function/method so that it returns 
# the url with anything after the anchor (#) removed.
            
def removed(url):
    return url.split('#')[0]

string1="http://www.codewars.com/#combat"
         
print(removed(string1))