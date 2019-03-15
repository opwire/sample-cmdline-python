import json
import os
import sys

def load(args):
  _store = {}
  load_env(_store)
  load_input(_store)
  return _store

def load_env(store):
  for envName in ["OPWIRE_EDITION", "OPWIRE_REQUEST", "OPWIRE_SETTING"]:
    envData = os.environ.get(envName)
    if type(envData) == str:
      try:
        store[envName] = json.loads(envData)
      except:
        store[envName] = envData
        pass #try
      pass #if
    pass #for
  pass #def

def load_input(store):
  _input = ''
  for line in sys.stdin:
    _input += line
    pass #for
  if isinstance(_input, str):
    store["input"] = _input
    try:
      store["input"] = json.loads(_input)
    except Exception, err:
      raise err
    pass #if
  return store
