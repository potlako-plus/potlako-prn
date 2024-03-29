from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, HIGH_PRIORITY, site_action_items

DEATH_REPORT_ACTION = 'submit-death-report'
SUBJECT_OFFSTUDY_ACTION = 'submit-subject-offstudy'
COORDINATOR_EXIT_ACTION = 'submit-coordinator-exit-form'


class PotlakoCoordinatorAction(Action):
    name = COORDINATOR_EXIT_ACTION
    display_name = 'Submit Coordinator Exit Form'
    reference_model = 'potlako_prn.coordinatorexit'
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'potlako_prn.deathreport'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        actions = []
        potlako_deathreport_cls = django_apps.get_model(
            'potlako_prn.deathreport')

        action_item_cls = django_apps.get_model('edc_action_item.actionitem')

        subject_identifier = self.reference_model_obj.subject_identifier

        offstudy = action_item_cls.objects.filter(
            subject_identifier=subject_identifier,
            action_type__name='submit-subject-offstudy')

        try:
            potlako_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            pass
        else:
            if not offstudy:
                actions = [SubjectOffStudyAction]
        return actions


class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Submit Subject Offstudy'
    reference_model = 'potlako_prn.subjectoffstudy'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        potlako_deathreport_cls = django_apps.get_model(
            'potlako_prn.deathreport')
        action_item_cls = django_apps.get_model('edc_action_item.actionitem')
        subject_identifier = self.reference_model_obj.subject_identifier
        off_study_reason = self.reference_model_obj.reason
        death_actions = action_item_cls.objects.filter(
            subject_identifier=subject_identifier,
            action_type__name='submit-death-report')
        actions = [PotlakoCoordinatorAction]

        try:
            potlako_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            if not death_actions and off_study_reason == 'death':
                actions.append(DeathReportAction)
        return actions


site_action_items.register(DeathReportAction)
site_action_items.register(SubjectOffStudyAction)
site_action_items.register(PotlakoCoordinatorAction)
