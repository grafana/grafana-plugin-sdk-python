import abc
import logging

import grpc
from concurrent import futures

import sdk.proto.backend_pb2 as backend
import sdk.proto.backend_pb2_grpc as backend_grpc


class BasePlugin(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def CheckHealth(self, request, context):
        pass

    @abc.abstractmethod
    def CollectMetrics(self, request, context):
        pass

    @abc.abstractmethod
    def QueryData(self, request, context):
        pass

    @abc.abstractmethod
    def CallResource(self, request, context):
        pass


class Server(object):

    def __init__(self, handler):

        if not issubclass(handler.__class__, BasePlugin):
            raise

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        self._add_servicers(handler)

    def _add_servicers(self, handler):
        backend_grpc.add_DiagnosticsServicer_to_server(
            handler, self.server)
        backend_grpc.add_DataServicer_to_server(
            handler, self.server)
        backend_grpc.add_ResourceServicer_to_server(
            handler, self.server)

    def serve(self):
        # fix
        logging.basicConfig()
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        self.server.wait_for_termination()
