import httplib,urllib
from urlparse import urlparse
conn = urllib.urlopen("http://localhost/HomeIOT/Test.php")
# res = conn.read()
# print res
url = "http://localhost/HomeIOT/Test.php"
url_part = urlparse(url)
print url_part
conn = httplib.HTTPConnection("http://localhost/HomeIOT/Test.php",80)
conn.request("GET",url_part.path)
res = conn.getresponse()
print res