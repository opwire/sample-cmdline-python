import argparse
import json
import os
import sys

# ----------------------------------------------------- local methods

def bootstrap(args):
  _store = {}
  load_env(_store)
  load_input(_store)
  return _store

def load_env(store):
  for envName in ["OPWIRE_REQUEST", "OPWIRE_SETTING"]:
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

# ----------------------------------------------------- args parsing

def extract_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input-format', help='Format for input data')
  parser.add_argument('--output-format', help='Format for output data')
  parser.add_argument('--format', help='Default format for input/output data')
  raw_args = parser.parse_args()
  
  _args = dict()
  _format = "json"
  if raw_args.format != None:
    _format = raw_args.format
  _args["input-format"] = _format
  if raw_args.input_format != None:
    _args["input-format"] = raw_args.input_format
  _args["output-format"] = _format
  if raw_args.output_format != None:
    _args["output-format"] = raw_args.output_format
  return _args

# ----------------------------------------------------- main program

if __name__ == '__main__':
  args = extract_args()
  try:
    # load environment varialbes & input data
    store = bootstrap(args)

    # do something with input data
    # .....

    # suppose the store is output...
    if args["output-format"] == "json":
      sys.stdout.write(json.dumps(store, indent=2))
    else:
      for key, data in store.items():
        sys.stdout.write(key.upper() + ":\n")
        if isinstance(data, str):
          sys.stdout.write(data)
        else:
          sys.stdout.write(json.dumps(data, indent=2))
        sys.stdout.write("\n\n")
        pass #for

  except Exception as err:
    errmap = {
      "name": type(err).__name__,
      "message": err.message
    }
    if args["output-format"] == "json":
      error = json.dumps(errmap, indent=2)
    else:
      error = "{name}: {message}".format(**errmap)
    sys.stderr.write(error)
    sys.exit(1)
