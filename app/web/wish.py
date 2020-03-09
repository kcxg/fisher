from flask import url_for, flash, render_template
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from . import web
from .. import db
from ..models.wish import Wish
from ..viewmodels.wish import MyWishes


@web.route('/my/wish')
@login_required
def my_wish():
    view_model = MyWishes(current_user.id)
    return render_template('my_wish.html', wishes=view_model.wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
