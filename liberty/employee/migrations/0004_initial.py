# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table(u'employee_title', (
            ('title_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'employee', ['Title'])

        # Adding model 'Employee'
        db.create_table(u'employee_employee', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('employee_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee_number', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Address'])),
            ('contact_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Contact'])),
            ('hire_date', self.gf('django.db.models.fields.DateField')()),
            ('pay_type', self.gf('django.db.models.fields.CharField')(default='HR', max_length=3)),
            ('pay_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2, blank=True)),
            ('termination_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('termination_reason', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'employee', ['Employee'])

        # Adding M2M table for field e_title on 'Employee'
        m2m_table_name = db.shorten_name(u'employee_employee_e_title')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('employee', models.ForeignKey(orm[u'employee.employee'], null=False)),
            ('title', models.ForeignKey(orm[u'employee.title'], null=False))
        ))
        db.create_unique(m2m_table_name, ['employee_id', 'title_id'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table(u'employee_title')

        # Deleting model 'Employee'
        db.delete_table(u'employee_employee')

        # Removing M2M table for field e_title on 'Employee'
        db.delete_table(db.shorten_name(u'employee_employee_e_title'))


    models = {
        u'common.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NY'", 'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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

    complete_apps = ['employee']