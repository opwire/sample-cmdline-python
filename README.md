# Sample Opwire command line in Python

## Install

Clone example source code from github:

```shell
git clone https://github.com/opwire/sample-cmdline-python.git
```

Change the current working directory to the project folder:

```shell
cd sample-cmdline-python
```

Download latest `opwire-agent` to this folder:

![project-home-dir](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/ls.png)

## Run

Execute the following command:

```shell
./opwire-agent -p=8888 --default-command="python example.py"
```

Make the simple REST request:

```curl
curl "http://localhost:8888/run?type=microservice&type=python"
```

or open with a web browser:

![example-output](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/example.png)
