# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
vagrantfile_api_version = "2"

# directory name is used for the VM hostname, and ansible role name
base_dir = File.basename(File.expand_path(File.dirname __FILE__))

# definitions for the machines provisioned by this vagrant file
box_params = {
  box: 'erumble/centos7-x64',
  hostname: "#{base_dir}.dev",
  playbook: 'vagrant/playbook.yml'
}

# make the vagrant machine(s)
Vagrant.configure(vagrantfile_api_version) do |config|
  config.vm.define box_params.fetch(:hostname) do |box|

    # specify the box, hostname, and ip address
    box.vm.box = box_params.fetch :box
    box.vm.hostname = box_params.fetch :hostname

    box.vm.provider 'virtualbox' do |v|
      v.memory = 1024
      v.cpus = 2
    end

    # mount the base dir in /src instead of /vagrant
    config.vm.synced_folder ".", "/vagrant", disabled: true
    config.vm.synced_folder ".", "/src/#{base_dir}"

    # provision the thing
    box.vm.provision :ansible do |ansible|
      ansible.playbook = box_params.fetch :playbook
    end

  end # config.vm.define
end # Vagrant.configure
