Front
======
Also know as leading underscore.  This case is focused on a single leading underscore. Double will be covered later.

.. image:: _static/py_private.png
   :width: 600

Python specification
--------------------
Weak “internal use” indicator. E.g. from M import * does not import objects whose names start with an underscore.

Convention
__________

Function, methods, classes, module level variables
--------------------------------------------------

Indicate that this things are for internal use.

- For libraries it's a good way to reduce maintenance cost.

  - When you change public method you are responsible for "fixing" it's usage.
  - When you change internal methods it's their problems, you should not care.
  - When you review public attributes, you should think about business (context where this class is used), if it works but  looks strange it's a valid reason for block the review. If internal method is working but look strange, this could be  refactored later.
  - If you have strict rules about documenting supported by linters, you could save time and not documenting internal things, linters respect leading underscore.
  - It's easy to keep module boundaries, linter will complain about violations.

- For code that is not a library this is not so important, but still a good thing to have.

Couple of simple rules:
 - Always start from internal
 - When you need to make it public, think if you really need it!, and do it. This is a really simple refactoring that touches a single file.


Argument names
--------------
Argument is not used, this might be useful when you implement some interface or work with external code.
Linting tools do not complain on such unused variables.


Example
_______

.. literalinclude:: ../example/front.py
   :language: Python


The main candidates for internal methods are code reuse and code extracting function to make code more readable.


Big classes are not that easy to read.

.. literalinclude:: ../example/many_lines_1.py
   :language: Python

Splitting this to chunks make thing simpler.

.. literalinclude:: ../example/many_lines_2.py
   :language: Python
