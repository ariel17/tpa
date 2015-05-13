=====
 TPA
=====

UTN FRBA - System design: 2nd group.

Install dependencies
====================

.. code-block:: bash

   ~/tpa$ sudo apt-get install python-pip
   ~/tpa$ pip install -r requirements.txt
  
Generate class diagram
======================

.. code-block:: bash

   ~/tpa/tpa$ python manage.py graph_models accounts health recipes auth -g -o docs/models.png
