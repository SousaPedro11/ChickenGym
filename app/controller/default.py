from urllib.parse import urlparse, urljoin

from flask import render_template, request

from app import app, lm
from app.model.tables import User


@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html')
