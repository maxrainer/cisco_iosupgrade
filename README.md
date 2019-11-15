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
ansible-galaxy install -p roles maxrainer.cisco_iosupgrade
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

```
- hosts: ios
  connection: network_cli
  gather_facts: no
  roles:
    - maxrainer.cisco_iosupgrade
  vars:
    - ios_platform: c3560c405ex
    - ios_image_string: c3560c405ex-universalk9-mz.152-2.E9
    - ios_image_md5: e58fdcc94e989a6d07d140f0d5f6b6f3
    - ios_image_tar: c3560c405ex-universalk9-tar.152-2.E9.tar
    - ios_upload_server: 10.10.10.10
    - ios_upload_username: scp_user
    - ios_upload_password: changeme
```

## Flow Diagram 

![alt text](flow.jpg?raw=true "FlowDiagram")

License
-------

GNU GENERAL PUBLIC LICENSE

Author Information
------------------

mrainer@redhat.com
