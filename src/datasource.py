import logging

import grpc
from concurrent import futures

import proto.backend_pb2 as backend
import proto.backend_pb2_grpc as backend_grpc


class DiagnosticsHandler(backend_grpc.DiagnosticsServicer):

    def CheckHealth(self, request, context):
        return backend.CheckHealthResponse(status="200", message="hello world")

    def CollectMetrics(self, request, context):
        pass


class QueryDataHandler(backend_grpc.DataServicer):

    def QueryData(self, request, context):
        pass


class ResourceHandler(backend_grpc.ResourceServicer):

    def CallResource(self, request, context):
        pass


class Datasource(object):

    def __init__(self, diagnostic_handler, query_handler, resource_handler={}):
        self.diagnostic_handler = diagnostic_handler
        self.query_handler = query_handler
        self.resource_handler = resource_handler

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        backend_grpc.add_DataServicer_to_server(query_handler, self.server)
        backend_grpc.add_DiagnosticsServicer_to_server(
            diagnostic_handler, self.server)
        backend_grpc.add_ResourceServicer_to_server(
            resource_handler, self.server)

    def serve(self):
        # fix
        logging.basicConfig()
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        self.server.wait_for_termination()


# remove
if __name__ == '__main__':
    dh = DiagnosticsHandler()
    qh = QueryDataHandler()
    rh = ResourceHandler()
    ds = Datasource(dh, qh, rh)

    ds.serve()
