# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = '2Steps2Freedom!'
response.subtitle = 'True High Yield Investment'

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [(T('Home'), False,  URL('default', 'index'))]

if not auth.is_logged_in(): response.menu += [(T('Join'), False,  URL('default', 'user/register'))]
    
if auth.is_logged_in():
    response.menu += [
    (T('Buy Coinpack'), False, URL('default', 'about')),
    (T('Wallets'), False, URL('default', 'how_it_works')),
    (T('Holdings'), False, URL('default', 'design')),
    (T('Transactions'), False, '#'),
    (T('Referrals'), False, URL('default', 'design')),
    (T('Promote'), False, 'http://webchat.freenode.net/?channels=web2py'),
    (T('Bounties'), False, '#', [
         (T('Browse'), False, URL('track_record', 'historical')),
         (T('Manage'), False, URL('track_record', 'historical'))
        ])
    ]
else:
    response.menu += [
        (T('About'), False, URL('default', 'about')),
        (T('How it Works'), True, URL('default', 'how_it_works')),
        (T('FAQ'), False, URL('default', 'x')),
        (T('Track Record'), False, '#', [
         (T('Historical'), False, URL('track_record', 'historical')),
         (T('Online'), False, URL('track_record', 'historical'))
        ])
    ]

response.menu += [
    (T('Contact'), False, 'http://webchat.freenode.net/?channels=web2py')
]



if "auth" in locals():
    auth.wikimenu()
