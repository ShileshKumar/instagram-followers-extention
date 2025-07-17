from browser import document, html, alert

def on_analyze(ev):
    username = document["username"].value.strip()
    ignore_public = document["ignorePublic"].checked
    ignore_verified = document["ignoreVerified"].checked
    if not username:
        alert("Enter an Instagram username.")
        return

    results_div = document["results"]
    results_div.clear()
    # You can use JS interop for real scraping from the current tab or use APIs
    # Here’s a mock demo with sample data:
    mockdata = [
        {"username": "alice", "is_verified": False, "is_private": True, "full_name": "Alice Smith"},
        {"username": "bob", "is_verified": True, "is_private": False, "full_name": "Bob Jones"},
        {"username": "carol", "is_verified": False, "is_private": False, "full_name": "Carol Lee"}
    ]
    tbl = html.TABLE()
    tbl <= html.TR(html.TH("Username") + html.TH("Verified") + html.TH("Private") + html.TH("Full Name"))
    for user in mockdata:
        if ignore_public and not user["is_private"]: continue
        if ignore_verified and user["is_verified"]: continue
        tbl <= html.TR(
            html.TD(user["username"]) +
            html.TD("Yes" if user["is_verified"] else "No") +
            html.TD("Yes" if user["is_private"] else "No") +
            html.TD(user["full_name"] if user["full_name"] else "")
        )
    results_div <= tbl

document["analyzeBtn"].bind("click", on_analyze)
