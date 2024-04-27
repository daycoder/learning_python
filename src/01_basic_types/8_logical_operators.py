"""
┌────────────────────────────────────────────────────────────┐
│                     Logical operators                      │
├──────────┬─────────┬───────────────────────────────────────┤
│ Operator │ Syntax  │              Description              │
├──────────┼─────────┼───────────────────────────────────────┤
│   and    │ x and y │ True if both x and y are True         │
│    or    │ x or y  │ True if either x or y are True        │
│   not    │ x and y │ True if x is False, False if x isTrue │
└──────────┴─────────┴───────────────────────────────────────┘

Precedence: NOT > AND > OR

This means NOT is evaluated first, then AND, then OR.

>>> not False and True
True

To invert the result of an and, use NOT with parentheses
>>> not (False and True)
False

Similarly, AND is evaluated before OR
>>> False and False or True
True

Use parantheses to evaluate the OR first
>>> False and (False or True)
False


"""







# How did I make that table ?
from tableutil import Table, HEADING, JUSTIFY, Justify

OPERATOR = 'Operator'
SYNTAX = 'Syntax'
DESCRIPTION = 'Description'

logical_operators = Table(title="Logical operators",
                          row_numbers=False,
                          headings=[{HEADING: OPERATOR, JUSTIFY: Justify.centre},
                                    {HEADING: SYNTAX},
                                    {HEADING: DESCRIPTION}],
                          rows=[{OPERATOR: "and",
                                 SYNTAX: 'x and y',
                                 DESCRIPTION: 'True if both x and y are True'},
                                {OPERATOR: "or",
                                 SYNTAX: 'x or y',
                                 DESCRIPTION: 'True if either x or y are True'},
                                {OPERATOR: "not",
                                 SYNTAX: 'x and y',
                                 DESCRIPTION: 'True if x is False, False if x is True'},
                                ])
print(logical_operators)
