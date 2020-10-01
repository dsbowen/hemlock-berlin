from hemlock_berlin import berlin

from hemlock import Branch, Page, Label, route

@route('/survey')
def start():
    return Branch(
        berlin(require=True),
        Page(
            Label('<p>Hello World</p>'), 
            terminal=True
        )
    )