# DDoSGrid Deployment
A collection of configuration to deploy all components related to DDoSGrid

## Requirements
One may either provision a remote host or setup a VM with these assets.
In any case, you will need:
* Port 443 needs to be publicly accessible on the target host 
* SSL certificate in assets folder (certificate.cert, certificate.key)
* Domain name
* Host OS that supports one of the options below. We tested on Debian Buster (10).
* The following two ansible collections are required, install them with sudo if your host requires such priviledge to deploy a VM with port 443:
  ```bash
  ansible-galaxy collection install community.general
  ```
  ```bash
  ansible-galaxy collection install geerlingguy.docker
  ```

a) For a **VM-based** deployment you will also require the following:
* Vagrant
* VM Provider, in the default configuration we use Virtualbox but you can reconfigure to use KVM for example
* Ansible

b) To simply provision an **existing host** (e.g. an existing VM) you will require:
* Ansible ([Official Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html#connecting-to-remote-nodes))
* Remote host accessible through Ansible

