from flask import Flask, jsonify, request
from .network_utils import NetworkUtils
import calendar
import time

ping_api = Flask("__name__")
CONST_ROUTE_PING = "/ping"
CONST_HOST_NAME = "host"
CONST_LINE_PROTOCOL_DATA = "line_protocol_data"


@ping_api.route(CONST_ROUTE_PING)
def handle_ping_request():
    host_name = request.args[CONST_HOST_NAME]
    if host_name is not None:
        return jsonify(perform_ping(host_name))
    return "no host name provided"


def perform_ping(host):
    output = {}
    interface_data = []
    interfaces = NetworkUtils.get_interfaces()
    for interface in interfaces:
        status = NetworkUtils.check_ping(interface, host)
        line_protocol_string = NetworkUtils.CONST_PING_DATA + "," + NetworkUtils.CONST_FIELD_INTERFACE + "=" + interface + \
                               " " + NetworkUtils.CONST_PING_STATUS + "=" + status + " " + str(
            calendar.timegm(time.gmtime()))
        interface_data.append(line_protocol_string)
    output[CONST_LINE_PROTOCOL_DATA] = interface_data
    return output
