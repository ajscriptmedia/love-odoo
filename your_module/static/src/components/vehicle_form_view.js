/** @odoo-module */

import { registry } from "@web/core/registry"
import { formView } from "@web/views/form/form_view"
import { FormController } from "@web/views/form/form_controller"

class VehicleFormController extends FormController {
    newButton(url){
        console.log("New Button")
    }
}

VehicleFormController.template = "VehicleFormView"

export const vehicleFormView = {
    ...formView,
    Controller: VehicleFormController,
}

registry.category("views").add("vehicle_form_view", vehicleFormView)