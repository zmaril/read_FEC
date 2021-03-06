# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SkedE.candidate_checked'
        db.add_column(u'formdata_skede', 'candidate_checked',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['summary_data.Candidate_Overlay'], null=True),
                      keep_default=False)

        # Adding field 'SkedE.district_checked'
        db.add_column(u'formdata_skede', 'district_checked',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['summary_data.District'], null=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_party_checked'
        db.add_column(u'formdata_skede', 'candidate_party_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_overlay'
        db.add_column(u'formdata_skede', 'candidate_overlay',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_name_checked'
        db.add_column(u'formdata_skede', 'candidate_name_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_office_checked'
        db.add_column(u'formdata_skede', 'candidate_office_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_state_checked'
        db.add_column(u'formdata_skede', 'candidate_state_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.candidate_district_checked'
        db.add_column(u'formdata_skede', 'candidate_district_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SkedE.support_oppose_checked'
        db.add_column(u'formdata_skede', 'support_oppose_checked',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SkedE.candidate_checked'
        db.delete_column(u'formdata_skede', 'candidate_checked_id')

        # Deleting field 'SkedE.district_checked'
        db.delete_column(u'formdata_skede', 'district_checked_id')

        # Deleting field 'SkedE.candidate_party_checked'
        db.delete_column(u'formdata_skede', 'candidate_party_checked')

        # Deleting field 'SkedE.candidate_overlay'
        db.delete_column(u'formdata_skede', 'candidate_overlay')

        # Deleting field 'SkedE.candidate_name_checked'
        db.delete_column(u'formdata_skede', 'candidate_name_checked')

        # Deleting field 'SkedE.candidate_office_checked'
        db.delete_column(u'formdata_skede', 'candidate_office_checked')

        # Deleting field 'SkedE.candidate_state_checked'
        db.delete_column(u'formdata_skede', 'candidate_state_checked')

        # Deleting field 'SkedE.candidate_district_checked'
        db.delete_column(u'formdata_skede', 'candidate_district_checked')

        # Deleting field 'SkedE.support_oppose_checked'
        db.delete_column(u'formdata_skede', 'support_oppose_checked')


    models = {
        u'formdata.committee_changed': {
            'Meta': {'object_name': 'Committee_Changed'},
            'committee_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'formdata.filing_header': {
            'Meta': {'object_name': 'Filing_Header'},
            'amended_by': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amendment_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amends_filing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coverage_from_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'coverage_through_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'covered_by': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'covered_by_periodic_filing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'entry_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filing_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'filing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'filing_time_is_exact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'header_data': ('djorm_hstore.fields.DictionaryField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_amendment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superceded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lines_present': ('djorm_hstore.fields.DictionaryField', [], {'default': '{}', 'null': 'True', 'db_index': 'True'}),
            'raw_filer_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        u'formdata.otherline': {
            'Meta': {'object_name': 'OtherLine'},
            'filer_committee_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'filing_number': ('django.db.models.fields.IntegerField', [], {}),
            'form_parser': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'form_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'header_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_data': ('djorm_hstore.fields.DictionaryField', [], {'default': '{}', 'null': 'True'}),
            'superceded_by_amendment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'formdata.skeda': {
            'Meta': {'object_name': 'SkedA'},
            'back_reference_sched_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'back_reference_tran_id_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conduit_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'conduit_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'conduit_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'conduit_street1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'conduit_street2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'conduit_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'contribution_aggregate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'contribution_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'contribution_date': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'contribution_date_formatted': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'contribution_purpose_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'contribution_purpose_descrip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contributor_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contributor_employer': ('django.db.models.fields.CharField', [], {'max_length': '38', 'null': 'True', 'blank': 'True'}),
            'contributor_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'contributor_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contributor_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'contributor_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contributor_occupation': ('django.db.models.fields.CharField', [], {'max_length': '38', 'null': 'True', 'blank': 'True'}),
            'contributor_organization_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contributor_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'contributor_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'contributor_street_1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'contributor_street_2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'contributor_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'contributor_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'donor_candidate_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'donor_committee_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'donor_committee_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'election_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'election_other_description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'filer_committee_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'filing_number': ('django.db.models.fields.IntegerField', [], {}),
            'form_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'header_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'memo_text_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reference_code': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'superceded_by_amendment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'formdata.skedb': {
            'Meta': {'object_name': 'SkedB'},
            'back_reference_sched_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'back_reference_tran_id_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'beneficiary_candidate_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'beneficiary_committee_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'beneficiary_committee_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'category_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'communication_date': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'conduit_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'conduit_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'conduit_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'conduit_street_1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'conduit_street_2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'conduit_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'election_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'election_other_description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'expenditure_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'expenditure_date': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'expenditure_date_formatted': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'expenditure_purpose_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'expenditure_purpose_descrip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'filer_committee_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'filing_number': ('django.db.models.fields.IntegerField', [], {}),
            'form_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'header_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'memo_text_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payee_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payee_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'payee_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payee_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'payee_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payee_organization_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'payee_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'payee_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'payee_street_1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'payee_street_2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'payee_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'payee_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'ref_to_sys_code_ids_acct': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'refund_or_disposal_of_excess': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'semi_annual_refunded_bundled_amt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'superceded_by_amendment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'formdata.skede': {
            'Meta': {'object_name': 'SkedE'},
            'back_reference_sched_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'back_reference_tran_id_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'calendar_y_t_d_per_election_office': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'candidate_checked': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['summary_data.Candidate_Overlay']", 'null': 'True'}),
            'candidate_district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'candidate_district_checked': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'candidate_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'candidate_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'candidate_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'candidate_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'candidate_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'candidate_name_checked': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'candidate_office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'candidate_office_checked': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'candidate_overlay': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'candidate_party_checked': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'candidate_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'candidate_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'candidate_state_checked': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'candidate_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'category_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'completing_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'completing_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'completing_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'completing_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'completing_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'date_signed_formatted': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'district_checked': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['summary_data.District']", 'null': 'True'}),
            'election_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'election_other_description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'expenditure_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'expenditure_date': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'expenditure_date_formatted': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'expenditure_purpose_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'expenditure_purpose_descrip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'filer_committee_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'filing_number': ('django.db.models.fields.IntegerField', [], {}),
            'form_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'header_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'memo_text_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payee_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payee_cmtte_fec_id_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'payee_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'payee_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payee_middle_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'payee_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payee_organization_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'payee_prefix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'payee_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'payee_street_1': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'payee_street_2': ('django.db.models.fields.CharField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'payee_suffix': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'payee_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'superceded_by_amendment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'support_oppose_checked': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'support_oppose_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'legislators.legislator': {
            'Meta': {'object_name': 'Legislator'},
            'bioguide': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'bioguide_previous': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cspan': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'govtrack': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'house_history': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'icpsr': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'lis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'official_full': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'opensecrets': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'thomas': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'votesmart': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'wikipedia': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'})
        },
        u'summary_data.candidate_overlay': {
            'Meta': {'unique_together': "(('fec_id', 'cycle'),)", 'object_name': 'Candidate_Overlay'},
            'bio_blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cand_cand_contrib': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'cand_cand_loans': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'cand_ici': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'cand_is_gen_winner': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'candidate_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cash_on_hand': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'cash_on_hand_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'crp_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'curated_election_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'cycle': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['summary_data.District']", 'null': 'True'}),
            'election_year': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'electioneering': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'expenditures_opposing': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'expenditures_supporting': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'has_contributions': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_general_candidate': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_incumbent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_minor_candidate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'not_seeking_reelection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'office_district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'other_fec_id': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'other_office_sought': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'outstanding_loans': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2', 'blank': 'True'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'pcc': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'pty': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'term_class': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_contributions': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'total_disbursements': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'total_expenditures': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'total_receipts': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'total_unitemized': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'transparency_id': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'transparencydata_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'null': 'True'})
        },
        u'summary_data.district': {
            'Meta': {'object_name': 'District'},
            'altered_by_2010_redistricting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cycle': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'dem_frac_historical': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'election_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incumbent_legislator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['legislators.Legislator']", 'null': 'True'}),
            'incumbent_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'incumbent_party': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'incumbent_pty': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'next_election_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'next_election_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'office_district': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'open_seat': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'rep_frac_historical': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'special_election_scheduled': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'term_class': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['formdata']