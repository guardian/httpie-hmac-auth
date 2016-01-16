httpie-hmac-auth
================

`HMAC <https://tools.ietf.org/html/rfc2104>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.


HTTP requests will be signed with a shared secret key using HMAC. The string to sign format is:

.. code-block:: bash

    <Method>\n
    <Content-MD5>\n
    <Content-Type>\n
    <Date>\n
    <URL>

Example String-to-sign

.. code-block:: bash

    POST
    vVqHE1k/uBRCoWe0FAh95g==
    application/json
    Tue, 12 Jan 2016 14:57:28 GMT
    /api/v1/avatars

Example Authorization Header with HMAC signature

.. code-block:: bash

    Authorization: HMAC XH+v0qhV4i/89y/DT2OOJx9Kjf3f/0j+w2aGZk625nU=

Installation
------------

.. code-block:: bash

    $ pip install httpie-hmac-auth

You should now see ``hmac`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=hmac --auth='client:secret' example.org

Examples
--------

To authenticate a client request when an access key is required by the server to lookup the shared secret:

.. code-block:: bash

    $ http --auth-type=hmac --auth="client:secret" example.org

To authenticate a client request when there is no requirement for a client to supply an access key:

.. code-block:: bash

    $ http --auth-type=hmac --auth=":secret" example.org

License
-------

Copyright (c) 2016 The Guardian. Available under the MIT License.
