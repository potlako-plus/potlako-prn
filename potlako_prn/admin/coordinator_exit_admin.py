from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import potlako_prn_admin
from ..forms import CoordinatorExitForm
from ..models import CoordinatorExit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(CoordinatorExit, site=potlako_prn_admin)
class CoordinatorExitAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = CoordinatorExitForm

    fieldsets = (
        ('To be completed by Physician (Final status)', {
            'fields': ('subject_identifier',
                       'report_datetime',
                       'components_rec',
                       'components_rec_other',
                       'cancer_stage',
                       'cancer_treatment_rec',
                       'cancer_treatments',
                       'cancer_treatment_other',
                       'date_therapy_started',
                       'date_therapy_started_estimated',
                       'date_therapy_started_estimation',
                       'treatment_intent',
                       'patient_disposition',
                       'patient_contact_date'),
        }),
        audit_fieldset_tuple)

    radio_fields = {'cancer_stage': admin.VERTICAL,
                    'cancer_treatment_rec': admin.VERTICAL,
                    'date_therapy_started_estimated': admin.VERTICAL,
                    'date_therapy_started_estimation': admin.VERTICAL,
                    'treatment_intent': admin.VERTICAL,
                    'patient_disposition': admin.VERTICAL, }

    search_fields = ('subject_identifier',)

    list_display = ('subject_identifier', 'report_datetime',)

    filter_horizontal = ('components_rec', 'cancer_treatments')
