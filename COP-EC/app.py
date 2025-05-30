from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Collect base inputs
        source_loc = request.form.get('source_location')
        dest_loc = request.form.get('destination_location')
        source_conn = request.form.get('source_connectivity')
        dest_conn = request.form.get('destination_connectivity')

        # Determine flow type label
        flow_label = None
        gateway = None

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

        # If no early gateway decision, check advanced parameters
        if not gateway:
            payload_size = float(request.form.get('payload_size', 0))
            oas_size = float(request.form.get('oas_size', 0))
            msg_type = request.form.get('message_type')
            tps = int(request.form.get('tps', 0))
            tpm = int(request.form.get('tpm', 0))
            cycle_time = int(request.form.get('cycle_time', 0))
            can_modernize = request.form.get('can_modernize') == 'yes'

            # Decision rules
            if (
                payload_size >= 10 or
                oas_size >= 500 or
                ((flow_label == 'Internal Flow' or flow_label== 'Egress Flow') and msg_type == 'soap') or
                tps > 30 or
                tpm > 1000 or
                cycle_time < 55 or cycle_time > 120

            ):
                gateway = 'Apigee' if can_modernize else 'DataPower'
            else:
                gateway = 'Apigee'

        return render_template('form.html', flow_label=flow_label, gateway=gateway, form=request.form)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
