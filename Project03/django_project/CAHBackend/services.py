from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

# Register new account
def register(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Login account
def login(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Get current sentence and phrases
def getphrase(request):
    if request.method == 'GET':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Add one completed sentence    
def addresult(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Add one custom sentence template
def addsentence(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Add one custom phrase
def addphrase(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Thumbs up a sentence
def like(request):
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()

# Get completed sentences
def display(request):
    if request.method == 'GET':
        raise NotImplementedError()
    else:
        return HttpResponseForbidden()
