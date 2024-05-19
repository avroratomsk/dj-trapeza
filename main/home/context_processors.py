from home.models import BaseSettings
from home.forms import CallbackForm, ContactForm, ReviewsForm, WriteToUsForm
from shop.models import Branch, Category 
from service.models import Service
 
def load_settings(request):
    return {'settings': BaseSettings.load()}

def load_branch(request):
    return {'branchs': Branch.objects.all()[:2]}

def load_category(request):
    return {"cats": Category.objects.all().exclude(slug="bez-kategorii")}

def load_cat(request):
    return {"cat": Category.objects.all().exclude(slug="bez-kategorii")}

def load_service(request):
    return {"services": Service.objects.filter(status=True).exclude(slug="priyti-pokushat")}

def setup(request):
    try:
        setup = BaseSettings.objects.get()
    except:
        setup = []
        
    return {"setup": setup}

def callback(request):
    callback = CallbackForm()
    return {"callback": callback}

def writetous(request):
    writetous = WriteToUsForm()
    return {"writetous": writetous}

def contactform(request):
    contactform = ContactForm()
    return {"contactform": contactform}

def reviewsform(request):
    reviewsform = ReviewsForm()
    return {"reviewsform": reviewsform}