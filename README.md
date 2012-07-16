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

## Config variables

Variables are listed in the bash script "./config".  These variables are
available to either python scripts or bash scripts, and can be used in
templates for writing config files.

To use these variables in a bash script, simply:

    source ../config

at the top of your script.

To use the variables in a python script:

    from common import config

    print config.YERK_HELLO

To use the variables in a config file template, use `$VARNAME` in the template.  The name will be interpolated into the script if you use the `write_conf` utility provided in common.py:

    from common import write_conf

    write_conf("hello", "/tmp/hello.there")
