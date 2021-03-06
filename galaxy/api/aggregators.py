# (c) 2012-2016, Ansible by Red Hat
#
# This file is part of Ansible Galaxy
#
# Ansible Galaxy is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by
# the Apache Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Ansible Galaxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Apache License for more details.
#
# You should have received a copy of the Apache License
# along with Galaxy.  If not, see <http://www.apache.org/licenses/>.

import django.db.models.aggregates

# Usage (to retrieve objects with highest average, NULLs become zeroes and are last):
# MyModel.objects.annotate(average=AvgWithZeroForNull('other_model__field_name')).order_by('-average')

class AvgWithZeroForNull(django.db.models.aggregates.Avg):
    template = 'COALESCE(%(function)s(%(field)s), 0)'
    name = 'AvgWithZeroForNull'
django.db.models.aggregates.AvgWithZeroForNull = AvgWithZeroForNull
