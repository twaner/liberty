# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'client_client', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('client_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_number', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('is_business', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'], null=True, blank=True)),
            ('contact_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'], null=True, blank=True)),
            ('billing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Billing_Information'], null=True, blank=True)),
        ))
        db.send_create_signal(u'client', ['Client'])

        # Adding model 'Sales_Prospect'
        db.create_table(u'client_sales_prospect', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sales_prospect_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('liberty_contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'], null=True, blank=True)),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('probability', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('initial_contact_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'], null=True, blank=True)),
            ('contact_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'], null=True, blank=True)),
            ('is_client', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'client', ['Sales_Prospect'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'client_client')

        # Deleting model 'Sales_Prospect'
        db.delete_table(u'client_sales_prospect')


    models = {
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']", 'null': 'True', 'blank': 'True'}),
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Billing_Information']", 'null': 'True', 'blank': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'client_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'client_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'client.sales_prospect': {
            'Meta': {'object_name': 'Sales_Prospect'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'initial_contact_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_client': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'liberty_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']", 'null': 'True', 'blank': 'True'}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'sales_prospect_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NY'", 'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'common.billing_information': {
            'Meta': {'object_name': 'Billing_Information'},
            'attention_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'attention_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'billing_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'common.city': {
            'Meta': {'object_name': 'City'},
            'city_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'common.contact': {
            'Meta': {'object_name': 'Contact'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'office_phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'blank': 'True'}),
            'phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'employee.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']"}),
            'e_title': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employee.Title']", 'symmetrical': 'False'}),
            'employee_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'employee_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hire_date': ('django.db.models.fields.DateField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pay_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'default': "'HR'", 'max_length': '3'}),
            'termination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'termination_reason': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'employee.title': {
            'Meta': {'object_name': 'Title'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['client']