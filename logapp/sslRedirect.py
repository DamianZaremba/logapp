from django.conf import settings
from django.http import HttpResponseRedirect, get_host

class sslRedirect:
	def process_request( self, request ):
		if not request.is_secure() and request.method != 'POST' and settings.PRODUCTION == True:
				return HttpResponseRedirect( "https://%s%s" % ( get_host( request ), request.get_full_path() ) )
