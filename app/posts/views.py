from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app.database import db
from app.posts.models import Post
from app.users.decorators import requires_login

mod = Blueprint('posts', __name__, url_prefix='/posts')
