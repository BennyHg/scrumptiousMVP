from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.list import CreateView, UpdateView
from recipes.forms import RatingForm

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


def create_recipe(request):
    if request.method == "POST" and RecipeForm:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", pk=recipe.pk)
    elif RecipeForm:
        form = RecipeForm()
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/new.html", context)

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    # borrowing template from new.html
    template_name = "recipes/new.html"
    # where(homepage) to redirect the user to after creating form
    success_url = "/"

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ["name", "author", "description", "image"]
    template_name = "recipes/edit.html"
    success_url = "/"


def change_recipe(request, pk):
    if Recipe and RecipeForm:
        instance = Recipe.objects.get(pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("recipe_detail", pk=pk)
        else:
            form = RecipeForm(instance=instance)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


def show_recipes(request):
    context = {
        "recipes": Recipe.objects.all() if Recipe else [],
    }
    return render(request, "recipes/list.html", context)


def show_recipe(request, pk):
    context = {
        "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
        "rating_form": RatingForm(),
    }
    return render(request, "recipes/detail.html", context)

def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = Recipe.objects.get(pk=recipe_id)
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)