import requests


def test_check_status_code_by_url(test_data):
    status_code = requests.Session().get(url=test_data["url"]).status_code
    assert status_code == test_data["status_code"]
