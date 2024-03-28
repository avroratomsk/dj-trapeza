from home.models import BaseSettings
from shop.models import Branch, Category 
from service.models import Service
 
def load_settings(request):
    return {'site_settings': BaseSettings.load()}

def load_branch(request):
    return {'branchs': Branch.objects.all()}

def load_category(request):
    return {"categorys": Category.objects.all().exclude(slug="bez-kategorii")}

def load_service(request):
    return {"services": Service.objects.filter(status=True).exclude(slug="priyti-pokushat")}

def setup(request):
    try:
        setup = BaseSettings.objects.get()
    except:
        setup = []
        
    return {"setup": setup}