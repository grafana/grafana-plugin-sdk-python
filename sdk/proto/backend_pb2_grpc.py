# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import backend_pb2 as backend__pb2


class ResourceStub(object):
    """---------------------------------------------------------
    Resource service enables HTTP-style requests over gRPC.
    ---------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CallResource = channel.unary_stream(
            '/pluginv2.Resource/CallResource',
            request_serializer=backend__pb2.CallResourceRequest.SerializeToString,
            response_deserializer=backend__pb2.CallResourceResponse.FromString,
        )


class ResourceServicer(object):
    """---------------------------------------------------------
    Resource service enables HTTP-style requests over gRPC.
    ---------------------------------------------------------

    """

    def CallResource(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CallResource': grpc.unary_stream_rpc_method_handler(
            servicer.CallResource,
            request_deserializer=backend__pb2.CallResourceRequest.FromString,
            response_serializer=backend__pb2.CallResourceResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'pluginv2.Resource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Resource(object):
    """---------------------------------------------------------
    Resource service enables HTTP-style requests over gRPC.
    ---------------------------------------------------------

    """

    @staticmethod
    def CallResource(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pluginv2.Resource/CallResource',
                                              backend__pb2.CallResourceRequest.SerializeToString,
                                              backend__pb2.CallResourceResponse.FromString,
                                              options, channel_credentials,
                                              call_credentials, compression, wait_for_ready, timeout, metadata)


class DataStub(object):
    """-----------------------------------------------
    Data
    -----------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryData = channel.unary_unary(
            '/pluginv2.Data/QueryData',
            request_serializer=backend__pb2.QueryDataRequest.SerializeToString,
            response_deserializer=backend__pb2.QueryDataResponse.FromString,
        )


class DataServicer(object):
    """-----------------------------------------------
    Data
    -----------------------------------------------

    """

    def QueryData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QueryData': grpc.unary_unary_rpc_method_handler(
            servicer.QueryData,
            request_deserializer=backend__pb2.QueryDataRequest.FromString,
            response_serializer=backend__pb2.QueryDataResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'pluginv2.Data', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Data(object):
    """-----------------------------------------------
    Data
    -----------------------------------------------

    """

    @staticmethod
    def QueryData(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pluginv2.Data/QueryData',
                                             backend__pb2.QueryDataRequest.SerializeToString,
                                             backend__pb2.QueryDataResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)


class DiagnosticsStub(object):
    """-----------------------------------------------
    Diagnostics
    -----------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckHealth = channel.unary_unary(
            '/pluginv2.Diagnostics/CheckHealth',
            request_serializer=backend__pb2.CheckHealthRequest.SerializeToString,
            response_deserializer=backend__pb2.CheckHealthResponse.FromString,
        )
        self.CollectMetrics = channel.unary_unary(
            '/pluginv2.Diagnostics/CollectMetrics',
            request_serializer=backend__pb2.CollectMetricsRequest.SerializeToString,
            response_deserializer=backend__pb2.CollectMetricsResponse.FromString,
        )


class DiagnosticsServicer(object):
    """-----------------------------------------------
    Diagnostics
    -----------------------------------------------

    """

    def CheckHealth(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CollectMetrics(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiagnosticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CheckHealth': grpc.unary_unary_rpc_method_handler(
            servicer.CheckHealth,
            request_deserializer=backend__pb2.CheckHealthRequest.FromString,
            response_serializer=backend__pb2.CheckHealthResponse.SerializeToString,
        ),
        'CollectMetrics': grpc.unary_unary_rpc_method_handler(
            servicer.CollectMetrics,
            request_deserializer=backend__pb2.CollectMetricsRequest.FromString,
            response_serializer=backend__pb2.CollectMetricsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'pluginv2.Diagnostics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Diagnostics(object):
    """-----------------------------------------------
    Diagnostics
    -----------------------------------------------

    """

    @staticmethod
    def CheckHealth(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pluginv2.Diagnostics/CheckHealth',
                                             backend__pb2.CheckHealthRequest.SerializeToString,
                                             backend__pb2.CheckHealthResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CollectMetrics(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pluginv2.Diagnostics/CollectMetrics',
                                             backend__pb2.CollectMetricsRequest.SerializeToString,
                                             backend__pb2.CollectMetricsResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)


class TransformStub(object):
    """-----------------------------------------------
    Transform - Very experimental
    -----------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TransformData = channel.unary_unary(
            '/pluginv2.Transform/TransformData',
            request_serializer=backend__pb2.QueryDataRequest.SerializeToString,
            response_deserializer=backend__pb2.QueryDataResponse.FromString,
        )


class TransformServicer(object):
    """-----------------------------------------------
    Transform - Very experimental
    -----------------------------------------------

    """

    def TransformData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransformServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'TransformData': grpc.unary_unary_rpc_method_handler(
            servicer.TransformData,
            request_deserializer=backend__pb2.QueryDataRequest.FromString,
            response_serializer=backend__pb2.QueryDataResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'pluginv2.Transform', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Transform(object):
    """-----------------------------------------------
    Transform - Very experimental
    -----------------------------------------------

    """

    @staticmethod
    def TransformData(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pluginv2.Transform/TransformData',
                                             backend__pb2.QueryDataRequest.SerializeToString,
                                             backend__pb2.QueryDataResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)


class TransformDataCallBackStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryData = channel.unary_unary(
            '/pluginv2.TransformDataCallBack/QueryData',
            request_serializer=backend__pb2.QueryDataRequest.SerializeToString,
            response_deserializer=backend__pb2.QueryDataResponse.FromString,
        )


class TransformDataCallBackServicer(object):
    """Missing associated documentation comment in .proto file"""

    def QueryData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransformDataCallBackServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QueryData': grpc.unary_unary_rpc_method_handler(
            servicer.QueryData,
            request_deserializer=backend__pb2.QueryDataRequest.FromString,
            response_serializer=backend__pb2.QueryDataResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'pluginv2.TransformDataCallBack', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class TransformDataCallBack(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def QueryData(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pluginv2.TransformDataCallBack/QueryData',
                                             backend__pb2.QueryDataRequest.SerializeToString,
                                             backend__pb2.QueryDataResponse.FromString,
                                             options, channel_credentials,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)
