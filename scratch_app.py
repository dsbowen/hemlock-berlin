import eventlet
eventlet.monkey_patch()

from flask_login import current_user
from hemlock import Branch, Page, Label, create_app, route
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
    label.label = 'Berlin score: {}'.format(
        current_user.g['BerlinScore']
    )

app = create_app()

if __name__ == '__main__':
    from hemlock.app import socketio
    socketio.run(app, debug=True)