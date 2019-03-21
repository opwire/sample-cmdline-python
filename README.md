# opwire-agent: sample command line in Python

<!-- TOC -->

- [Installation](#installation)
  - [Checkout source code](#checkout-source-code)
  - [Download `opwire-agent`](#download-opwire-agent)
- [Call the service from browsers](#call-the-service-from-browsers)
- [Contributing](#contributing)
- [License](#license)

<!-- /TOC -->

## Installation

### Checkout source code

Clone example source code from github repository:

```shell
git clone https://github.com/opwire/sample-cmdline-python.git
```

Change the current working directory to the project folder:

```shell
cd sample-cmdline-python
```

### Download `opwire-agent`

To download the latest `opwire-agent` on Linux/macOS/BSD systems, run:

```shell
curl https://opwire.org/opwire-agent/install.sh | bash
```

For other systems:

* Download the relevant [`opwire-agent`](https://github.com/opwire/opwire-agent/releases/latest) release,
* Extract the `opwire-agent` or `opwire-agent.exe` binary from the archive to example folder (current directory).

![project-home-dir](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/ls.png)

## Call the service from browsers

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
