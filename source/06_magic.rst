Magic
=====
Double underscore at the start and end

Methods that use it called magic or dundr (double underscore)

.. image:: _static/py_hat.png
   :width: 600


Python specification
--------------------
Yes, this is part of Python specification

Convention
__________

Think twice before adding an own one. This might be confusing.

You should not call this methods directly outside of the method.

`str(Foo) != Foo.__str__()`


Example
_______

Attributes that come from the box:

.. literalinclude:: ../example/dundr_predefined.py
   :language: Python


Attributes that defined you class behaviour for base Python usage:

.. literalinclude:: ../example/dundr_methods.py
   :language: Python
