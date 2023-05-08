#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2023 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for acls_health_check
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
docstring
"""

EXAMPLES = """

"""

RETURN = """
"""

from ansible.errors import AnsibleFilterError

ARGSPEC_CONDITIONALS = {}



    """ """
    interface_status_summary = {
        "total": len(health_facts.keys()),
        "up": 0,
        "down": 0,
        "admin_up": 0,
        "admin_down": 0,
    }
    for interface in health_facts.values():

        if "up" in interface.get("admin") or "Up" in interface.get("admin"):
            interface_status_summary["admin_up"] += 1
        else:
            interface_status_summary["admin_down"] += 1

        if "up" in interface.get("operational") or "Up" in interface.get(
            "operational"
        ):
            interface_status_summary["up"] += 1
        elif "down" in interface.get("operational") or "Down" in interface.get(
            "operational"
        ):
            interface_status_summary["down"] += 1
    return interface_status_summary


def health_check_view(*args, **kwargs):
    params = ["health_facts", "target"]
    data = dict(zip(params, args))
    data.update(kwargs)
    if len(data) < 2:
        raise AnsibleFilterError(
            "Missing either 'health facts' or 'other value in filter input,"
            "refer 'network.acls.health_check_view' filter plugin documentation for details",
        )
    return health_checks


def is_present(health_checks, option):
    for item in health_checks:
        if item["name"] == option:
            return item
    return None


class FilterModule(object):
    """health_check_view"""

    def filters(self):
        """a mapping of filter names to functions"""
        return {"health_check_view": health_check_view}