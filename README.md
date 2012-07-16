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

Variables are listed in the bash script "./config".  Every variable must begin
with "YERK". These variables are available to either python scripts or bash
scripts, and can be used in templates for writing config files.

To use these variables in a bash script, simply:

    source ../config

at the top of your script.

To use the variables in a python script:

    from common import config

    print config.YERK_HELLO

To use the variables in a config file template, use `$VARNAME` in the template.  The name will be interpolated into the script if you use the `write_conf` utility provided in common.py:

    from common import write_conf

    write_conf("hello", "/tmp/hello.there")

## Design Overview

### 3 Tier Storage (1-1-1)

1. One secrets configuration file (for passwords, etc.).
2. One repository for scripts and configuration, i.e., this repository.
3. One blob repository to store all real-time data in one root directory.
   Symlinks are created to map to the system structure as needed.

This approach makes it very easy to move from one host system to another.

### Use Simple Scripts When Possible

The simplest install module is a single script. These scripts are generally
idempotent and can be run once or many times. An example would be
`apt-get update && apt-get -y upgrade`.

### Break Complicated Scripts Into Stages

More complicated install modules can broken into multiple scripts:

1. Install   - `apt-get install <foo>`
2. Prepare   - stop services, setup users, etc.
3. Configure - create/update configuration from templates
4. Copy      - copy files from backup or other store; generally only done once
5. Finalize  - start/restart services, etc.

During cold-install, the scripts are run once in order. An example of a script
that is generally only run once is the **copy** script.

Other scripts are often updated and run over and over on the production system.
An example would be the **configure** script that is run multiple times because
configuration changes often.

### Use Templating for Configuration

Use a Python string style template system for creating files.

## To Dos

- `real`
    - Install
        - Base System Setup (updates, SSH, firewall, etc.)
        - Install DjbDNS, Yerk DNS
        - Install Postfix, Mailman, Dovecot, etc.
        - Install Apache
    - Copy
        - `/var/mailboxes` - mail store
        - `/var/www` - www files
        - `/var/lib/mailman` - mailman
        - `/var/lib/postgresql` - db
