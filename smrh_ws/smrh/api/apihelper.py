import gdata.gauth
import gdata.auth
from google.appengine.api import users
import gdata.contacts
import gdata.contacts.service
import gdata.contacts.client
import gdata.apps.service
import gdata.alt.appengine
import gdata.spreadsheet.service
import gdata.service

SETTINGS = {
    'APP_NAME': 'gdata-feedfetcher',
    'CONSUMER_KEY': '1003153080191.apps.googleusercontent.com',
    'CONSUMER_SECRET': 'CCq3ehm1vm2phGBHDJD-fX8T',
    'SCOPES': ['https://docs.google.com/feeds/', 'https://www.google.com/m8/feeds/','https://spreadsheets.google.com/feeds/spreadsheets/private/full']
    }
class ApiHelper:
	@staticmethod
	def getAccessToken(userid):
		access_token_key = 'access_token_%s' % userid
        	return gdata.gauth.ae_load(access_token_key)
	@staticmethod
	def getSharedContactClient(user):
		sig_method = gdata.auth.OAuthSignatureMethod.HMAC_SHA1
		#gcontact = gdata.contacts.client.ContactsClient(source=SETTINGS['APP_NAME'])
        	#gcontact.auth_token = getAccessToken(userid)
		gd_client = gdata.contacts.service.ContactsService(tokens=ApiHelper.getAccessToken(user.user_id()))
		#gd_client.SetOAuthToken(ApiHelper.getAccessToken(user.user_id()))
		#gd_client.email = 'madhu@apexnetsol.net'#user.email() 
		#gd_client.password = 'abcd1234'#ApiHelper.getAccessToken(user.user_id())
		gd_client.source = 'gdata-feedfetcher'
		gd_client.account_type = 'HOSTED'
		gd_client.contact_list = 'renmaduzohocom.sample-ga.com'
		#gd_client.ProgrammaticLogin()
		return gd_client
	@staticmethod
	def getSharedContactClient1(user):
		gcontact = gdata.contacts.client.ContactsClient(source=SETTINGS['APP_NAME'],auth_token=ApiHelper.getAccessToken(user.user_id()),
				)
		return gcontact
	@staticmethod
	def getAllDomainUsers(user,key,domain):
		sig_method = gdata.auth.OAuthSignatureMethod.HMAC_SHA1
		service = gdata.apps.service.AppsService(domain=key)
		#service.SetOAuthToken(ApiHelper.getAccessToken(user.user_id()))
		source_app_name = SETTINGS['APP_NAME']

		service.SetOAuthInputParameters(sig_method, SETTINGS['CONSUMER_KEY'], consumer_secret=SETTINGS['CONSUMER_SECRET'], two_legged_oauth=True)
		service.debug = True
		print 'the domain is +'+user.email().partition('@')[2]
		service.domain ='renmaduzohocom.sample-ga.com'
		#service = gdata.apps.service.AppsService(domain=key)
		#service.SetOAuthToken(ApiHelper.getAccessToken(user.user_id()))
		#gdata.alt.appengine.run_on_appengine(service)
		#service.ProgrammaticLogin()
		userfeed = service.RetrieveAllUsers()
		return userfeed
	@staticmethod
	def getADomainUser(user,key):
		sig_method = gdata.auth.OAuthSignatureMethod.HMAC_SHA1
		service = gdata.apps.service.AppsService(domain=key)
		#service.SetOAuthToken(ApiHelper.getAccessToken(user.user_id()))
		source_app_name = SETTINGS['APP_NAME']

		service.SetOAuthInputParameters(sig_method, SETTINGS['CONSUMER_KEY'], consumer_secret=SETTINGS['CONSUMER_SECRET'], two_legged_oauth=True)
		service.debug = True
		service.domain ='renmaduzohocom.sample-ga.com' 
		user_to_check='admin'
		lookup_user = service.RetrieveUser('admin')
		if lookup_user.login.admin == 'true':
  			print user_to_check+' is an admin.++++'
		else:
  			print user_to_check+' is not an admin.++++'
	@staticmethod
	def getSpreadSheetService(user,key,domain1):
		gd_client = gdata.spreadsheet.service.SpreadsheetsService()
		gd_client.auth_token = ApiHelper.getAccessToken(user.user_id())
		gd_client.SetClientLoginToken((ApiHelper.getAccessToken(user.user_id())))
		#gd_client.ProgrammaticLogin()
		gd_client.domain ='renmaduzohocom.sample-ga.com' 
		#gd_client.UpgradeToSessionToken()
		return gd_client
		
	@staticmethod
	def getSpreadSheetClient(user,key,domain1):
		sig_method = gdata.auth.OAuthSignatureMethod.HMAC_SHA1
		service = gdata.spreadsheets.client.SpreadsheetsClient()
		service.auth_token=ApiHelper.getAccessToken(user.user_id()) 
		source_app_name = SETTINGS['APP_NAME']
		#service.SetOAuthToken(ApiHelper.getAccessToken(user.user_id()))
		#service.SetClientLoginToken((ApiHelper.getAccessToken(user.user_id())))
		#service.ProgrammaticLogin()
		#service.SetOAuthInputParameters(sig_method, SETTINGS['CONSUMER_KEY'], consumer_secret=SETTINGS['CONSUMER_SECRET'], two_legged_oauth=True)
		service.debug = True
		service.domain ='renmaduzohocom.sample-ga.com' 
		return service
		
		
				
		
		
