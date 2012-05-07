from django.conf.urls.defaults import patterns, include, url

from views import recipes_list, recipe_info, making_edit, making_delete, recipe_add, cache_manifest, making_info

urlpatterns = patterns('',
    url(r'^$', recipes_list, {}, name='recipes_list'),
    url(r'cache.manifest', cache_manifest, name="cache_manifest"),
    url(r'recipe/([0-9]+)/$', recipe_info, kwargs={"template_name": "recipes/recipe_info.html"}, name='recipe_info'),
    url(r'recipe/([0-9]+)/description/$', recipe_info, kwargs={"template_name": "recipes/recipe_description.html"}, name='recipe_description'),
    url(r'recipe/([0-9]+)/add_making/$', recipe_info, kwargs={"template_name": "recipes/recipe_add_making.html"}, name='recipe_add_making'),
    url(r'recipe/add$', recipe_add, {}, name="recipegroup_add"),
    url(r'making/edit/([0-9]+)/$', making_edit, {}, name='making_edit'),
    url(r'making/info/([0-9]+)/$', making_info, {}, name='making_info'),
    url(r'making/delete/([0-9]+)/$', making_delete, {}, name='making_delete'),
)
