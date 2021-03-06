from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import potlako_prn_admin
from ..forms import DeathReportForm
from ..models import DeathReport
from .modeladmin_mixins import ModelAdminMixin


@admin.register(DeathReport, site=potlako_prn_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'death_date',
                'cause',
                'specify_relationship',
                'cause_other',
                'autopsy_done',
                'perform_autopsy',
                'death_cause',
                'cause_category',
                'cause_category_other',
                'illness_duration',
                'medical_responsibility',
                'death_known',
                'place_of_death',
                'facility_patient_died',
                'facility_patient_died_other',
                'participant_hospitalized',
                'hospitalised_facility',
                'hospitalised_facility_other',
                'days_hospitalized',
                'comment', ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'cause': admin.VERTICAL,
        'cause_category': admin.VERTICAL,
        'autopsy_done': admin.VERTICAL,
        'perform_autopsy': admin.VERTICAL,
        'medical_responsibility': admin.VERTICAL,
        'place_of_death': admin.VERTICAL,
        'facility_patient_died': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
        'hospitalised_facility': admin.VERTICAL, }
