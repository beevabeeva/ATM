Setup
=====
This page will guide you though downloading and installing ATM.

0. Requirements
---------------
Currently, ATM is only compatible with Python 2.7 and \*NIX systems, and `git
<https://git-scm.com/>`_ is required to download and update the software.

1. Clone the project
-----------------------
From the terminal, run::

    $ git clone https://github.com/hdi-project/atm.git ./atm


2. Install a database
-----------------------

ATM requires a SQL-like database to store information about datasets, dataruns,
and classifiers. It's currently compatible with the SQLite3 and MySQL dialects.
For first-time and casual users, we recommend installing SQLite::

    $ sudo apt-get install sqlite3

If you're planning on running large, distributed, or performance-intensive jobs,
you might prefer using MySQL. Run::

    $ sudo apt-get install mysql-server mysql-client

and following the instructions.

No matter which you choose, you'll need to install the mysql client developer
library in order for SQLAlchemy to work correctly::
    
    $ sudo apt-get install libmysqlclient-dev

3. Install Python dependencies
------------------------------

We recommend using `pip <https://pip.pypa.io/en/stable>`_ and `virtualenv
<https://virtualenv.pypa.io/en/stable/>`_ to make this process easier.::

    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv

Next, create the virtual environment and enter into it::

    $ virtualenv atm-env
    $ * see note below: install python-devel
    $ . atm-env/bin/activate
    (atm-env) $
    
    
**Note:**
        Python developement packages need to be installed. This can be done after activating your virtualenv, but BEFORE running `python setup.py install`
        Here is how to do that (from https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory):


For `apt` (**Ubuntu, Debian...**)::

        sudo apt-get install python-dev   # for python2.x installs
        sudo apt-get install python3-dev  # for python3.x installs
    
For `yum` (**CentOS, RHEL...**)::

    sudo yum install python-devel   # for python2.x installs
    sudo yum install python34-devel   # for python3.4 installs (substitute 34 for your version. E.g 3.6 = python36-devel


For `dnf` (**Fedora...**)::

    sudo dnf install python2-devel  # for python2.x installs
    sudo dnf install python3-devel  # for python3.x installs

For `zypper` (**openSUSE...**)::

    sudo zypper in python-devel   # for python2.x installs
    sudo zypper in python3-devel  # for python3.x installs

For `apk` (**Alpine...**)::

    # This is a departure from the normal Alpine naming
    # scheme, which uses py2- and py3- prefixes
    sudo apk add python2-dev  # for python2.x installs
    sudo apk add python3-dev  # for python3.x installs

For `apt-cyg` (**Cygwin...**)::

    apt-cyg install python-devel   # for python2.x installs
    apt-cyg install python3-devel  # for python3.x installs
    
    
The required packages are:

.. literalinclude:: ../../requirements.txt

Install them with pip::

    (atm-env) $ pip install -r requirements.txt

Or, if you want to use ATM as a library in other applications, you can install
it as a package. This will install the requirements as well::

    (atm-env) $ pip install -e . --process-dependency-links

You're all set. Head over to the `quick-start <quickstart.html>`_ section to create and
execute your first job with ATM.
