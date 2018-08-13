About the Module Index
----------------------

.. _Travis: https://travis-ci.org/LuisAlejandro/pypicontents
.. _pypi.json: https://github.com/LuisAlejandro/pypicontents/blob/contents/pypi.json

In the `pypi.json`_ file (located in the ``contents`` branch) you will find a dictionary with all the packages registered
at the main PyPI instance, each one with the following information::

    {
        "pkg_a": {
            "version": [
                "X.Y.Z"
            ],
            "modules": [
                "module_1",
                "module_2",
                "..."
            ],
            "cmdline": [
                "path_1",
                "path_2",
                "..."
            ]
        },
        "pkg_b": {
             "...": "..."
        },
        "...": {},
        "...": {}
    }

This index is generated using Travis_. This is done by executing the ``setup.py`` file
of each package through a monkeypatch that allows us to read the parameters that were passed
to ``setup()``. Check out ``pypicontents/api/process.py`` for more info.

Use cases
~~~~~~~~~

.. _Pip Sala Bim: https://github.com/LuisAlejandro/pipsalabim

* Search which package (or packages) contain a python module. Useful to determine a project's ``requirements.txt`` or ``install_requires``.

::

    import json
    import urllib2
    from pprint import pprint

    pypic = 'https://raw.githubusercontent.com/LuisAlejandro/pypicontents/contents/pypi.json'

    f = urllib2.urlopen(pypic)
    pypicontents = json.loads(f.read())

    def find_package(contents, module):
        for pkg, data in contents.items():
            for mod in data['modules']:
                if mod == module:
                    yield {pkg: data['modules']}

    # Which package(s) content the 'django' module?
    # Output: 
    pprint(list(find_package(pypicontents, 'django')))

..

    Hint: Check out `Pip Sala Bim`_.

Known Issues
~~~~~~~~~~~~

#.  Some packages have partial or totally absent data because of some of these
    reasons:

    #. Some packages depend on other packages outside of ``stdlib``. We try to
       override these imports but if the setup heavily depends on it, it will fail anyway.
    #. Some packages are broken and error out when executing ``setup.py``.
    #. Some packages are empty or have no releases.

#.  If a package gets updated on PyPI and the change introduces or deletes
    modules, then it won't be reflected until the next index rebuild. You
    should check for the ``version`` field for consistency. Also, if you need a
    more up-to-date index, feel free to download this software and build your own
    index.