Using Gadget
============

Logging Operations
------------------

.. code-block:: python

       >>> gadget.log_operation('setup', 'db1', {'use_transactions': True})

The code above will log that an operation called *setup* ran on an entity named *db1*, and as extra parameters would include ``{'use_transactions': True}``.

Logging Updates
---------------

.. code-block:: python

       >>> gadget.log_update('db1', {'connection_string': '...'})

Logging States
--------------

.. code-block:: python

       >>> gadget.log_state('db1', {'connected': True, 'num_records': 1000})
