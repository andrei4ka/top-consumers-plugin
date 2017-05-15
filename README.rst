=================
TOP Consumers Horizon Dashboard
=================

Setup Instructions
==================
This instruction assumes that Horizon is already installed and it's installation
folder is <horizon>. Detailed information on how to install Horizon can be
found at http://docs.openstack.org/developer/horizon/quickstart.html#setup.


The installation folder of TOP Consumers Horizon Dashboard will be referred to as <top-consumers-plugin>.

The following should get you started
============

1. Install module::

    $ git clone https://github.com/andrei4ka/top-consumers-plugin.git
    $ sudo python setup.py sdist
    $ sudo pip install dist/topconsumersplugin-*.tar.gz

2. Collect and Compress the static::

    $ python <horizon>/openstack_dashboard/manage.py compress
    $ python <horizon>/openstack_dashboard/manage.py collectstatic --noinput

3. Copy files to Horizon tree::

    $ cp /topconsumersplugin/enabled/_31000_topconsumersplugin.py <horizon>/openstack_dashboard/local/enabled/

4. When you're ready, you would need to either restart your apache::

    $ sudo service apache2 restart
