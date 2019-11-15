# Cisco IOS Image Upgrade

Upgrades Images on Cisco IOS Devices. Uses "archive" command. 

## Overview

This is an Ansible Role for network engineers and operators. It handles all necessary steps to Upgrade an IOS Image including Flash cleanup, Cisco Catalyst Stack support.
It uses IOS command: archive. 

## Prerequests

1) Cisco IOS Device supporting "archive" command
2) SCP Server

## Quick Start

1) Download the role from ansible-galaxy into your roles directory
```
ansible-galaxy install -p roles maxrainer.iosupgrade
```


## Role Variables

### should Ansible clean Flash from all images found and not needed? 
### does not delete the active image
ios_flash_clean_enabled: False

### Cisco CCO data
ios_image_string: binary_file_name  (do not add .bin here)
ios_image_md5: image_md5_checksum   (CCO provided checksum)
ios_image_tar: image_tarball        (CCO provided)
### SCP Credentials
ios_upload_server: 127.0.0.1        (SCP Server)
ios_upload_username: user           
ios_upload_password: changme
ios_upload_protocol: scp

# this is be needed for cleanup flash 
ios_platform: c2960x

# maybe changed
ios_verify_timeout: 90
debug: False 

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: cisco
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GNU GENERAL PUBLIC LICENSE

Author Information
------------------

mrainer@redhat.com
