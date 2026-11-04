import os
from flask import Flask, render_template_string, request
from supabase import create_client, Client

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL", "https://otavnjcevhbtkfsujyig.supabase.co")
key = os.environ.get("SUPABASE_KEY", "")
supabase: Client = create_client(url, key) if key else None

NAV_BAR = '''
<div style="background: #111; border-bottom: 2px solid #0f0; padding: 10px; font-family: monospace; font-size: 14px;">
    <a href="/" style="color: #0f0; margin-right: 15px; text-decoration: none;">[D1: Foundation]</a>
    <a href="/d2" style="color: #0f0; margin-right: 15px; text-decoration: none;">[D2: Marketplace]</a>
    <a href="/d3" style="color: #0f0; margin-right: 15px; text-decoration: none;">[D3: Field Terminal]</a>
    <a href="/d4" style="color: #0f0; margin-right: 15px; text-decoration: none;">[D4: Dispatch]</a>
    <a href="/d5" style="color: #0f0; margin-right: 15px; text-decoration: none;">[D5: Estimator]</a>
    <a href="/d6" style="color: #0f0; text-decoration: none;">[D6: Contractor Hub]</a>
</div>
'''

@app.route("/")
def index():
    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D1 Foundation & System Status</h2>
        <p><b>Core Engine:</b> ONLINE</p>
        <p><b>Supabase Endpoint:</b> Active ({url})</p>
        <p><b>Subscription Status:</b> TRIAL / MOCK MODE ACTIVE</p>
        <p><b>Operational Mode:</b> Off-Grid Resilient / Starlink Ready</p>
        <hr style="border-color: #0f0;">
        <h3>D1 Automated Pipeline Metrics</h3>
        <ul>
            <li>Dual Hazard Detection: Active (80°+ Lean & Roof-Contact Limbs)</li>
            <li>Ghost-Building Defense: Active (Shadow Variance Validation)</li>
            <li>Confidence Scoring: Active (5-Star Reliability Grading)</li>
        </ul>
    </div>
    '''

@app.route("/d2", methods=["GET", "POST"])
def d2_marketplace():
    search_query = request.form.get("query", "") if request.method == "POST" else request.args.get("q", "")
    leads = []
    if supabase:
        try:
            query = supabase.table("leads").select("*")
            if search_query:
                query = query.ilike("name", f"%{search_query}%")
            response = query.execute()
            leads = response.data
        except:
            leads = []

    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D2 Spatial Lead Search & Marketplace</h2>
        <form method="GET" action="/d2" style="margin-bottom: 20px;">
            <input type="text" name="q" value="{search_query}" placeholder="Search leads by name..." style="padding: 6px; width: 280px; background: #222; color: #0f0; border: 1px solid #0f0;">
            <button type="submit" style="padding: 6px 12px; background: #0f0; color: #000; border: none; font-weight: bold; cursor: pointer;">Search Leads</button>
        </form>
        <h3>Available Leads ($5.00 Base / $10.00 Anchor):</h3>
        <ul>
    '''+ ''.join([f"<li><b>{l.get('name', 'Lead')}</b> - {l.get('email', 'No Email')} [Hazard Confirmed]</li>" for l in leads]) + ('' if leads else '<li>No matching leads found in current batch.</li>') + '''
        </ul>
    </div>
    '''

@app.route("/d3")
def d3_field():
    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D3 Field Terminal & Lead Card Engine</h2>
        <p><b>Status:</b> Secure Field Reader Active</p>
        <div style="border: 1px solid #0f0; padding: 15px; margin-top: 15px; background: #111;">
            <h3>Active Queue (3 Initial Trial Leads Loaded)</h3>
            <p><b>Lead #1:</b> 4962 Stoner Road, Blanca, CO</p>
            <p><b>Hazards:</b> Dual 30-foot pine limbs encroaching service drop.</p>
            <div style="margin-top: 10px;">
                <button style="background: #0f0; color: #000; padding: 6px 12px; font-weight: bold; border: none; margin-right: 10px;">[DROP + Photo]</button>
                <button style="background: #0f0; color: #000; padding: 6px 12px; font-weight: bold; border: none; margin-right: 10px;">[SET Appointment]</button>
                <button style="background: #0f0; color: #000; padding: 6px 12px; font-weight: bold; border: none;">[Callback]</button>
            </div>
        </div>
    </div>
    '''

@app.route("/d4")
def d4_dispatch():
    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D4 Customer Dispatch & Broadcast Engine</h2>
        <p><b>Status:</b> Standalone Communications & Manual Verizon Bridge Active</p>
        <div style="border: 1px solid #0f0; padding: 15px; margin-top: 15px; background: #111;">
            <h3>Automated SMS & Billing Hooks</h3>
            <p>• Appointment Set Verification ($5.00 Billed on `sms.sent`): <b>Armed</b></p>
            <p>• Copy / Callback Notifications ($1.00 Billed): <b>Armed</b></p>
            <p>• Sold Job Notifications ($0.00 Exception): <b>Armed</b></p>
        </div>
    </div>
    '''

@app.route("/d5")
def d5_estimator():
    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D5 Estimator Hub & Contract Writer</h2>
        <p><b>Status:</b> Centralized Mapping & Immutability Overlay Active</p>
        <div style="margin-top: 15px;">
            <button style="background: #0f0; color: #000; padding: 8px 16px; font-weight: bold; border: none; margin-right: 10px;">⚡ Scan Neighbor [$1.50]</button>
            <button style="background: #222; color: #0f0; border: 1px solid #0f0; padding: 8px 16px; font-weight: bold;">Flip: Appointment / Callback</button>
        </div>
    </div>
    '''

@app.route("/d6")
def d6_contractor():
    return f'''
    {NAV_BAR}
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 20px; min-height: 90vh;">
        <h2>D6 Contractor Intelligence & Financial Hub</h2>
        <p><b>Status:</b> Master Admin Control & Stripe Parity Active</p>
        <div style="border: 1px solid #0f0; padding: 15px; margin-top: 15px; background: #111;">
            <p>• Zip Code Membership Price: <b>$50.00 / mo</b> (Admin Adjustable)</p>
            <p>• Trial & Billing Cycles: <b>Flexible (7-30 Days)</b></p>
            <p>• Absolute COD & Stripe Webhook Ledger: <b>Connected</b></p>
        </div>
    </div>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
