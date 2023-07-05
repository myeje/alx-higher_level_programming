#!/usr/bin/python3
"""Module that multiplies 2 matrices by using NumPy module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - return multipies of 2 matrices
    @m_a: first matrix
    @m_b: second matrix
    Return: multiplication of matrices
    """
    return (np.matmul(m_a, m_b))
