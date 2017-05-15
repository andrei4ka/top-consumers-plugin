#    Copyright 2017, Tinkoff Bank, JSC .
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import re

from django.core import urlresolvers
from django.template.defaultfilters import linebreaksbr
from django.utils.http import urlencode
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from topconsumersplugin import api


def get_instance(sample):
    if hasattr(sample, "metadata"):
        return "%s" % sample.metadata['display_name']

    return _("Not available")

def get_instance_link(sample):
    try:
        return urlresolvers.reverse('horizon:project:instances:detail', args=(sample.metadata['instance_id'],))
    except urlresolvers.NoReverseMatch:
        return None

class MetricsTable(tables.DataTable):
    id = tables.Column("id",
                        verbose_name=_("ID"))
    resource = tables.Column("resource_id",
                        verbose_name=_("Resource"))
    instance_name = tables.Column(get_instance,
                         link=get_instance_link,
                         verbose_name=_("Instance name"))
    value = tables.Column("volume",
                         verbose_name=_("Value"))
    date = tables.Column("timestamp",
                         verbose_name=_("Date"))

    class Meta(object):
        name = "topconsumers"
        verbose_name = _("Top Consumers")
