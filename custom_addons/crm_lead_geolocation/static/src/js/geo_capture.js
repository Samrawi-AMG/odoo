/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

patch(FormController.prototype, {
    async setup() {
        // Call original setup first
        super.setup(...arguments);

        // Only try if geolocation is available
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    try {
                        this.model.root.update({
                            latitude: +position.coords.latitude.toFixed(6),
                            longitude: +position.coords.longitude.toFixed(6),
                        });
                    } catch (e) {
                        console.warn("Failed to update geo in buffer", e);
                    }
                },
                (err) => {
                    console.warn("Geolocation error:", err);
                }
            );
        }
    },
});
