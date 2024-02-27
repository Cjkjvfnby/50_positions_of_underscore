Name mangling
=============
Double underscore before the method name.

Python specification
--------------------
Yes

Lets see this on example:

Accidental override
___________________
.. literalinclude:: ../example/name_mangling_01.py
   :language: Python

`_get` method was unintentionally overridden.

There are two version of cause:
_get was added to Foo after it was published and used.
_get was added to Boo without checking all non public methods.


Naive protection
________________

.. literalinclude:: ../example/name_mangling_02.py
   :language: Python

It works but ugly and hard to maintain.

Using Python specification
__________________________

.. literalinclude:: ../example/name_mangling_03.py
   :language: Python

This name is converted to the `_<class><method>` in the instance dictionary and when you access it.
Then current class is owner for the method.  When you call if from the Foo it foo, when you try to call it from Boo,
if will try to get _Boo__get.


Convention
__________

If you class is meant to be inherited, use it!
This is recommended way to avoid override thing by accident.
It does not protect from calling it, you just need to use mangled name for that.

There is not reason to use it for classes that are not used as parents, single underscore is enough.


Example
_______
.. literalinclude:: ../example/all.py
   :language: Python
