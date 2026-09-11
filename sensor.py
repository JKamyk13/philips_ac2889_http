"""Sensor entities."""

from __future__ import annotations

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import PERCENTAGE, UnitOfTemperature, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from homeassistant.helpers.entity import EntityCategory

from .entity import PhilipsEntity

SENSORS = {
    "pm25": ("PM2.5", "mdi:blur", SensorDeviceClass.PM25, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER),
    "temp": ("Temperature", "mdi:thermometer", SensorDeviceClass.TEMPERATURE, UnitOfTemperature.CELSIUS),
    "rh": ("Humidity", "mdi:water-percent", SensorDeviceClass.HUMIDITY, PERCENTAGE),
    "iaql": ("Allergen Index", "mdi:allergy", None, None),
    "wl": ("Water Level", "mdi:water", None, PERCENTAGE),
}

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["philips_ac2889_http"][entry.entry_id]
    async_add_entities([
        PhilipsValueSensor(coordinator, key, *spec)
        for key, spec in SENSORS.items()
        if key in coordinator.data
    ])


class PhilipsValueSensor(PhilipsEntity, SensorEntity):
    """Dynamic Philips value sensor."""

    def __init__(self, coordinator, key, name, icon, device_class, unit):
        super().__init__(coordinator, f"sensor_{key}")
        self._attr_name = name
        self._attr_icon = icon
        self._attr_device_class = device_class
        self._attr_native_unit_of_measurement = unit

    @property
    def native_value(self):
        value = self.coordinator.data.get(self._key.replace("sensor_", ""))
        try:
            return float(value) if value is not None else None
        except (TypeError, ValueError):
            return value
