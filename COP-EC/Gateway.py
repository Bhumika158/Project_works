from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/gateway-check', methods=['POST'])
def gateway_check():
    data = request.get_json()

    # Collect base inputs
    source_loc = data.get('source_location')
    dest_loc = data.get('destination_location')
    source_conn = data.get('source_connectivity')
    dest_conn = data.get('destination_connectivity')
    msg_type = data.get('message_type')
    payload_size = float(data.get('payload_size', 0))
    oas_size = float(data.get('oas_size', 0))
    tps = int(data.get('tps', 0))
    tpm = int(data.get('tpm', 0))
    req_time = int(data.get('req_time', 0))
    res_time = int(data.get('res_time', 0))
    can_modernize = data.get('can_modernize') == 'yes'

    flow_label = None
    gateway = None
    trigger_conditions = []

    # Determine Flow Type
    if source_loc == 'external' and dest_loc == 'internal':
        flow_label = 'Ingress Flow'
        if source_conn == 'lease_line':
            gateway = 'RISE or Apigee DCAM'
        elif source_conn == 'https' and dest_conn == 'mq':
            gateway = 'DataPower'
    elif source_loc == 'internal' and dest_loc == 'external':
        flow_label = 'Egress Flow'
        if dest_conn == 'mq':
            gateway = 'DataPower'
    elif source_loc == 'internal' and dest_loc == 'internal':
        flow_label = 'Internal Flow'
        if source_conn == 'mq' or dest_conn == 'mq':
            gateway = 'DataPower'

    # Advanced Logic if Gateway not yet decided
    if not gateway:
        is_tps_triggered = flow_label == 'Ingress Flow' and tps > 30
        is_tpm_triggered = flow_label in ['Egress Flow', 'Internal Flow'] and tpm > 1000
        is_payload_large = payload_size >= 10
        is_oas_large = oas_size >= 500
        is_soap_internal = (flow_label in ['Internal Flow', 'Egress Flow'] and msg_type == 'soap')
        is_cycle_out_of_bounds = req_time < 55 or res_time > 120

        if is_payload_large: trigger_conditions.append('Payload >= 10MB')
        if is_oas_large: trigger_conditions.append('OAS >= 500KB')
        if is_soap_internal: trigger_conditions.append('SOAP message in internal/egress flow')
        if is_tps_triggered: trigger_conditions.append('TPS > 30 (Ingress)')
        if is_tpm_triggered: trigger_conditions.append('TPM > 1000 (Egress/Internal)')
        if is_cycle_out_of_bounds: trigger_conditions.append('Cycle Time out of range')

        if trigger_conditions:
            gateway = 'Apigee' if can_modernize else 'DataPower'
        else:
            gateway = 'Apigee'

    decision_basis = "All conditions within acceptable range." if not trigger_conditions else "; ".join(trigger_conditions)

    if can_modernize and 'Apigee' in gateway:
        gateway += " (must be modernized as selected)"

    return jsonify({
        "flow_label": flow_label,
        "recommended_gateway": gateway,
        "decision_basis": decision_basis,
        "trigger_conditions": trigger_conditions
    })
