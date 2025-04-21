# run.py
from app import create_app
from app.routes import bp
app = create_app()
app.register_blueprint(bp)

@app.route('/')
def index():
    return "Inventory API is up!"

if __name__=='__main__':
    app.run(debug=True)
