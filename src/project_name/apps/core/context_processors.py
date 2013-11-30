from django.conf import settings # import the settings file

def extra_context(request):
    # return the value you want as a dictionnary. you may add multiple values
    return {'RAVEN_JS': getattr(settings, 'RAVEN_JS', None)}