import os
from flask import Flask, render_template
from flask.ext.login import LoginManager

config_obj = os.environ.get('DIAG_CONFIG_MODULE')
app = Flask(__name__)
app.config.from_object(config_obj)

login_manager = LoginManager()
login_manager.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Register application blueprints
from consolecraze.users.views import mod as usersModule
app.register_blueprint(usersModule)

from consolecraze.articles.views import mod as articlesModule
app.register_blueprint(articlesModule)

from consolecraze.comments.views import mod as commentsModule
app.register_blueprint(commentsModule)

from consolecraze.frontend.views import mod as frontendModule
app.register_blueprint(frontendModule)
