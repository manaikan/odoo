#!/usr/bin/env python3

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
from odoo.cli import main

main()
