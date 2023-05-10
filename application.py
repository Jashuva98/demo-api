import cdmsapp
from cdmsapp.extensions import db

application = cdmsapp.create_app()

if __name__ == '__main__':
    application.run()

# @app.route("/api")
# def api():
#     return "App RUNS"F

# @app.route("/")
# def index():
#     return "IT WORKS"