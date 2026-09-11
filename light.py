"""Light entity for the purifier display."""

from __future__ import annotations

from homeassistant.components.light import ColorMode, LightEntity

from .entity import PhilipsEntity


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([PhilipsAC2889Light(coordinator)])


class PhilipsAC2889Light(PhilipsEntity, LightEntity):
    """Control the purifier display brightness."""

    _attr_name = "Oświetlenie"
    _attr_supported_color_modes = {ColorMode.BRIGHTNESS}
    _attr_color_mode = ColorMode.BRIGHTNESS

    def __init__(self, coordinator):
        super().__init__(coordinator, "light")
        self._attr_icon = "mdi:led-on"

    @property
    def is_on(self):
        return self._brightness_percent > 0

    @property
    def brightness(self):
        return round(self._brightness_percent * 255 / 100)

    @property
    def _brightness_percent(self):
        try:
            return max(0, min(100, int(self.coordinator.data.get("aqil", 0))))
        except (TypeError, ValueError):
            return 0

    async def async_turn_on(self, *args, **kwargs):
        brightness = kwargs.get("brightness")
        if brightness is None:
            brightness_percent = self._brightness_percent or 100
        else:
            brightness_percent = round(max(0, min(255, brightness)) * 100 / 255)
        await self.coordinator.async_set_values({"aqil": brightness_percent})

    async def async_turn_off(self, *args, **kwargs):
        await self.coordinator.async_set_values({"aqil": 0})

    async def async_set_brightness(self, brightness):
        brightness_percent = round(max(0, min(255, brightness)) * 100 / 255)
        await self.coordinator.async_set_values({"aqil": brightness_percent})
