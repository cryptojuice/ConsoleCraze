from flask import Blueprint, request, render_template, flash, g, session, \
        redirect, url_for, jsonify

from consolecraze.database import db_session
from consolecraze.comments.models import Comment
from consolecraze.users.decorators import requires_login

mod = Blueprint('comments', __name__, url_prefix='/comments')

