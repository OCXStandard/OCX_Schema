Naive XML Bindings for python dataclasses
=========================================

--------

xsdata
-----
We use the python package `xsData`_ to create conformance classes for the schema.
xsData is a complete data binding library for python allowing developers to access and
use XML and JSON documents as simple objects rather than using DOM.

.. _xsdata: https://xsdata.readthedocs.io/en/latest/

The code generator supports XML schemas, DTD, WSDL definitions, XML & JSON documents.
It produces simple dataclasses with type hints and simple binding metadata.

Features
-------
- Generate code from:
    - XML Schemas 1.0 & 1.1
    - WSDL 1.1 definitions with SOAP 1.1 bindings
    - DTD external definitions
    - Directly from XML and JSON Documents
    - Extensive configuration to customize output
    - Pluggable code writer for custom output formats
- Default Output:
    - Pure python dataclasses with metadata
    - Type hints with support for forward references and unions
    - Enumerations and inner classes
    - Support namespace qualified elements and attributes
- Data Binding:
    - XML and JSON parser, serializer
    - PyCode serializer
    - Handlers and Writers based on lxml and native xml python
    - Support wildcard elements and attributes
    - Support xinclude statements and unknown properties
    - Customize behaviour through config

Installation
------------

.. code-block::

   pip install xsdata[cli]

Usage
-----

.. code-block::

   xsdata --help
   Usage: xsdata [OPTIONS] COMMAND [ARGS]...

   xsdata command line interface.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  generate*    Generate code from xml schemas, webservice definitions and...

  download     Download a schema or a definition locally with all its...

  init-config  Create or update a configuration file.

Configuration
-------------

The configuration for the schema databinding can be defined in the file ``.xsdata.xml``, see the `xsData`_ documentation for a detailed description of the configuration options.

OCX schema specific configurations:

Package name
^^^^^^^^^^^^

.. code-block:: XML

    <Package>ocx_databinding</Package>

The schema dataclasses are written to a python package named ``ocx_datbinding``.

Namespace separation
^^^^^^^^^^^^^^^^^^^^

.. code-block:: XML

   <Structure>filenames</Structure>

Each namespace are output to separate files named after the ``XSD`` file.