## Initial Setup

Install [Ruby](http://www.ruby-lang.org/en/) and make sure you have
[Bundler](http://gembundler.com/) installed.

    git clone git@github.com:yourcelf/yerk-base-install.git
    cd yerk-base-install
    bundle
    vagrant box add precise32 http://files.vagrantup.com/precise32.box

## Running Virtual Instances

    cd real # or imaginary
    # Startup
    vagrant up
    # SSH into machine
    vagrant ssh
    # ...
    # Shutdown
    vagrant halt
