import bootstrap
import cmdargs
import json
import sys

if __name__ == '__main__':
  args = cmdargs.load()
  try:
    # load environment varialbes & input data
    store = bootstrap.load(args)

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
