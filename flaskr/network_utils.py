import os
import subprocess
import re
import calendar
import time


class NetworkUtils:
    """ get lists of all the available network interfaces"""
    CONST_PING_COUNT = 2
    INTERFACES_COMMAND = "ip link show"
    CONST_PING_DATA = "ping_data"
    CONST_FIELD_INTERFACE = "interface"
    CONST_PING_STATUS = "status"
    CONST_STATUS_SUCCESSFUL = "successful"
    CONST_STATUS_UNSUCCESSFUL = "unsuccessful"
    CONST_TIMESTAMP = "timestamp"

    @staticmethod
    def get_interfaces():
        interfaces = []
        with subprocess.Popen(['ip', 'link', 'show'], stdout=subprocess.PIPE) as proc:
            data = proc.stdout.read().decode()
        filtered_data = re.findall("\:.*\: <", data)
        if filtered_data is None or len(filtered_data) == 0:
            print("No network Interfaces found")
            return
        for interface in filtered_data:
            full_name = re.sub("[\:,<]", "", interface).strip()
            interfaces.append(full_name)
        return interfaces

    @staticmethod
    def check_ping(interface_name, host_name):
        with subprocess.Popen(["ping", "-I", interface_name, "-c", "3", host_name], stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE) as proc:
            error = proc.stderr.read().decode()
            if error is not None and len(error) > 0:
                return NetworkUtils.CONST_STATUS_UNSUCCESSFUL
            data = proc.stdout.read().decode()
            packet_loss_string = re.findall("[0-9]*\% packet loss", data)
            if packet_loss_string is not None and len(packet_loss_string) > 0:
                net_loss = re.sub("% packet loss", "", packet_loss_string[0])
                if net_loss.strip() == "0":
                    return NetworkUtils.CONST_STATUS_SUCCESSFUL
            return NetworkUtils.CONST_STATUS_UNSUCCESSFUL



