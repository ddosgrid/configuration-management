# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.
Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.define "left" do |left|
    left.vm.box = "debian/buster64"
    left.vm.network "forwarded_port", guest: 8080, host: 8080, guest_ip: "10.0.1.2"
    left.vm.network "forwarded_port", guest: 8081, host: 8081, guest_ip: "10.0.1.2"
    left.vm.network "private_network", ip: "10.0.1.2"

    left.vm.define "ddosgrid-v2"
    left.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "4096", "--cpus", "2"]
    end

    # Disable the new default behavior introduced in Vagrant 1.7, to
    # ensure that all Vagrant machines will use the same SSH key pair.
    # See https://github.com/mitchellh/vagrant/issues/5005
    left.ssh.insert_key = false

    left.vm.provision "ansible" do |ansible|
      ansible.verbose = "v"
      ansible.playbook = "playbook-demo-grid-left.yml"
      ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/python3",
        # OVERWRITE THIS:
        fqdn: "test.vonderassen.com"
      }
    end
  end

  config.vm.define "right" do |right|
    right.vm.box = "debian/buster64"
    right.vm.network "forwarded_port", guest: 8080, host: 8090, guest_ip: "10.0.1.3"
    right.vm.network "forwarded_port", guest: 8081, host: 8091, guest_ip: "10.0.1.3"
    right.vm.network "private_network", ip: "10.0.1.3"

    right.vm.define "ddosgrid-v2"
    right.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "4096", "--cpus", "2"]
    end

    # Disable the new default behavior introduced in Vagrant 1.7, to
    # ensure that all Vagrant machines will use the same SSH key pair.
    # See https://github.com/mitchellh/vagrant/issues/5005
    right.ssh.insert_key = false

    right.vm.provision "ansible" do |ansible|
      ansible.verbose = "v"
      ansible.playbook = "playbook-demo-grid-right.yml"
      ansible.extra_vars = {
        ansible_python_interpreter: "/usr/bin/python3",
        # OVERWRITE THIS:
        fqdn: "test.vonderassen.com"
      }
    end
  end
end
