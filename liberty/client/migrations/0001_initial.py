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
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_business', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'])),
            ('contact_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'])),
            ('billing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Billing_Information'])),
        ))
        db.send_create_signal(u'client', ['Client'])

        # Adding model 'Sales_Prospect'
        db.create_table(u'client_sales_prospect', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sales_prospect_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('liberty_contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Employee'])),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('probability', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('initial_contact_date', self.gf('django.db.models.fields.DateField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'client', ['Sales_Prospect'])

        # Adding model 'Billing_Information'
        db.create_table(u'client_billing_information', (
            ('billing_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attention_first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('attention_last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('business_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_business', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'client', ['Billing_Information'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'client_client')

        # Deleting model 'Sales_Prospect'
        db.delete_table(u'client_sales_prospect')

        # Deleting model 'Billing_Information'
        db.delete_table(u'client_billing_information')


    models = {
        u'client.billing_information': {
            'Meta': {'object_name': 'Billing_Information'},
            'attention_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'attention_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'billing_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'client.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Billing_Information']"}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'client_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'client_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'is_business': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'client.sales_prospect': {
            'Meta': {'object_name': 'Sales_Prospect'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'initial_contact_date': ('django.db.models.fields.DateField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'liberty_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']"}),
            'probability': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sales_prospect_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'office_phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'phone_extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'common.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'employee.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Address']"}),
            'contact_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Contact']"}),
            'employee_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'employee_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hire_date': ('django.db.models.fields.DateField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pay_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'pay_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'termination_date': ('django.db.models.fields.DateField', [], {}),
            'termination_reason': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['employee.Title']", 'symmetrical': 'False'})
        },
        u'employee.title': {
            'Meta': {'object_name': 'Title'},
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['client']