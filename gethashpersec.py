import urllib2
import json
req = urllib2.Request("http://mining.bitcoin.cz/stats/json/")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print 'Pool speed currently at ' + json['ghashes_ps'] + ' Ghash/s'
