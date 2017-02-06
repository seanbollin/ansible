#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Sean Bollin <sean@sean-bollin.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: conan
short_description: Manages C/C++ packages with Conan
version_added: "2.2"
description:
    - Manages C/C++ packages with Conan
    -
    -
author: "Sean Bollin (@seanbollin)"
requirements:
    - "python >= 2.7"
options:
    group_id:
        description:
            - The Maven groupId coordinate
        required: true
'''

EXAMPLES = '''
# Run conan
- conan:
    group_id: junit
    artifact_id: junit
    dest: /tmp/junit-latest.jar
'''


from ansible.module_utils.basic import *


def main():
    module = AnsibleModule(
        argument_spec=dict()
    )

    # module.fail_json(msg="Something fatal happened")
    module.exit_json(changed=True, something_else=12345)

if __name__ == '__main__':
    main()
