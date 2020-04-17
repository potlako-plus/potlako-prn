from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import datetime_not_before_study_start

from ..choices import DEATH_INFO_SOURCE, CAUSE_OF_DEATH_CAT
from ..choices import MED_RESPONSIBILITY


class DeathReportModelMixin(models.Model):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of Death:')

    cause = models.CharField(
        max_length=50,
        choices=DEATH_INFO_SOURCE,
        verbose_name=('What was the source o information about participant'
                      'death?'
                      ))

    cause_other = OtherCharField(
        max_length=50)

    perform_autopsy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Will an autopsy be performed later')

    death_cause = models.TextField(
        verbose_name=('Describe the major cause of death (including pertinent'
                      ' autopsy information if available), starting with the'
                      ' first noticeable illness thought to be  related to'
                      ' death, continuing to time of death.'),
        blank=True,
        null=True,
        help_text=('Note: Cardiac and pulmonary arrest are not major reasons'
                   ' and should not be used to describe major cause'))

    cause_category = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,
        verbose_name=('Based on the description above, what category'
                      ' best defines the major cause of death?'))

    cause_category_other = OtherCharField()

    illness_duration = models.IntegerField(
        verbose_name='Duration of acute illness directly causing death',
        help_text='in days (If unknown enter -1)')

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name=('Who was responsible for primary medical care of the '
                      'participant during the month prior to death?'))

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Was the participant hospitalised before death?')

    days_hospitalized = models.IntegerField(
        verbose_name=('For how many days was the participant hospitalised'
                      ' during the illness immediately before death? '),
        help_text='in days',
        default=0)

    comment = models.TextField(
        max_length=250,
        verbose_name='Comments',
        blank=True,
        null=True)

    def get_consent_version(self):
        subject_screening_cls = django_apps.get_model(
            'td_maternal.subjectscreening')
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            subject_screening_obj = subject_screening_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except subject_screening_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Screening form. Please complete '
                'it before proceeding.')
        else:
            try:
                consent_version_obj = consent_version_cls.objects.get(
                    screening_identifier=subject_screening_obj.screening_identifier)
            except consent_version_cls.DoesNotExist:
                raise ValidationError(
                    'Missing Consent Version form. Please complete '
                    'it before proceeding.')
            return consent_version_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(DeathReportModelMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
