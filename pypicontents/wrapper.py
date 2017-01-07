#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   This file is part of PyPIContents.
#   Copyright (C) 2016-2017, PyPIContents Developers.
#
#   Please refer to AUTHORS.rst for a complete list of Copyright holders.
#
#   PyPIContents is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   PyPIContents is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see http://www.gnu.org/licenses.

import os
import sys
import json

from pipsalabim.api.report import get_modules, get_packages

while 'patchedglobals' not in globals():
    try:
        from pypicontents.core.patches import patchedglobals
        from pypicontents.core.utils import s, u
    except ImportError:
        appdir = os.path.dirname(os.path.realpath(__file__))
        sys.path.append(os.path.dirname(appdir))

if __name__ == '__main__':

    if os.path.isdir(sys.argv[1]):
        setupdir = sys.argv[1]
        storepath = os.path.join(setupdir, 'store.json')
        os.chdir(setupdir)

        try:
            with open(storepath, 'w') as store:
                store.write(u(json.dumps({
                    'modules': get_modules(get_packages(setupdir)),
                    'cmdline': []})))
        except Exception as e:
            sys.stderr.write('%s: %s' % (type(e).__name__, str(e)))
    else:

        setuppath = sys.argv[1]
        setupdir = os.path.dirname(setuppath)

        env = patchedglobals()
        env.update({'__file__': setuppath})

        os.chdir(setupdir)
        sys.path.append(setupdir)

        try:
            with open(setuppath) as _sfile:
                exec(compile(s(_sfile.read()), setuppath, 'exec'), env)
        except Exception as e:
            sys.stderr.write('%s: %s' % (type(e).__name__, str(e)))
