# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('recipes_recipe_ingredients')

        # Adding model 'Making'
        db.create_table('recipes_making', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.RecipeGroup'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('temperature', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('recipes', ['Making'])

        # Adding M2M table for field ingredients on 'Making'
        db.create_table('recipes_making_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('making', models.ForeignKey(orm['recipes.making'], null=False)),
            ('ingredientforrecipe', models.ForeignKey(orm['recipes.ingredientforrecipe'], null=False))
        ))
        db.create_unique('recipes_making_ingredients', ['making_id', 'ingredientforrecipe_id'])

        # Adding model 'ImageFile'
        db.create_table('recipes_imagefile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Making'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('recipes', ['ImageFile'])

        # Adding model 'RecipeGroup'
        db.create_table('recipes_recipegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Ingredient'])),
        ))
        db.send_create_signal('recipes', ['RecipeGroup'])

        # Deleting field 'IngredientForRecipe.unit'
        db.delete_column('recipes_ingredientforrecipe', 'unit')

        # Changing field 'IngredientForRecipe.amount'
        db.alter_column('recipes_ingredientforrecipe', 'amount', self.gf('django.db.models.fields.CharField')(max_length=50))


    def backwards(self, orm):
        
        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        db.create_table('recipes_recipe_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('ingredientforrecipe', models.ForeignKey(orm['recipes.ingredientforrecipe'], null=False))
        ))
        db.create_unique('recipes_recipe_ingredients', ['recipe_id', 'ingredientforrecipe_id'])

        # Deleting model 'Making'
        db.delete_table('recipes_making')

        # Removing M2M table for field ingredients on 'Making'
        db.delete_table('recipes_making_ingredients')

        # Deleting model 'ImageFile'
        db.delete_table('recipes_imagefile')

        # Deleting model 'RecipeGroup'
        db.delete_table('recipes_recipegroup')

        # Adding field 'IngredientForRecipe.unit'
        db.add_column('recipes_ingredientforrecipe', 'unit', self.gf('django.db.models.fields.CharField')(default='-', max_length=10), keep_default=False)

        # Changing field 'IngredientForRecipe.amount'
        db.alter_column('recipes_ingredientforrecipe', 'amount', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'recipes.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Making']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'recipes.ingredientforrecipe': {
            'Meta': {'object_name': 'IngredientForRecipe'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Ingredient']"})
        },
        'recipes.making': {
            'Meta': {'object_name': 'Making'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.RecipeGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.IngredientForRecipe']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'temperature': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'recipes.recipegroup': {
            'Meta': {'object_name': 'RecipeGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Ingredient']"})
        }
    }

    complete_apps = ['recipes']
