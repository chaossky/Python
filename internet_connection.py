from urllib import request

def check_internet_connection():
    try:
        request.urlopen('http://216.58.192.142',timeout=1)
        return True
    except request.URLError:
        return False
    
if check_internet_connection():
    print("Internet connection is available.")
else:
    print("Internet connection is not available.")
    