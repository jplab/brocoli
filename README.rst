===================================================================================
BRoCoLi - Package dealing with LImit ROots of COxeter groups (eternal Beta version)
===================================================================================

This package deals with limits roots of infinite Coxeter groups and related structures.
It allows to compute several related objects such as matrices representing the 
elements, roots, weights, and obtain properties of the representation. Further,
it allows to visualize the isotropic cone, the roots, the weights, the limit
roots, and the Tits cone in the affine space spanned by the simple roots.

This code's ultimate goal is to be merged into the Sagemath software.
Some tickets related to this project:

 - http://trac.sagemath.org/ticket/17798
 - http://trac.sagemath.org/ticket/16126
 - http://trac.sagemath.org/ticket/15703
 - http://trac.sagemath.org/ticket/16087

You can find the complete documentation at https://jplab.github.io/brocoli/doc/html/

Installation
------------

Local install from source
^^^^^^^^^^^^^^^^^^^^^^^^^

Download the tar ball source and run the following command in the brocoli folder::

    $ sage  -pip install --upgrade --no-index -v .

Install from PyPI
^^^^^^^^^^^^^^^^^^

TODO: distribute on PyPI.

Uninstall from source
^^^^^^^^^^^^^^^^^^^^^^

You can uninstall the brocoli package as follows, once in the brocoli folder::

    $ sage -pip uninstall .


Usage
-----

Once the package is installed, you can use it on Sage with::

    sage: from brocoli import *
    sage: M1 = CoxeterMatrix([[1,4,4],[4,1,4],[4,4,1]])
    sage: GR1 = GeometricRepresentationCoxeterGroup(M1);GR1
    Geometric representation of a Coxeter group of rank 3 with Coxeter matrix
    [1 4 4]
    [4 1 4]
    [4 4 1]

Documentation
-------------

The complete documentation is available at https://jplab.github.io/brocoli/doc/html

The ``html`` and ``pdf`` versions are also available in the ``docs/build``
folder.
