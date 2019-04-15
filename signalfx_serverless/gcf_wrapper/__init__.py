# Copyright (C) 2019 SignalFx, Inc. All rights reserved.

from .. import serverless_common
from ..version import name, version

from . import utils

fields = utils.get_fields()
serverless_common.configure('gcf', fields)
    

# backwards compatibility
def wrapper(*args, **kwargs):
    return serverless_common.wrapper(*args, **kwargs)


def emits_metrics(*args, **kwargs):
    return serverless_common.emits_metrics(*args, **kwargs)


def is_traced(*args, **kwargs):
    return serverless_common.is_traced(*args, **kwargs)


# less convenient method
def send_metric(counters=[], gauges=[]):
    serverless_common.send_metric(counters, gauges)


# convenience method
def send_counter(metric_name, metric_value=1, dimensions={}):
    serverless_common.send_counter(metric_name, metric_value, dimensions)


# convenience method
def send_gauge(metric_name, metric_value, dimensions={}):
    serverless_common.send_gauge(metric_name, metric_value, dimensions)
