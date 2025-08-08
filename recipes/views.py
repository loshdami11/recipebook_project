from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Retrieve data from the database."""
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    template = 'recipes/index.html' 
    return render(request, template, context)


@login_required
def success(request):
    return render(request, 'recipes/success.html')

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST) 
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            return redirect('success')
    else:
        form = RecipeForm()
        template = 'recipes/create_recipe.html'
        context = {'form': form}
        return render(request, template, context)
    

@login_required   
def recipe_detail(request, recipe_id):
    """Detail View for a recipe"""
    recipe = recipe.objects.get(id=recipe_id)
    if recipe.author != request.user:
        raise Http404
    context = {'recipe': recipe}
    template = 'recipes/recipe_detail.html'
    return render(request, template, context)


@login_required
def update_recipe(request, recipe_id):
    """Update a recipe."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        raise Http404
    
    if request.method == 'POST':
        form = RecipeForm(data=request.POST, instance=recipe)
        if form.is_valid():
            edit_recipe = form.save(commit=False)
            #edit_recipe.author = request.user
            edit_recipe.save()
            return redirect('recipe-detail', recipe.id)
    else:
        form = RecipeForm(instance=recipe)
        return render(request, template_name='recipes/update_recipe.html', context={'form': form})
    

@login_required
def delete_recipe(request, recipe_id):
    """Delete a recipe."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        raise Http404
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    context = {'recipe': recipe}
    return render(request, template_name='recipes/delete_recipe.html', context=context)

    


