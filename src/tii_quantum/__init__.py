"""The `tii-quantum` package"""

import importlib.metadata as im

__version__ = im.version(__package__)

from qibo_client.qibo_job import QiboJob, QiboJobStatus

from .tii_client import Client
