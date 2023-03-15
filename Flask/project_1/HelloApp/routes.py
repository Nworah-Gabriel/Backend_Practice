from HelloApp import app

@app.route('/')
def index():
    """A function for a homepage view"""
    return "This is my second flask application, am gonna follow the rule which says \"start and dont stop\""