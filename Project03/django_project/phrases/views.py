from django.shortcuts import render
from django.http import HttpResponse
from phrases import models as phrases_models
from .models import Phrases, Sentences

def display(request):
	context = {
		'sentence': phrases_models.Sentences.objects.values_list('sentence', flat=True).order_by("?").first(),
		'phrase1': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		'phrase2': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		'phrase3': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		'phrase4': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
	}
	return render(request, 'display.html', context)


def submit(request):
	if request.method == 'POST':
		if request.POST.get('phrase'):
			post = Phrases()
			post.phrase = request.POST.get('phrase')
			post.save()
			return render(request, 'insert.html')
		elif request.POST.get('sentence'):
			post = Sentences()
			post.sentence = request.POST.get('sentence')
			post.save()
			return render(request, 'insert.html')
	else:
		return render(request, 'insert.html') 
