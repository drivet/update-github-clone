# update-github-clone

A small Flask application to keep a github clone up to date.

If you have a clone of a github repo on some remote server somewhere, you
can keep that cloned repo up to date by using this app and github's webhook
API.

## Requirements

The only real requirement is Flask.  I don't think you need a particularly
up to date one.

## Deployment

The app configures a POST route on '/'.  This means that you have to configure 
your github webhook (in the repo you're cloning from) to hit your server like 
this:

http://www.yourserver.com/

Other options exist.  You can change the route, of course, but what I choose
to do (since I already had a WSGI app configured and running) is "attach"
the app to a different URL (github-webhook) at the WSGI level, via the 
DispatcherMiddleware from the [werkzeug][1] project:

```python
from yawt import create_app
yawtapp = create_app('/path/to/yawt-site')

from update-github-clone import app as webhookapp
from werkzeug.wsgi import DispatcherMiddleware
application = DispatcherMiddleware(yawtapp, {
    '/github-webhook':     webhookapp
})
```

So now you can POST via this URL:

http://www.yourserver.com/github-webhook

In any case, what's provides here is mostly a template to be adpated to new
situations.

[1]: https://github.com/mitsuhiko/werkzeug
