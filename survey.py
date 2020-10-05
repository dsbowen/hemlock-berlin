from flask_login import current_user
from hemlock import Branch, Page, Label, route
from hemlock_berlin import berlin

@route('/survey')
def start():
    return Branch(
        berlin(),
        Page(
            Label(compile=display_score), 
            terminal=True
        )
    )

def display_score(label):
    label.label = '<p>Berlin score: {}</p>'.format(
        current_user.g['BerlinScore']
    )