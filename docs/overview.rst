Overview
========

What is Gadget?
---------------
Gadget is a mechanism intended to improve the speed of investigating bugs from post-mortem logs.

Gadget operates by embedding specifically-marked log lines which can later be parsed. Log lines indicate important events in your flow, which you may be interested in finding later.

There are several types of events:

1. **Operation**: indicates that some action happened to or on some entity. It must contain the name of the entity and the name of the operation, and may contain other arbitrary parameters
2. **Update**: Indicates that a certain entity has been updated. It must contain the update data (but not necessarily the new state)
3. **State**: Indicates a new state for a given entity

What is ``gadget-python``?
--------------------------

``gadget-python`` is the Python library used to emit Gadget-targeted log lines and parse them.
