"""Switch entities."""

from __future__ import annotations

from homeassistant.components.switch import SwitchEntity

from .entity import PhilipsEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([PhilipsChildLockSwitch(coordinator)])


class PhilipsChildLockSwitch(PhilipsEntity, SwitchEntity):
    _attr_name = "Child Lock"

    def __init__(self, coordinator):
        super().__init__(coordinator, "child_lock")
        self._attr_icon = "mdi:lock"

    @property
    def is_on(self):
        return str(self.coordinator.data.get("cl", "False")).lower() == "true"

    async def async_turn_on(self, **kwargs):
        await self.coordinator.async_set_values({"cl": True})

    async def async_turn_off(self, **kwargs):
        await self.coordinator.async_set_values({"cl": False})
