"""Shared entity helpers."""

from __future__ import annotations

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import PhilipsDataUpdateCoordinator

class PhilipsEntity(CoordinatorEntity[PhilipsDataUpdateCoordinator]):
    """Base entity."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: PhilipsDataUpdateCoordinator, key: str):
        super().__init__(coordinator)
        self._key = key
        self._attr_unique_id = f"{coordinator.host}_{key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, coordinator.host)},
            "name": coordinator.device_name,
            "manufacturer": "Philips",
            "model": "AC2889/10",
        }
