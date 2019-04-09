# opwire-agent: sample command line in Python

<!-- TOC -->

- [Installation](#installation)
  - [Checkout source code](#checkout-source-code)
  - [Download `opwire-agent`](#download-opwire-agent)
- [Call the service from browsers](#call-the-service-from-browsers)
- [Test the service with `curl`](#test-the-service-with-curl)
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
./opwire-agent serve
```

Open the URL `http://localhost:8888/$?type=microservice&type=python`:

![example-output](https://raw.github.com/opwire/sample-cmdline-python/master/docs/assets/images/example.png)

## Test the service with `curl`

Execute the following command:

```shell
./opwire-agent serve -p=8888 --default-command="python example.py"
```

Make a HTTP request with `curl`:

```curl
curl -v --request POST \
  --url 'http://localhost:8888/$?type=microservice&type=python' \
  --header 'opwire-execution-timeout: 0.5s' \
  --header 'opwire-explain-failure: 1' \
  --header 'opwire-explain-success: 1' \
  --header 'opwire-request-id: 12345667899222' \
  --data '{
  "name": "Opwire",
  "url": "https://opwire.org/"
}'
```

Result:

```plain
> POST /$?type=microservice&type=python HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8888
> Accept: */*
> opwire-execution-timeout: 0.5s
> opwire-explain-failure: 1
> opwire-explain-success: 1
> opwire-request-id: 12345667899222
> Content-Length: 54
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 54 out of 54 bytes
< HTTP/1.1 205 Reset Content
< Content-Type: text/plain
< X-Exec-Duration: 0.024510
< Date: Tue, 09 Apr 2019 05:49:29 GMT
< Transfer-Encoding: chunked
< 

[edition------------------------------------------------------------------------
{
  "revision": "3de2f29",
  "version": "v1.0.6-34-g3de2f29"
}
------------------------------------------------------------------------edition]

[request------------------------------------------------------------------------
{
  "header": {
    "Accept": [
      "*/*"
    ],
    "Content-Length": [
      "54"
    ],
    "Content-Type": [
      "application/x-www-form-urlencoded"
    ],
    "Opwire-Execution-Timeout": [
      "0.5s"
    ],
    "Opwire-Explain-Failure": [
      "1"
    ],
    "Opwire-Explain-Success": [
      "1"
    ],
    "Opwire-Request-Id": [
      "12345667899222"
    ],
    "User-Agent": [
      "curl/7.35.0"
    ]
  },
  "method": "POST",
  "params": null,
  "path": "/$",
  "query": {
    "type": [
      "microservice",
      "python"
    ]
  }
}
------------------------------------------------------------------------request]

[command------------------------------------------------------------------------
{
  "provided": {
    "method": "POST",
    "resource": "",
    "timeout": 0.5
  },
  "resolved": {
    "command": "python example.py",
    "method": null,
    "resource": ":default-resource:",
    "timeout": 0.5
  }
}
------------------------------------------------------------------------command]

[settings-----------------------------------------------------------------------
{
  "MYSQL_PASSWORD": "root",
  "MYSQL_URL": "mysql://localhost:3306",
  "MYSQL_USERNAME": "root"
}
-----------------------------------------------------------------------settings]

[stdin--------------------------------------------------------------------------
{
  "name": "Opwire",
  "url": "https://opwire.org/"
}
--------------------------------------------------------------------------stdin]

[stdout-------------------------------------------------------------------------
{
  "OPWIRE_SETTINGS": {
    "MYSQL_PASSWORD": "root", 
    "MYSQL_URL": "mysql://localhost:3306", 
    "MYSQL_USERNAME": "root"
  }, 
  "OPWIRE_EDITION": {
    "version": "v1.0.6-34-g3de2f29", 
    "revision": "3de2f29"
  }, 
  "OPWIRE_REQUEST": {
    "path": "/$", 
    "query": {
      "type": [
        "microservice", 
        "python"
      ]
    }, 
    "method": "POST", 
    "params": null, 
    "header": {
      "Opwire-Execution-Timeout": [
        "0.5s"
      ], 
      "Content-Length": [
        "54"
      ], 
      "Opwire-Explain-Failure": [
        "1"
      ], 
      "Opwire-Explain-Success": [
        "1"
      ], 
      "Accept": [
        "*/*"
      ], 
      "User-Agent": [
        "curl/7.35.0"
      ], 
      "Opwire-Request-Id": [
        "12345667899222"
      ], 
      "Content-Type": [
        "application/x-www-form-urlencoded"
      ]
    }
  }, 
  "input": {
    "url": "https://opwire.org/", 
    "name": "Opwire"
  }
}
-------------------------------------------------------------------------stdout]
* Connection #0 to host localhost left intact
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b your-new-feature`)
3. Commit your changes (`git commit -am "Add some feature"`)
4. Push to the branch (`git push origin your-new-feature`)
5. Create new Pull Request

## License

MIT

See [LICENSE](LICENSE) to see the full text.
