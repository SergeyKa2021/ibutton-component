#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/gpio/one_wire/gpio_one_wire.h"
#include "esphome/components/one_wire/one_wire.h"

namespace esphome {
namespace ibutton {

class IButtonComponent : public Component, public BinarySensor {
 public:
//    void set_one_wire_bus(const one_wire::OneWireBus *bus) { bus_ = bus; };
//    void set_read_rom_command(uint8_t command) { read_rom_command_ = command; };
//    void log_serial_number() const;

// protected:
//    const one_wire::OneWireBus* bus_{nullptr};  // Один провод для коммуникации
//    uint8_t read_rom_command_;                 // Команда для чтения серийного номера
};

}  // namespace ibutton
}  // namespace esphome
