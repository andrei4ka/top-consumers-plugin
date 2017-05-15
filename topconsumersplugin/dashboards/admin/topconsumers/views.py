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

from tables import MetricsTable
from horizon import messages
from horizon import exceptions

from horizon import tables
from openstack_dashboard import api
from datetime import datetime, timedelta

import logging
import pprint

LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = MetricsTable
    template_name = 'admin/topconsumers/index.html'

    def get_data(self):
        client = api.ceilometer.ceilometerclient(self.request)

        meter = self.request.GET.get('meter', 'disk.device.write.bytes.rate')
        dt = datetime.now() - timedelta(minutes=self.request.GET.get('period', 5))
        limit = self.request.GET.get('limit', 30)
        f = '{"and": [{"=": {"meter": "%s"}}, {">": {"timestamp": "%s"}}, {">": {"volume": 1024000}}]}' % (meter, dt)
        o = '[{"volume":"desc"}]'
        metrics = client.query_samples.query(filter=f, orderby=o, limit=limit)

        return metrics

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            meters = api.ceilometer.Meters(request=self.request,
                                           ceilometer_meter_list=api.ceilometer.meter_list(self.request))
            if not meters:
                msg = "There are no meters defined yet."
                messages.warning(self.request, msg)

            needle_meters = [
                'disk.device.read.bytes',
                'disk.device.read.bytes.rate',
                'disk.device.read.requests',
                'disk.device.read.requests.rate',
                'disk.device.write.bytes',
                'disk.device.write.bytes.rate',
                'disk.device.write.requests',
                'disk.device.write.requests.rate',
            ]
            context['meters'] = {
                'nova_meters': meters._list(only_meters=needle_meters),
            }
        except Exception:
            exceptions.handle(self.request, 'Unable to retrieve meters.')

        return context
