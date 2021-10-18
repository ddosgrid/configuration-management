# LCN Demo setup

## Setup
This had to be done to run the demo on a Ubuntu 21.04 host machine:

```
# Install virtualbox and vagrant
sudo apt-get update && sudo apt-get install vagrant virtualbox -y

# Install ansible
python3 -m pip install --user ansible

# Install ansible modules to run the playbook
ansible-galaxy collection install community.general --force
ansible-galaxy install geerlingguy.docker

# Clone this repo
git clone --branch lcn-demo https://github.com/ddosgrid/configuration-management.git lcn-demo-playbook
cd lcn-demo-playbook

# Create machines and provision them
vagrant up
```
## Usage
Just navigate to `http://10.0.1.2:8081/ddosgrid` and `http://10.0.1.3:8081/ddosgrid`.
