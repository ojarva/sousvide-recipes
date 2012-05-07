# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
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

        # Adding model 'IngredientForRecipe'
        db.create_table('recipes_ingredientforrecipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Ingredient'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('recipes', ['IngredientForRecipe'])

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('recipes', ['Ingredient'])


    def backwards(self, orm):
        
        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('recipes_recipe_ingredients')

        # Deleting model 'IngredientForRecipe'
        db.delete_table('recipes_ingredientforrecipe')

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')


    models = {
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'recipes.ingredientforrecipe': {
            'Meta': {'object_name': 'IngredientForRecipe'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Ingredient']"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.IngredientForRecipe']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['recipes']
