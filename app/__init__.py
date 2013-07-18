from flask import Flask, render_template
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register application blueprints
from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.posts.views import mod as postsModule
app.register_blueprint(postsModule)
