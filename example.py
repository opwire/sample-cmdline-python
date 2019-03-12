import json
import sys

def bootstrap():
  _store = {}
  _store["input"] = "Hello Opwire"
  return _store

sys.stdout.write(json.dumps(bootstrap(), indent=2))
