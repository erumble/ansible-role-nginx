nginx
=========

Install and configure nginx

Requirements
------------

- none

Role Variables
--------------

For now, look in [defaults/main.yml](defaults/main.yml)

Dependencies
------------

- none

Installation
------------

Add the following to `requirements.yml`:

    - src: https://github.com/erumble/ansible-role-nginx
      name: erumble.nginx

Then run `ansible-galaxy install -r requirements.yml`

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: erumble.nginx }

Testing
-------

This role is tested on Docker containers through the use of Molecule, and Testinfra.  
The Vagrantfile in this repo is used to provision a VM for local testing.

To run the test suite:
    
    git clone git@github.com:erumble/ansible-role-nginx.git
    cd ansible-role-nginx
    vagrant up
    vagrant ssh -c 'cd /src/ansible-role-nginx && molecule test'

More information can be found at:  
- https://www.vagrantup.com/
- https://www.docker.com/
- http://molecule.readthedocs.io/en/master/index.html
- http://testinfra.readthedocs.io/en/latest/

License
-------

BSD

Author Information
------------------

meh

