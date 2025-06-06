#!/usr/bin/env python
"""Copyright (c) 2018-2025 mundialis GmbH & Co. KG.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

First test
"""

__license__ = "GPLv3"
__author__ = "Carmen Tawalika"
__copyright__ = "Copyright 2025 mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

import pytest
from flask import make_response

from actinia_rest_lib.resource_base import ResourceBase

@pytest.mark.unittest
def test_resource_base():
    """Test for tranform_input function."""

    class TestResource(ResourceBase):
        """Get something for test"""

        def get(self):
            """Get something."""
            return make_response("something", 200)

    assert (
        'location_deprecated_decorator' in
        [i.__name__ for i in TestResource.decorators]
    ), "Decorator 'location_deprecated_decorator' not found in TestResource.decorators"
