# DDoSGrid Deployment
A collection of configuration to deploy all components related to DDoSGrid

## Requirements
One may either provision a remote host or setup a VM with these assets.
In any case, you will need:
* Port 443 needs to be publicly accessible on the target host 
* SSL certificate in assets folder (certificate.cert, certificate.key)
* Domain name
* The following two ansible collections are required, install them with sudo if your host requires such priviledge to deploy a VM with port 443:
  ```bash
  ansible-galaxy collection install community.general
  ```
  ```bash
  ansible-galaxy install geerlingguy.docker
  ```
* Host OS that supports one of the options below. We tested on Debian Buster (10):

a) For a **VM-based** deployment you will also require the following:
* Vagrant
* VM Provider, in the default configuration we use Virtualbox but you can reconfigure to use KVM for example
* Ansible

b) To simply provision an **existing host** (e.g. an existing VM) you will require:
* Ansible ([Official Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html#connecting-to-remote-nodes))
* Remote host accessible through ssh

## Deployment
* Place your SSL cert and key into the `assets` folder
* Make sure that your host is reachable through your domain (E.g. by PINGing it)

a) To deploy with Vagrant, simply replace the `fqdn` variable in the provisioning block of the `Vagrantfile` and call vagrant up. This will build and install services including Docker and provision/configure them
b) To deploy with ansible we recommend to create a [hosts]() file pointing to the host you want to provision. Make sure to that `ansible_python_interpreter: /usr/bin/python3` is set for the host. Then you can simply call `ansible-playbook -i hosts playbook.yml`. Since you are calling Ansible interactively you will be prompted for your domain name (FQDN) which is then used for the configuration of the services.
