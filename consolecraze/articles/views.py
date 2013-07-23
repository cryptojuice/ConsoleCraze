from flask import Blueprint, request, render_template, flash, g, session, \
        redirect, url_for, jsonify

from consolecraze.database import db_session
from consolecraze.articles.models import Article
from consolecraze.users.decorators import requires_login

mod = Blueprint('articles', __name__, url_prefix='/articles')

@mod.route("/")
def index():
    return jsonify(articles=[
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Dead Rising 3 started on 360, pushed the hardware to far",
            "summary":"Dead Rising 3 first surfaced almost two years ago. So how did it end up an Xbox One title? According to Capcom Vancouver producer Mike Jones, talking to Siliconera, it was a matter of resources.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "thumbnail_url":"",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        }


    ])
