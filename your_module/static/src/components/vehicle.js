/** @odoo-module */

import { registry } from "@web/core/registry"
const { Component, onWillStart, onMounted, useState } = owl

export class VehicleClientAction extends Component {
    setup(){
        this.states = useState({
            name: "",
            logo: "",
        })

        onWillStart(()=>{

        })

        onMounted(()=>{

        })
    }
}

VehicleClientAction.template = "VehicleClientAction"
registry.category("actions").add("vehicle_client_action", VehicleClientAction)