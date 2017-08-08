#!/bin/bash

vars=`cat /etc/ansible/roles/elastic_base/pvars/elastic_subtype.extra`
ansible-playbook $@  /etc/ansible/playbook/elastic233.yml --extra-vars $vars
