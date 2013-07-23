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
            "image_url": "http://cdn.destructoid.com/ul/258452-dr3stuffs.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"GTAV PC petition nets 200,000 signatures",
            "summary":"Online petition calling for PC version of upcoming open-world action game reaches new signature milestone.",
            "url":"http://www.gamespot.com/news/gtav-pc-petition-nets-200000-signatures-6411872",
            "image_url": "http://image.gamespotcdn.net/gamespot/images/2013/202/GTAV77_48397_640screen.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Rumor: Left 4 Dead 3 countdown appears",
            "summary":"A suspicious looking URL has just been uncovered that appears to be a countdown clock for Left 4 Dead 3, complete with a Source 2 logo. When it comes to Valve rumors, I’m as skeptical as it gets. ",
            "url":"http://stickskills.com/2013/07/22/rumor-left-4-dead-3-countdown-appears/",
            "image_url": "http://stickskills.com/omega/wp-content/uploads/2013/07/L4D3-620x400.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Why the Xbox One Will Win Next Gen",
            "summary":"Yes, you read the title correctly: The Xbox One will win next gen. Before I get into my explanation, let me just say firstly that I am someone who isn’t particularly fond of Microsoft.",
            "url":"http://gaminrealm.com/2013/07/21/why-the-xbox-one-will-win-next-gen/",
            "image_url": "http://gaminrealm.com/wp-content/uploads/2013/07/o-XBOX-ONE-facebook-660x350.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"New Castlevania Game On Its Way",
            "summary":"At Comic-Con, Konami hinted to a new Castlevania game coming and that it would not be developed by MercurySteam. David Cox, producer of Castlevania said that the past games had mistakes that could have been avoided, and that Konami has a plan on avoiding them next time around with this new Castlevania game.",
            "url":"http://www.destructoid.com/dead-rising-3-started-on-360-pushed-the-hardware-too-far-258452.phtml",
            "image_url": "http://gaminrealm.com/wp-content/uploads/2013/07/Castlevania-Theme-660x350.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"Rumor: ‘Tomb Raider’ sequel outed by comic tie-in author",
            "summary":"Good news for fans of this year’s Tomb Raider reboot: if the author of the tie-in comic is to be believed, there will be a sequel to the origin story.",
            "url":"http://stickskills.com/2013/07/19/rumor-tomb-raider-sequel-outed-by-comic-tie-in-author/",
            "image_url": "http://stickskills.com/omega/wp-content/uploads/2013/07/tr-620x400.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        },
        {
            "title":"The Last of Us Review | AFK",
            "summary":"“The Last of Us” is a third person action adventure game developed by Naughty Dog (Uncharted Series) and published by Sony. ",
            "url":"http://afk.ie/last-of-us-review/",
            "image_url": "http://emenzee.files.wordpress.com/2013/06/the-last-of-us.jpg",
            "user_id": 0, 
            "upvoted_by": None,
            "downvoted_by": None
        }


    ])
