import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_UPDATE_INTERVAL
#from esphome.core.entity_helpers import inherit_property_from

#from .const import CONF_ONE_WIRE_BUS, CONF_READ_ROM_COMMAND, DEFAULT_IBUTTON_READ_ROM_COMMAND

CODEOWNERS = ["@SergeyKa2021"] 
#DEPENDENCIES = ["one_wire"]
#MULTI_CONF = True

#CONF_ONE_WIRE_BUS = 0
CONF_READ_ROM_COMMAND = 0x33
DEFAULT_IBUTTON_READ_ROM_COMMAND = 0x33


ibutton_ns = cg.esphome_ns.namespace("ibutton")

IButtonComponent = ibutton_ns.class_(
    "IButtonComponent", 
    binary_sensor.BinarySensor, 
    cg.Component
)

CONFIG_SCHEMA = (
    binary_sensor.binary_sensor_schema(IButtonComponent)
    .extend(
        {
            cv.GenerateID(): cv.declare_id(IButtonComponent),
            cv.Optional(CONF_UPDATE_INTERVAL, default='60s'): cv.update_interval
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

#CONFIG_SCHEMA = cv.Schema(
#    {
#        cv.GenerateID(): cv.declare_id(IButtonComponent),
#        cv.Required(CONF_ONE_WIRE_BUS): cv.use_id(cg.Component),
#        cv.Optional(CONF_READ_ROM_COMMAND, default=DEFAULT_IBUTTON_READ_ROM_COMMAND): cv.hex_uint8_t,
#        cv.Optional(CONF_UPDATE_INTERVAL, default='60s'): cv.update_interval,
#    }
#).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = await binary_sensor.new_binary_sensor(config)
    await cg.register_component(var, config)

#    one_wire_bus = await cg.get_variable(config[CONF_ONE_WIRE_BUS])
#    cg.add(var.set_one_wire_bus(one_wire_bus))
#    cg.add(var.set_read_rom_command(config[CONF_READ_ROM_COMMAND]))
#    cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL].total_seconds()))

    # Логирование результата
 #   log_stmt = f"{var._var_name}.log_serial_number();"
 #   cg.add(RawStatement(log_stmt))
