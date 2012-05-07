from django.conf import settings
from django.contrib.auth import get_backends
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Sum, Avg
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST, condition, require_GET

import datetime

from recipes.models import *
from recipes.forms import MakingForm, RecipeForm, DescrForm

@require_GET
def cache_manifest(request):
    """ Return cache manifest, including all recipe groups """
    recipegroups = RecipeGroup.objects.all()
    return render_to_response("recipes/cache.manifest.txt", {"recipegroups": recipegroups}, context_instance=RequestContext(request), mimetype="text/cache-manifest")

@require_GET
def recipes_list(request):
    """ Get list of all ingredients """

    recipes = RecipeGroup.objects.all()
    in_progress_makings = Making.objects.filter(in_progress=True)
    for recipe in recipes:
        recipe.makingscount = Making.objects.filter(group=recipe).count()
    ingredientcount = recipes.count()
    makingcount = Making.objects.all().count()
    hourcount = (Making.objects.all().aggregate(Sum("time"))).get("time__sum") / 60
    houravg = round(float((Making.objects.all().aggregate(Avg("time"))).get("time__avg")) / 60, 1)

    return render_to_response("recipes/recipes_list.html", {"ingredientcount": ingredientcount, "makingcount": makingcount, "houravg": houravg, "hourcount": hourcount, "in_progress_makings": in_progress_makings, "recipes": recipes}, context_instance=RequestContext(request))

def recipe_info(request, id, template_name):
    recipegroup = RecipeGroup.objects.get(id=id)
    descrform = DescrForm(initial={"description":recipegroup.description})
    form = MakingForm()
    if request.method == 'POST' and request.user.is_authenticated():
        if request.GET.get("descr") is not None:
            descrform = DescrForm(request.POST)
            if descrform.is_valid():
                recipegroup.description = descrform.cleaned_data["description"]
                recipegroup.save()
        else:
            form = MakingForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.group = recipegroup
                instance.save()
                form = MakingForm()

    recipegroup.description = recipegroup.description.replace("\n", "<br>")

    makings = Making.objects.filter(group=recipegroup)
    return render_to_response(template_name, {"descr_form": descrform, "form": form, "recipegroup": recipegroup, "makings": makings}, context_instance=RequestContext(request))

@login_required
@csrf_protect
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            ingredient = Ingredient(name=form.cleaned_data["ingredient"])
            ingredient.save()
            recipegroup = RecipeGroup(main_ingredient=ingredient)
            recipegroup.save()
            return HttpResponseRedirect(reverse("recipe_info", args=(recipegroup.id,)))
    else:
        form = RecipeForm()
    return render_to_response("recipes/recipe_add.html", {"form": form}, context_instance=RequestContext(request))

def making_info(request, id):
    making = Making.objects.get(id=id)
    recipegroup = making.group
    return render_to_response("recipes/making_info.html", {"recipegroup": recipegroup, "making": making} , context_instance=RequestContext(request))
    

@login_required
@csrf_protect
def making_edit(request, id):
    making = Making.objects.get(id=id)
    recipegroup = making.group
    if request.method == "POST":
        form = MakingForm(request.POST, instance=making)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("recipe_info", args=(recipegroup.id,)))
    else:
        form = MakingForm(instance=making)
    return render_to_response("recipes/making_edit.html", {"form": form, "recipegroup": recipegroup, "making": making} , context_instance=RequestContext(request))

@login_required
@csrf_protect
@require_POST
def making_delete(request, id):
    if request.method == "POST":
        making = Making.objects.get(id=id)
        groupid = making.group.id
        main_ingredient = making.group.main_ingredient
        making.delete()
        return HttpResponseRedirect(reverse("recipe_info", args=(groupid,)))
    else:
        return HttpResponse("Invalid request")
