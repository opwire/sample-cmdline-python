import json
import sys

def bootstrap():
  _store = {}

  _input = ''
  for line in sys.stdin:
    _input += line
  _store["input"] = _input

  return _store

sys.stdout.write(json.dumps(bootstrap(), indent=2))
