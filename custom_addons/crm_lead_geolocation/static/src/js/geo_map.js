/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, onMounted, useEffect } from "@odoo/owl";

export class GeoMap extends Component {
    setup() {
        super.setup();
        onMounted(this.renderMap);

        // React when lat/long values change
        useEffect(
            () => {
                this.updateMarker();
            },
            () => [this.props.record.data.latitude, this.props.record.data.longitude]
        );
    }

    renderMap = () => {
        const lat = this.props.record.data.latitude || 9.03; // default Addis Ababa
        const lng = this.props.record.data.longitude || 38.74;

        this.map = L.map(this.el).setView([lat, lng], 13);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "&copy; OpenStreetMap contributors",
        }).addTo(this.map);

        this.marker = L.marker([lat, lng]).addTo(this.map);
    };

    updateMarker = () => {
        if (!this.map) return;
        const lat = this.props.record.data.latitude;
        const lng = this.props.record.data.longitude;
        if (lat && lng) {
            this.marker.setLatLng([lat, lng]);
            this.map.setView([lat, lng], 14);
        }
    };
}

GeoMap.template = "crm_lead_geolocation.GeoMap";
GeoMap.props = standardFieldProps;

registry.category("fields").add("geo_map", GeoMap);
