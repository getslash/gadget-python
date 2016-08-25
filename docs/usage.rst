Using Gadget
============

Logging Operations
------------------

.. code-block:: python

       >>> gadget.log_operation('setup', 'db1', {'use_transactions': True})

The code above will log that an operation called *setup* ran on an entity named *db1*, and as extra parameters would include ``{'use_transactions': True}``.

.. note::
   entities of operations can be either a single string id, a list of ids, or a dictionary mapping entitiy *roles* to entity ids:

   .. code-block:: python

	  >>> gadget.log_operation('copy', {'source': '/tmp/file1.txt', 'target': '/tmp/file2.txt'})

.. note::
   entity ids are completely arbitrary, and it is the user's responsibility to make sure they are indeed unique in the log.

Logging Updates
---------------

.. code-block:: python

       >>> gadget.log_update('db1', {'connection_string': '...'})

Logging States
--------------

.. code-block:: python

       >>> gadget.log_state('db1', {'connected': True, 'num_records': 1000})
