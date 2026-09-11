"""Data coordinator using py-air-control's HTTP client."""

from __future__ import annotations

from datetime import timedelta
import logging
from typing import Any

from pyairctrl.http_client import HTTPAirClient

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)

def _client_status(host: str) -> dict[str, Any]:
    client = HTTPAirClient(host, debug=False)
    status = client.get_status()
    if not status:
        raise RuntimeError("Philips purifier returned no status")
    return dict(status)

def _client_set(host: str, values: dict[str, Any]) -> dict[str, Any] | None:
    client = HTTPAirClient(host, debug=False)
    return client.set_values(values)

def _client_filters(host: str) -> dict[str, Any] | None:
    client = HTTPAirClient(host, debug=False)
    return client.get_filters()

def test_connection(host: str) -> dict[str, Any]:
    return _client_status(host)

class PhilipsDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Poll the purifier over HTTP."""

    def __init__(self, hass: HomeAssistant, host: str, name: str):
        self.host = host
        self.device_name = name
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            return await self.hass.async_add_executor_job(
                _client_status, self.host
            )
        except Exception as err:
            raise UpdateFailed(f"HTTP communication failed: {err}") from err

    async def async_set_values(self, values: dict[str, Any]) -> None:
        try:
            await self.hass.async_add_executor_job(_client_set, self.host, values)
            await self.async_request_refresh()
        except Exception as err:
            raise UpdateFailed(f"Could not set purifier value: {err}") from err

    async def async_get_filters(self) -> dict[str, Any] | None:
        try:
            return await self.hass.async_add_executor_job(
                _client_filters, self.host
            )
        except Exception as err:
            _LOGGER.debug("Filter query failed: %s", err)
            return None
