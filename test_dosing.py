from unittest.mock import MagicMock
import pandas
import sys
from dosing import csv

ec = pandas.DataFrame({
    'ID': [1, 2, 3, 4],
    'RID': [1, 2, 3, 4],
    'USERID': [1, 2, 3, 4],
    'VISCODE': ['u1', 'u1', 'u3', 'u4'],
    'ECSDSTXT': [200, -4, 2, 200]
})

registry = pandas.DataFrame({
    'ID': [1, 2, 3, 4],
    'RID': [1, 2, 3, 4],
    'USERID': [1, 2, 3, 4],
    'SVDOSE': [-4, -4, 'Y', -4],
    'VISCODE': ['u1', 'u1', 'u3', 'u4']
})

def test_filter1():
    pandas.read_csv = MagicMock(side_effect=[
        registry,
        ec
    ])
    sys.argv = ['', 'u1', -4, 5]
    csv()
    with open('results.csv', 'r') as f:
        lines = f.readlines()
    assert len(lines) == 3

def test_filter2():
    pandas.read_csv = MagicMock(side_effect=[
        registry,
        ec
    ])
    sys.argv = ['', 'u1', 'Y', 5]
    csv()
    with open('results.csv', 'r') as f:
        lines = f.readlines()
    assert len(lines) == 1

def test_filter3():
    pandas.read_csv = MagicMock(side_effect=[
        registry,
        ec
    ])
    sys.argv = ['', 'u1', -4, 200]
    csv()
    with open('results.csv', 'r') as f:
        lines = f.readlines()
    assert len(lines) == 2
