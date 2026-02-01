"""The `tii-client` package"""

import importlib.metadata as im

__version__ = im.version(__package__)

from .tii_client import Client
from qibo_client.qibo_job import QiboJob, QiboJobStatus
