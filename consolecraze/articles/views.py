from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from consolecraze.database import db_session
from consolecraze.articles.models import Article
from consolecraze.users.decorators import requires_login

mod = Blueprint('articles', __name__)
