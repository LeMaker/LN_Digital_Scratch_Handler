LN_Digital_Scratch_Handler
==========================

Allows Scratch to control LN Digital products through MESH.

Install
=======

Dowdload the source code package from Lemaker Github, unzip::

    $ cd LN_Digital_Scratch_Handler

Manual Install `LN_Digital_Scratch_Handler` (for Python 3) with the following command::

    $ sudo python3 setup.py install

Manual Install `LN_Digital_Scratch_Handler` (for Python 2) with the following command::

    $ sudo python setup.py install

Use
===

First you must [enable Mesh in
Scratch](http://wiki.scratch.mit.edu/wiki/Mesh#Mesh_by_Modification_of_Scratch).

The shift-click the *Share* menu-item and select *Host Mesh*.

To save the modified scratch virtual image in local, you have to run Scratch with::

    $ sudo scratch

Now run the Scratch Handler with the Desktop icon::LN-Digital-Scratch-Handler, or

    $ cd /usr/local/bin
    $ sudo LN-Digital-Scratch-Handler

Scratch
-------

The handler will make available inputs 1 through 8 via the sensor values. If
you want to control LN Digital's outputs you must create a variable for
each pin named like so:

    LN-output1
    LN-output2
    LN-output3
    LN-output4
    LN-output5
    LN-output6
    LN-output7
    LN-output8
