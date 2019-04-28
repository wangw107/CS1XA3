from django.shortcuts import render
from django.http import HttpResponse
from phrases import models as phrases_models
from .models import Phrases, Sentences

def display(request):
        result = "[Something wrong happened in the server...]"
        try:
                result = phrases_models.Sentences.objects.values_list('sentence', flat=True).order_by("?").first().replace("{}", phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first())
        except:
                pass
        context = {
		'result': result
		#'phrase1': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		#'phrase2': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		#'phrase3': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
		#'phrase4': phrases_models.Phrases.objects.values_list('phrase', flat=True).order_by("?").first(),
	}
        return render(request, 'display.html', context)

def submit(request):
        if request.method == 'POST':
                context = {}
                if request.POST.get('phrase'):
                        result = request.POST.get('phrase').strip()
                        try:
                                post = Phrases()
                                post.phrase = result
                                post.save()
                                context["result_color"] = "green"
                                context["result"] = "Content added successfully!"
                        except Exception as ex:
                                exstr = str(ex)
                                if "UNIQUE constraint failed" in exstr:
                                        context["result_color"] = "red"
                                        context["result"] = "Content with same value exists!"
                        return render(request, 'insert.html', context)
                elif request.POST.get('sentence'):
                        result = request.POST.get('sentence').strip()
                        try:
                                post = Sentences()
                                post.sentence = result
                                post.save()
                                context["result_color"] = "green"
                                context["result"] = "Content added successfully!"
                        except Exception as ex:
                                exstr = str(ex)
                                if "UNIQUE constraint failed" in exstr:
                                        context["result_color"] = "red"
                                        context["result"] = "Content with same value exists!"
                        return render(request, 'insert.html', context)
                else:
                        context["result_color"] = "red"
                        context["result"] = "Content is empty!"
                        print(context)
                        return render(request, 'insert.html', context)
        else:
                return render(request, 'insert.html') 
