import json
import sys

def bootstrap():
  _store = {}

  _store["input"] = load_input()

  return _store

def load_input():
  _input = ''
  for line in sys.stdin:
    _input += line
  try:
    _inputJSON = json.loads(_input)
    return _inputJSON
  except:
    return _input
  pass

sys.stdout.write(json.dumps(bootstrap(), indent=2))
