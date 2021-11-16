[![Circle CI](https://img.shields.io/circleci/build/gh/grafana/grafana-plugin-sdk-python)](https://circleci.com/gh/grafana/grafana-plugin-sdk-python)
[![codecov](https://codecov.io/gh/grafana/grafana-plugin-sdk-python/branch/master/graph/badge.svg)](https://codecov.io/gh/grafana/grafana-plugin-sdk-python)

# Grafana Plugin SDK Python

## Overview

In development, leave your expectations at the door!

You can find the officialy supported SDK [here]](https://pkg.go.dev/github.com/grafana/grafana-plugin-sdk-go). We recommend to read the [official guide](https://grafana.com/docs/grafana/latest/developers/plugins/) on how to build your own plugins first.

## Usage

`python -m grpc_tools.protoc -I <path_to_grafana_plugin_sdk_go>/proto --python_out=. --grpc_python_out=. backend.proto`
