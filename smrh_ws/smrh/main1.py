from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app, login_required
from google.appengine.api import users
import gdata.gauth
import gdata.docs.client
import gdata.contacts.client
from smrh.test.RedirectTest import RedirectTest
from smrh.test.controllers import GetContacts 
from smrh.test.spreadsheetdemo import SpreadSheetDemo 
from smrh.test.ssheet_return import SpreadSheetSerReturn 
from smrh.test.spreadsheet_demo import SpreadSheetDemo1 

# Constants included for ease of understanding. It is a more common
# and reliable practice to create a helper for reading a Consumer Key
# and Secret from a config file. You may have different consumer keys
# and secrets for different environments, and you also may not want to
# check these values into your source code repository.
SETTINGS = {
    'APP_NAME': 'smrh',
    'CONSUMER_KEY': '1003153080191.apps.googleusercontent.com',
    'CONSUMER_SECRET': 'CCq3ehm1vm2phGBHDJD-fX8T',
    'SCOPES': ['https://docs.google.com/feeds/', 'https://www.google.com/m8/feeds/','https://apps-apis.google.com/a/feeds/','https://www.google.com/m8/feeds/profiles/','https://spreadsheets.google.com/feeds/']
    }

# Create an instance of the DocsService to make API calls
gdocs = gdata.docs.client.DocsClient(source=SETTINGS['APP_NAME'])
gcontact = gdata.contacts.client.ContactsClient(source=SETTINGS['APP_NAME'])

class Fetcher(request):

    @login_required
    def get(self):
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
        scopes = SETTINGS['SCOPES']
        oauth_callback = 'http://%s/step2' % self.request.host
        consumer_key = SETTINGS['CONSUMER_KEY']
        consumer_secret = SETTINGS['CONSUMER_SECRET']
        request_token = gdocs.get_oauth_token(scopes, oauth_callback,
                                              consumer_key, consumer_secret)

        # Persist this token in the datastore.
        request_token_key = 'request_token_%s' % current_user.user_id()
        gdata.gauth.ae_save(request_token, request_token_key)

        # Generate the authorization URL.
        approval_page_url = request_token.generate_authorization_url()

        message = """<a href="%s">
Request token for the Google Documents Scope</a>"""
        self.response.out.write(message % approval_page_url)


class RequestTokenCallback(webapp.RequestHandler):

    @login_required
    def get(self):
        """When the user grants access, they are redirected back to this
        handler where their authorized request token is exchanged for a
        long-lived access token."""

        current_user = users.get_current_user()

        # Remember the token that we stashed? Let's get it back from
        # datastore now and adds information to allow it to become an
        # access token.
        request_token_key = 'request_token_%s' % current_user.user_id()
        request_token = gdata.gauth.ae_load(request_token_key)
        gdata.gauth.authorize_request_token(request_token, self.request.uri)

        # We can now upgrade our authorized token to a long-lived
        # access token by associating it with gdocs client, and
        # calling the get_access_token method.
        gdocs.auth_token = gdocs.get_access_token(request_token)
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
        for entry in feed.entry:
            template = '<div>%s</div>'
            self.response.out.write(template % entry.title.text)
        contactGroups = gcontact.GetGroups()
        for i,contactEntry in enumerate(contactGroups.entry):
            self.response.out.write('<div>\n%s %s' % (i + 1, contactEntry.title.text))
            self.response.out.write('    Group ID: %s </div>' % contactEntry.id.text)
            if contactEntry.title.text.find('relative') != -1:
                query = gdata.contacts.client.ContactsQuery()
                query.group = contactEntry.id.text
                contactFeed = gcontact.GetContacts(q = query)
                for i, conRealEntry in enumerate(contactFeed.entry):
                    self.response.out.write('<div>\n the name is ############ %s %s </div>' % (i + 1, conRealEntry.name.full_name.text))
        
    		# Display extended properties.
    		

	#gdocs.Create(gdata.docs.data.SPREADSHEET_LABEL, 'Madus95403259012')

def main():
    application = webapp.WSGIApplication([('/step1', Fetcher),
                                          ('/step2', RequestTokenCallback),('/rtest',RedirectTest),('/getcontact',GetContacts),('/ssheetCli',SpreadSheetDemo1),('/ssheetSer',SpreadSheetDemo),
					  ('/reURL',SpreadSheetSerReturn)],
                                         debug=True)
    run_wsgi_app(application)

