#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD95AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DOC', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 5},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'LIN', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'PIA', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'MEA', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'COM', MIN: 0, MAX: 9},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
