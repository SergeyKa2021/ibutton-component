#include "esphome/core/log.h"
#include "ibutton.h"

namespace esphome {
namespace ibutton {

//void IButtonComponent::log_serial_number() const {
//    uint8_t serial_number[8];
//    bool success = this->bus_->read_rom(serial_number);
//    if (!success) {
//        ESP_LOGW(TAG, "Ошибка чтения серийного номера");
//        return;
//    }

//    char buffer[25];  // Буфер для сериализации
//    snprintf(buffer, sizeof(buffer), "%02X:%02X:%02X:%02X:%02X:%02X:%02X:%02X",
//            serial_number[0], serial_number[1], serial_number[2], serial_number[3],
//            serial_number[4], serial_number[5], serial_number[6], serial_number[7]);

//    ESP_LOGD(TAG, "Серийный номер iButton: %s", buffer);  // Записываем серийник в лог
//}

}  // namespace ibutton
}  // namespace esphome
