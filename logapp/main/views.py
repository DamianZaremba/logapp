from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index( request ):
	context = RequestContext( request )
	return render_to_response( 'main/index.html', context )

def contact( request ):
	context = RequestContext( request )
	return render_to_response( 'main/contact.html', context )
