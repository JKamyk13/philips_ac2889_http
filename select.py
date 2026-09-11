"""Select entities."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity

from .const import FUNCTIONS, FUNCTION_NAMES, MODES, MODE_NAMES
from .entity import PhilipsEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([
        PhilipsModeSelect(coordinator),
        PhilipsFunctionSelect(coordinator),
    ])


class PhilipsModeSelect(PhilipsEntity, SelectEntity):
    _attr_name = "Tryb"
    _attr_options = list(MODES)

    def __init__(self, coordinator):
        super().__init__(coordinator, "mode")
        self._attr_icon = "mdi:air-filter"

    @property
    def current_option(self):
        return self.coordinator.data.get("mode")

    async def async_select_option(self, option):
        if option in MODES:
            await self.coordinator.async_set_values({"mode": option})


class PhilipsFunctionSelect(PhilipsEntity, SelectEntity):
    _attr_name = "Funkcja"
    _attr_options = list(FUNCTIONS)

    def __init__(self, coordinator):
        super().__init__(coordinator, "function")
        self._attr_icon = "mdi:air-purifier"

    @property
    def current_option(self):
        return self.coordinator.data.get("func")

    async def async_select_option(self, option):
        if option in FUNCTIONS:
            await self.coordinator.async_set_values({"func": option})
