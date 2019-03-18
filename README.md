# opwire-agent: sample command line in Python

## Install

Clone example source code from github:

```shell
git clone https://github.com/opwire/sample-cmdline-python.git
```

Change the current working directory to the project folder:

```shell
cd sample-cmdline-python
```

Download and extract the latest [`opwire-agent`](https://github.com/opwire/opwire-agent/releases/latest) program into this directory:

![project-home-dir](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/ls.png)

## Test the service using a web browser

Execute the following command:

```shell
./opwire-agent -p=8888 --default-command="python example.py"
```

Open the URL `http://localhost:8888/run?type=microservice&type=python`:

![example-output](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/example.png)

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b your-new-feature`)
3. Commit your changes (`git commit -am "Add some feature"`)
4. Push to the branch (`git push origin your-new-feature`)
5. Create new Pull Request

## License

MIT

See [LICENSE](LICENSE) to see the full text.
