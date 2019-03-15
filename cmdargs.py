import argparse

def load():
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
