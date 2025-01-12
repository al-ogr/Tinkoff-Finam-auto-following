# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from FinamPy.grpc.tradeapi.v1 import securities_pb2 as grpc_dot_tradeapi_dot_v1_dot_securities__pb2


class SecuritiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSecurities = channel.unary_unary(
                '/grpc.tradeapi.v1.Securities/GetSecurities',
                request_serializer=grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesRequest.SerializeToString,
                response_deserializer=grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesResult.FromString,
                )


class SecuritiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSecurities(self, request, context):
        """Securities table.
        Справочник инструментов.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecuritiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSecurities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSecurities,
                    request_deserializer=grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesRequest.FromString,
                    response_serializer=grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Securities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Securities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSecurities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Securities/GetSecurities',
            grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesRequest.SerializeToString,
            grpc_dot_tradeapi_dot_v1_dot_securities__pb2.GetSecuritiesResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)