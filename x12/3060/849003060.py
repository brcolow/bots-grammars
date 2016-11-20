from bots.botsconfig import *
from records003060 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'CF',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BRC', MIN: 1, MAX: 1},
    {ID: 'AAA', MIN: 0, MAX: 10},
    {ID: 'NTE', MIN: 0, MAX: 10},
    {ID: 'REF', MIN: 0, MAX: 12},
    {ID: 'PER', MIN: 0, MAX: 3},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'N1', MIN: 0, MAX: 50, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 1},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
    ]},
    {ID: 'CON', MIN: 0, MAX: 10000, LEVEL: [
        {ID: 'AAA', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PER', MIN: 0, MAX: 3},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'N1', MIN: 0, MAX: 50, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 3},
        ]},
        {ID: 'PAD', MIN: 0, MAX: 1000, LEVEL: [
            {ID: 'LIN', MIN: 0, MAX: 1},
            {ID: 'AAA', MIN: 0, MAX: 10},
            {ID: 'PID', MIN: 0, MAX: 200},
            {ID: 'MEA', MIN: 0, MAX: 40},
            {ID: 'UIT', MIN: 0, MAX: 5},
            {ID: 'QTY', MIN: 0, MAX: 5},
            {ID: 'AMT', MIN: 0, MAX: 2},
            {ID: 'RCD', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'CUR', MIN: 0, MAX: 1},
            {ID: 'SSS', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'CTT', MIN: 1, MAX: 1},
    {ID: 'AMT', MIN: 0, MAX: 5},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]