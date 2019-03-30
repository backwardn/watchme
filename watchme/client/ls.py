'''

Copyright (C) 2019 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''

from watchme.command import list_watchers
from watchme.logger import bot

def main(args, extra):
    '''list installed watchers
    '''    
    list_watchers(args.base)
