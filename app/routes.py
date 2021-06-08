from flask import render_template, flash, redirect
from app import app, db
from app.forms import ShortedLinkForm
from app.models import ShortedLink

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShortedLinkForm()
    if form.validate_on_submit():
        shorted_link = ShortedLink(long_url=form.long_url.data)
        token = form.token.data
        if ShortedLink.query.filter_by(token=token).first() is None:
            db.session.add(shorted_link)
            db.session.commit()
            shorted_link.set_token(token) # Two commits because it's takes id to generate token
            db.session.commit()
            flash('http://127.0.0.1:5000/' + shorted_link.token)
        else:
            flash('Use another custom URL')
    return render_template('index.html', form=form)


@app.route('/<token>')
def token_redirect(token):
    shorted_link = ShortedLink.query.filter_by(token=token).first()
    return redirect(shorted_link.long_url)