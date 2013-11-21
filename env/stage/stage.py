# -*- coding: utf-8 -*-
#
# ITerativ GmbH
# http://www.iterativ.ch/
#
# Copyright (c) 2012 ITerativ GmbH. All rights reserved.
#
# Created on Mar 13, 2012
# @author: maersu <me@maersu.ch>

from fabric.api import env
from deployit.fabrichelper.servicebase import UwsgiService, NginxService, CeleryService
from deployit.fabrichelper.environments import EnvTask


class StageEnv(EnvTask):
    """
    Use stage environment
    """
    name = "stage"

    def run(self):
        env.hosts = ['gurten.iterativ.ch']
        env.env_name = 'stage'
        env.services = [UwsgiService, NginxService, CeleryService]
        env.project_name = '{{ project_name }}'
        env.remote_virtualenv = '/srv/www/{{ project_name }}/stage/{{ project_name }}-env'
        env.server_names = ['{{ project_name }}.gurten.iterativ.ch']
        env.settings_module = '{{ project_name }}.settings.stage'
        env.nginx_no_follow = True
        env.requirements_file = 'requirements/production.txt'
        env.puppet_branch_name = 'ubuntu1204'


stage_env = StageEnv()
