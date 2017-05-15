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

# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'topconsumerspanel'

# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'admin'

PANEL_GROUP = 'admin'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'topconsumersplugin.dashboards.admin.topconsumers.panel.TopConsumersPanel'

# A list of applications to be prepended to INSTALLED_APPS
ADD_INSTALLED_APPS = ['topconsumersplugin']

# A list of AngularJS modules to be loaded when Angular bootstraps.
ADD_ANGULAR_MODULES = []

# Automatically discover static resources in installed apps
AUTO_DISCOVER_STATIC_FILES = True

# A list of js files to be included in the compressed set of files
ADD_JS_FILES = []

# A list of scss files to be included in the compressed set of files
ADD_SCSS_FILES = []
