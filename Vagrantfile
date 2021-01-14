# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.
Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.box = "debian/buster64"
  config.vm.network "forwarded_port", guest: 443, host: 443, guest_ip: "10.0.1.2"
  config.vm.network "private_network", ip: "10.0.1.2"

#  config.vm.network "public_network", ip: "192.168.88.212"
  config.vm.provider :virtualbox do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "4096", "--cpus", "2"]
  end

  # Disable the new default behavior introduced in Vagrant 1.7, to
  # ensure that all Vagrant machines will use the same SSH key pair.
  # See https://github.com/mitchellh/vagrant/issues/5005
  config.ssh.insert_key = false

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "pb.yml"
    ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
  end
end
