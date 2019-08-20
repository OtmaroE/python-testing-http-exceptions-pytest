from unittest import mock
from unittest.mock import patch

import pytest
from requests import HTTPError

from main import make_request


@patch("main.requests")
def test_main_exception(mock_requests):
    exception = HTTPError(mock.Mock(status=404), "not found")
    mock_requests.get(mock.ANY).raise_for_status.side_effect = exception

    with pytest.raises(HTTPError) as error_info:
        make_request()
        assert error_info == exception
