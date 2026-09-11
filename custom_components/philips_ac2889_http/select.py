"""Select entities."""

from __future__ import annotations

from homeassistant.components.select import SelectEntity

from .const import MODE_NAMES, MODES
from .entity import PhilipsEntity

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([PhilipsModeSelect(coordinator)])


class PhilipsModeSelect(PhilipsEntity, SelectEntity):
    _attr_name = "Mode"
    _attr_options = [MODE_NAMES[mode] for mode in MODES]

    def __init__(self, coordinator):
        super().__init__(coordinator, "mode")
        self._attr_icon = "mdi:air-filter"

    @property
    def current_option(self):
        mode = self.coordinator.data.get("mode")
        return MODE_NAMES.get(mode)

    async def async_select_option(self, option):
        mode = next(
            (mode for mode in MODES if MODE_NAMES[mode] == option),
            None,
        )
        if mode is not None:
            await self.coordinator.async_set_values({"mode": mode})
