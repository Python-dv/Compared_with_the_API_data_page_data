import json
import types

f =open('test.json','r')
sjson =''
while True:
    myjson=f.readline()
    if len(myjson) ==0:
        break
    sjson= sjson + myjson
f.close()

print ('sjson type is:',type(sjson))
mjson = json.loads(sjson)
print ('sjson change is',type(mjson))
print ('the length os mjson is ',len(mjson))
json_len = len(mjson)

sub = 'brief'

print (mjson['brief'])
mjson['brief'] = 'modify'
print (mjson['brief'])

print (mjson)
