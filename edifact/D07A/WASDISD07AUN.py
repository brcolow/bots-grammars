#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD07AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'LOC', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
        {ID: 'GOR', MIN: 0, MAX: 1},
    ]},
    {ID: 'TDT', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 2},
        {ID: 'MEA', MIN: 0, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'QTY', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 3},
        ]},
    ]},
    {ID: 'DGS', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'SGP', MIN: 0, MAX: 999},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'NAD', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
