# -*- coding: utf-8 -*-
#
# ITerativ GmbH
# http://www.iterativ.ch/
#
# Copyright (c) 2012 ITerativ GmbH. All rights reserved.
#
# Created on May 10, 2012
# @author: Daniel Egger <daniel.egger@gmail.com>, Daniel Egger <daniel.egger@gmail.com>

from fabric.api import env
from vagrant.vagrant import *

env.rsync_exclude.remove('*.dat')
env.rsync_exclude = env.rsync_exclude + ['media/']


from deployit.fabrichelper.common import *
