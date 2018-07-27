# Unit testing with Python

This was a talk given to [The Python User Group of
Redmond](https://www.redmondpython.com/) on 26 July 2018.

To view this presentation:
[reveal.js](https://github.com/hakimel/reveal.js/) submodule:

1. Install [Node.js](http://nodejs.org/)

1. If cloning this repo for the first time:
   ```sh
   $ git clone --recurse-submodules
   ```
   If you already cloned but didn't use the `--recurse-submodules`:
   ```sh
   $ git submodule init
   ```

1. Install all the reveal.js requirements (requires
   [node.js](https://nodejs.org/en/)):
   ```sh
   $ cd reveal.js
   $ npm install
   ```

1. Run the presentation:
   ```
   $ npm start -- --root=..
   ```


## Copyright

Copyright (C) 2018 Albert Hopkins, <marduk@letterboxes.org>
