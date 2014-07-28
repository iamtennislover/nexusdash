=========
NexusDash
=========

Program
=======
Nexus Dash

- A Django based monitoring web dashboard for Nexus machines. Simply drop-in the app and go!

Features
========

- A beautiful web-based dashboard for monitoring Nexus info

- Interactive graphs showing historical data of Nexus

- Live, on-demand monitoring of RAM, CPU, Load, Uptime, Disk Allocation, Interface Throughput and many more system stats

- Make your own Django App Plugin and easily add to this website
  

Installation
============
1) Install Dependencies using Conda
-----------------------------------

Follow these CLI commands to install all dependencies::

    $ # No need to sudo
    $ cd /tmp/
    $ # Install Miniconda
    $ wget http://repo.continuum.io/miniconda/Miniconda-3.5.5-Linux-x86_64.sh
    $ chmod +x Miniconda-3.5.5-Linux-x86_64.sh
    $ ./Miniconda-3.5.5-Linux-x86_64.sh
    $ 
    $ # Create a Python env
    $ conda create --name nexusdash
    $ source activate nexusdash
    $ conda install pip
    $ 
    $ # Download ./requirements.txt from source
    $ ## Use following args for pip if server doesn't allow SSL: --index-url http://pypi.gocept.com/simple/ --allow-all-external --timeout 60
    $ pip install -r requirements.txt


2) Start the Django Server
--------------------------

Follow these CLI commands to run the Django Server::

    $ source activate nexusdash
    $ # Key can be any string
    $ export SECRET_KEY=asdaduy7683ybhby
    $ # To run in Development env
    $ python manage.py runserver 0.0.0.0:5555 --noreload --settings="nexusdash.settings.local"
    $
    $ # To run in Production env
    $ python manage.py runserver 0.0.0.0:5555 --noreload --settings="nexusdash.settings.production"
    