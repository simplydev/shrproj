from django.template import Context, loader
from django.shortcuts import get_object_or_404,render_to_response
from django.core.urlresolvers import reverse
from smrh.models import Choice, Poll
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app, login_required
from google.appengine.api import users
#import gdata.gauth
#import gdata.docs.client
#import gdata.contacts.client


'''SETTINGS = {
    'APP_NAME': 'smrh',
    'CONSUMER_KEY': '1003153080191.apps.googleusercontent.com',
    'CONSUMER_SECRET': 'CCq3ehm1vm2phGBHDJD-fX8T',
    'SCOPES': ['https://docs.google.com/feeds/', 'https://www.google.com/m8/feeds/','https://apps-apis.google.com/a/feeds/','https://www.google.com/m8/feeds/profiles/','https://spreadsheets.google.com/feeds/']
    }'''

# Create an instance of the DocsService to make API calls
'''gdocs = gdata.docs.client.DocsClient(source=SETTINGS['APP_NAME'])
gcontact = gdata.contacts.client.ContactsClient(source=SETTINGS['APP_NAME'])'''

def checkUserLogin(request):
        """This handler is responsible for fetching an initial OAuth
        request token and redirecting the user to the approval page."""

        current_user = users.get_current_user()

        # We need to first get a unique token for the user to
        # promote.
        #
        # We provide the callback URL. This is where we want the
        # user to be sent after they have granted us
        # access. Sometimes, developers generate different URLs
        # based on the environment. You want to set this value to
        # "http://localhost:8080/step2" if you are running the
        # development server locally.
        #
        # We also provide the data scope(s). In general, we want
        # to limit the scope as much as possible. For this
        # example, we just ask for access to all feeds
        #scopes = SETTINGS['SCOPES']
        scopes = ['https://docs.google.com/feeds/', 'https://www.google.com/m8/feeds/','https://apps-apis.google.com/a/feeds/','https://www.google.com/m8/feeds/profiles/','https://spreadsheets.google.com/feeds/']
        oauth_callback = 'http://%s/reqcb' % request.get_host()
        consumer_key = '1003153080191.apps.googleusercontent.com'#SETTINGS['CONSUMER_KEY']
        consumer_secret = 'CCq3ehm1vm2phGBHDJD-fX8T'#SETTINGS['CONSUMER_SECRET']
        
	
	### Commenting to check the login flow
	#request_token = gdocs.get_oauth_token(scopes, oauth_callback,
                                              #consumer_key, consumer_secret)

        # Persist this token in the datastore.
        #request_token_key = 'request_token_%s' % current_user.user_id()

	### Commenting to check the login flow
        '''gdata.gauth.ae_save(request_token, request_token_key)'''

        # Generate the authorization URL.
        approval_page_url = request_token.generate_authorization_url()

        message = """<html><body><a href="%s"> Request token for the Google Documents Scope</a></body></html>""" % approval_page_url
	return HttpResponse(html)


def requestTokenCallBack(request):
        """When the user grants access, they are redirected back to this
        handler where their authorized request token is exchanged for a
        long-lived access token."""

        current_user = users.get_current_user()

        # Remember the token that we stashed? Let's get it back from
        # datastore now and adds information to allow it to become an
        # access token.
        request_token_key = 'request_token_%s' % current_user.user_id()

	### Commenting to check the login flow
        '''gdata.gauth.ae_save(request_token, request_token_key)
        request_token = gdata.gauth.ae_load(request_token_key)
        gdata.gauth.authorize_request_token(request_token, request.uri)'''

        # We can now upgrade our authorized token to a long-lived
        # access token by associating it with gdocs client, and
        # calling the get_access_token method.



	# commenting so that i check the pure flow


        '''gdocs.auth_token = gdocs.get_access_token(request_token)
        gcontact.auth_token = gdocs.auth_token

        # Note that we want to keep the access token around, as it
        # will be valid for all API calls in the future until a user
        # revokes our access. For example, it could be populated later
        # from reading from the datastore or some other persistence
        # mechanism.
        access_token_key = 'access_token_%s' % current_user.user_id()
        gdata.gauth.ae_save(gdocs.auth_token, access_token_key)


        # Finally fetch the document list and print document title in
        # the response
        feed = gdocs.GetDocList()
	templateStr = "<html><body>"
        for entry in feed.entry:
            template = '<div>%s</div>' % entry.title.text
	    templateStr += template
	
	templateStr += "</body></html>"'''
	html = "<html><body> the token is saved </body></html>" 
	return HttpResponse(html)
