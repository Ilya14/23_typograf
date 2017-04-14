# Typograf Service

## Description

Typograf Service for preparation of the Russian text for the
publication in WEB. Carries out the following operations:

* replacement of quotes ' and " on « »;
* replacement of a hyphen on a dash in the right places;
* replacement of hyphens by a short dash in phone numbers;
* linking of numbers with the subsequent words by indissoluble gap;
* removal of excess gaps and transfers of lines;
* linking of the unions and any words from 1-2 symbols with the subsequent words.

## Usage

For start of service on the localhost it is enough to enter
the following command:

```sh
$ python3.5 ./server.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Input and processing of the text are carried out in the browser on the
address: http://127.0.0.1:5000/

For expansion of functionality of Typograf Service it is necessary to
add regular expressions to typograf.py script.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
