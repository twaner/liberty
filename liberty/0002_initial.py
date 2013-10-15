# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'common_city', (
            ('city_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'common', ['City'])

        # Adding model 'State'
        db.create_table(u'common_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'common', ['State'])

        # Adding model 'Address'
        db.create_table(u'common_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.City'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.State'])),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'common', ['Address'])

        # Adding model 'Contact'
        db.create_table(u'common_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone_extension', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('office_phone_extension', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'common', ['Contact'])

        # Adding model 'Billing_Information'
        db.create_table(u'common_billing_information', (
            ('billing_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'common', ['Billing_Information'])

        # Adding model 'Equipment'
        db.create_table(u'common_equipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipment_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('equipment_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('equipment_notes', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'common', ['Equipment'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'common_city')

        # Deleting model 'State'
        db.delete_table(u'common_state')

        # Deleting model 'Address'
        db.delete_table(u'common_address')

        # Deleting model 'Contact'
        db.delete_table(u'common_contact')

        # Deleting model 'Billing_Information'
        db.delete_table(u'common_billing_information')

        # Deleting model 'Equipment'
        db.delete_table(u'common_equipment')


    models = {
        u'common.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.State']"}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'common.billing_information': {
            'Meta': {'object_name': 'Billing_Information'},
            'billing_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.city': {
            'Meta': {'object_name': 'City'},
            'city_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'common.contact': {
            'Meta': {'object_name': 'Contact'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'office_phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'common.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'equipment_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'equipment_notes': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'equipment_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['common']