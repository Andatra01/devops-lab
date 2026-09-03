#!/usr/bin/env python
import json

server_info = {"host":"web1","cpu":45}
json_string = json.dumps(server_info)
parsed = json.loads(json_string)

print (json_string)
print (parsed)

print(type(json_string))
print(type(parsed))
