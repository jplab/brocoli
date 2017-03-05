# -*- coding: utf-8 -*-
r"""
Limit Roots of Coxeter Groups

This module provide tools to study the limit roots of Coxeter groups.


EXAMPLES ::

    sage: from sage_sample import answer_to_ultimate_question
    sage: answer_to_ultimate_question()
    42

REFERENCES:

.. [HGG] Douglas Adams
   *The Hitchhiker's Guide to the Galaxy*.
   BBC Radio 4, 1978.

AUTHORS:

- Jean-Philippe Labbé (2011-2017): initial implementation
- Vivien Ripoll (2012): added features
"""
from sage.combinat.combinat import catalan_number

def answer_to_ultimate_question():
    r"""
    Return the answer to the Ultimate Question of Life, the Universe,
    and Everything.

    This uses SageMath Deep Thought supercomputer.

    EXAMPLES ::

        sage: from sage_sample import answer_to_ultimate_question
        sage: answer_to_ultimate_question()
        42

    TESTS ::

        sage: answer_to_ultimate_question() == 42
        True
    """
    return catalan_number(5)
