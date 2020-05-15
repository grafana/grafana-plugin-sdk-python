from __future__ import print_function
import logging

import grpc

import proto.backend_pb2 as backend
import proto.backend_pb2_grpc as backend_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = backend_grpc.DiagnosticsStub(channel)
        response = stub.CollectMetrics(backend.CollectMetricsRequest())
    print("Diagnostic client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
