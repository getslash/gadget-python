Using Gadget
============

Setting Up
----------

To use gadget you need to setup a context, helping you control the various configuration options affecting its runtime. For the simplest use case, just include:

.. code-block:: python

       >>> import gadget
       >>> with gadget.Setup():
       >>>    ... # your code here

Logging Operations
------------------

.. code-block:: python

       >>> with gadget.Setup():
       ...     ...
       ...     gadget.log_operation('setup', 'db1', {'use_transactions': True})

The code above will log that an operation called *setup* ran on an entity named *db1*, and as extra parameters would include ``{'use_transactions': True}``.
