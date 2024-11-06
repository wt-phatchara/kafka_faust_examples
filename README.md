# kafka_faust_examples
Examples using faust and kafka for stream processing with InfluxDB and Telegraf

## Local Development

This repository uses [Pipenv](https://pipenv.pypa.io/en/latest/) for package managment & isolation.

Python version management using [asdf](https://asdf-vm.com/) is supported via [`/.tool-versions`](/.tool-versions).

All examples require [Kafka](https://kafka.apache.org/), container config is provided in [`/docker-compose.yaml`](/docker-compose.yaml).

## Examples
Use the [scratchpad.md](./scratchpad.md) for commands to execute the following exmaples. 

### hello_world
The "Hello World" example demonstrates the basics of a Faust streaming application. It sets up a simple Faust app that reads events from a Kafka topic and prints each event to the console. This example serves as an introduction to Faust’s structure, helping you understand how to create, configure, and run a Faust application with minimal setup.


### page_views
The "Page Views" example showcases real-time counting of page views using Faust. It reads page view events from a Kafka topic, aggregates the number of views per page, and stores these counts in an in-memory table. For each page view, the updated count is published to another topic, allowing consumers to access up-to-date view counts for each page in real time. This example highlights Faust’s ability to handle stateful stream processing and perform real-time aggregations. `telegraf.conf` is configured to consume the JSON messages and write them to InfluxDB. 

### Notes
- Pypi package `faust-streaming` is a fork of the deprecated `faust`
