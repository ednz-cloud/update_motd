Update MOTD
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role enables you to set a cool motd on **debian-based** distributions using neofetch.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/update_motd.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
update_motd_filename: "00-motd-neofetch"
```
This variable sets the name for the file that'll be created in `/etc/update-motd.d` on the target system.

```yaml
update_motd_print_info:
  - name: "CPU"
    module: "cpu"
```
This variable is the list of modules that you want to enable in your motd. It references the neofetch modules. The `name` is the title that'll be appended to each module.

All of the other variables are used for the configuration file of neofetch that'll sit in `/etc/profile.d/motd/cfg` by default.
These are one to one identical to the neofetch modules. Documentation on the different settings can be found in the `files/documentation` file. It's just a copy on the default neofetch config file.

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires `ednxzu.manage_apt_packages` in order to make sure that neofetch is installed.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.update_motd
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.