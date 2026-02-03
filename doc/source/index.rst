.. tii-quantum documentation master file, created by
   sphinx-quickstart on Fri Dec 15 11:46:09 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

What is tii-quantum?
====================

TII-Quantum is the front end interface to TII Quantum Computing Cloud Platform.

The main purpose of the project is to create a client tool written in python
able to launch quantum computations through HTTP.

Installation instructions
=========================

Install first the package dependencies with the following commands.

We recommend to start with a fresh virtual environment to avoid dependencies
conflicts with previously installed packages.

.. code-block:: bash

   $ python -m venv ./env
   source activate ./env/bin/activate

The tii-quantum package can be installed through pip:

.. code-block:: bash

   pip install tii-quantum


Quick tutorial
==============

Once installed, the provider allows to run quantum circuit computations on the
remote server.

.. note::
   In order to run jobs on the remote cluster it is mandatory to own a validated
   account. Please, sign up to your preferred institution to obtain the needed
   token to run computations on the cluster.

The following example shows how to launch a simulation job.
Remember to replace `your token` string with your actual valid token
receive after registration.

.. code-block:: python

   >>> from tii_quantum import Client
   >>> import qibo
   >>> circuit = qibo.models.QFT(5)
   >>> client = Client("your token")
   >>> job = client.run_circuit(circuit, device="k2", project="personal", nshots=100)
   >>> result = job.result()
   >>> print(result)

The `device` name indicates the specific system or machine that will process the
job. The `project` name corresponds to the project or group to which the user
belongs and which will be charged for the service usage.

Content
=======

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

.. toctree::
    :maxdepth: 1
    :caption: Documentation links

    Qibo docs <https://qibo.science/qibo/stable/>
    Qibolab docs <https://qibo.science/qibolab/stable/>
    Qibocal docs <https://qibo.science/qibocal/stable/>
    Qibosoq docs <https://qibo.science/qibosoq/stable/>
    Qibochem docs <https://qibo.science/qibochem/stable/>
    Qibotn docs <https://qibo.science/qibotn/stable/>
    Qibo-cloud-backends docs <https://qibo.science/qibo-cloud-backends/stable/>

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
