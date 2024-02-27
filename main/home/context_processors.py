from home.models import BaseSettings
from shop.models import Subsidiary 
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def load_branch(request):
    return {'branchs': Subsidiary.objects.all()}

def setup(request):
    try:
        setup = BaseSettings.objects.get()
    except:
        setup = []
        
    return {"setup": setup}