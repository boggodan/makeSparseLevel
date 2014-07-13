makeSparseLevel
===============

A while back I started writing a platformer in Java. I'm using PyxelEdit to make tilesets, which in turns are exported as xml tilemaps
specifying the gfx used for each tile on the map. Unfortunately PyxelEdit writes all the empty tiles into the xml as well, so if your
map has millions of tiles only some of which are used you're going to run out of memory.

This is a small script that takes in a pyxeledit tilemap .xml file and outputs another xml file containing only the used tiles and
their positions. You can then parse the file and save up tons of memory and disk space if your game world is mostly empty (which
is often the case).

Usage:

makeSparseLevel.py [xmlTilesetFile]

Output:

xmlTileSetFile_sparse.xml
