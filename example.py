import json
import os
import sys

def bootstrap():
  _store = {}
  load_env(_store)
  load_input(_store)
  return _store

def load_env(store):
  for envName in ["OPWIRE_REQUEST", "OPWIRE_FEATAGS", "OPWIRE_SETTING"]:
    envData = os.environ.get(envName)
    if type(envData) == str:
      try:
        store[envName] = json.loads(envData)
      except:
        store[envName] = envData
        pass
      pass
    pass
  pass

def load_input(store):
  _input = ''
  for line in sys.stdin:
    _input += line
    pass
  _inputJSON = dict()
  try:
    if isinstance(_input, str):
      _inputJSON = json.loads(_input)
  except:
    pass
  store["input"] = _inputJSON
  return store

sys.stdout.write(json.dumps(bootstrap(), indent=2))
