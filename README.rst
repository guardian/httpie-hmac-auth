httpie-hmac-auth
================

`HMAC <https://tools.ietf.org/html/rfc2104>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

Installation
------------

.. code-block:: bash

    $ pip install httpie-hmac-auth

You should now see ``hmac`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=hmac --auth=':secret' example.org

Examples
--------

.. code-block:: bash

    $ http -v --pretty all --auth-type=hmac --auth=":secret" :8900/moderation/discussions X-Forwarded-Proto:https

    $ http -v --pretty all --auth-type=hmac --auth=":secret" POST :8900/moderation/antispam/foo X-Forwarded-Proto:https

License
-------

Copyright (c) 2016 The Guardian. Available under the MIT License.
