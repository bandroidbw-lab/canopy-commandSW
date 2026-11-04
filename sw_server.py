import os
from flask import Flask, render_template_string, request
from supabase import create_client, Client

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL", "https://otavnjcevhbtkfsujyig.supabase.co")
key = os.environ.get("SUPABASE_KEY", "")
supabase: Client = create_client(url, key) if key else None

@app.route("/")
def index():
    return '''
    <div style="font-family: monospace; background: #111; color: #0f0; padding: 20px; height: 100vh;">
        <h2>[<a href="/" style="color: #0f0;">D1: Foundation</a>] | [<a href="/d2" style="color: #0f0;">D2: Lead Search</a>]</h2>
        <h3>Core Engine: ONLINE</h3>
        <p>Supabase Endpoint: Active</p>
    </div>
    '''

@app.route("/d2", methods=["GET", "POST"])
def lead_search():
    search_query = request.form.get("query", "") if request.method == "POST" else request.args.get("q", "")
    leads = []
    
    if supabase:
        try:
            query = supabase.table("leads").select("*")
            if search_query:
                query = query.ilike("name", f"%{search_query}%")
            response = query.execute()
            leads = response.data
        except Exception as e:
            leads = []

    html = '''
    <div style="font-family: monospace; background: #111; color: #0f0; padding: 20px; min-height: 100vh;">
        <h2>[<a href="/" style="color: #0f0;">D1: Foundation</a>] | [<a href="/d2" style="color: #0f0;">D2: Lead Search</a>]</h2>
        <form method="GET" action="/d2" style="margin-bottom: 20px;">
            <input type="text" name="q" value="''' + search_query + '''" placeholder="Search leads by name..." style="padding: 5px; width: 250px; background: #222; color: #0f0; border: 1px solid #0f0;">
            <button type="submit" style="padding: 5px 10px; background: #0f0; color: #000; border: none; font-weight: bold;">Search</button>
        </form>
        <h3>Found Leads:</h3>
        <ul>
    '''
    if leads:
        for lead in leads:
            name = lead.get('name', 'Unnamed Lead')
            email = lead.get('email', 'No Email')
            html += f"<li><b>{name}</b> - {email}</li>"
    else:
        html += "<li>No leads found or database not connected yet.</li>"
        
    html += '</ul></div>'
    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
