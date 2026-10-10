"""Functions for retrieving TVMaze records."""

import requests

from tvsummary.models import ShowRecord

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"


def fetch_records(url=SOURCE_URL):
    """Download records and return them as ShowRecord objects."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Could not download records: {exc}") from exc

    if not isinstance(data, list):
        raise RuntimeError("Downloaded data is not a list of records.")

    return [ShowRecord(item) for item in data]
