from edc_constants.constants import OTHER, POS, NEG, NONE, UNKNOWN

MISSING = 'missing'

CAUSE_OF_DEATH_CAT = (
    ('hiv_related', 'HIV infection or HIV related diagnosis'),
    ('cancer', 'Cancer'),
    ('cancer_related_diseases', 'Cancer related diseases'),
    ('hiv_unrelated', 'Disease unrelated to HIV'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)

COMPONENTS_RECEIVED = (
    ('provider_edication', 'Provider education'),
    ('diagnostic_facilitation', 'Diagnostic facilitation (pre-biopsy/test)'),
    ('access_to_diagnostic_results',
     'Access to diagnostic results (e.g. histology)'),
    ('cancer_treatment_facilitation_post_test_results',
     'Cancer treatment facilitation post-test results'),
    ('retention_or_completion_of_cancer_treatment',
     'Retention or completion of cancer treatment'),
    (NONE, 'None'),
    (OTHER, 'Other (specify)'),
)

DEATH_INFO_SOURCE = (
    ('death_certificate_review', 'Death Certificate Review'),
    ('clinician', 'Clinician'),
    ('next_of_kin1', 'Next of kin 1'),
    ('other_fam_member', 'Other family member'),
    (OTHER, 'Other (specify)'),
)

DISTRICT = (
    ('chobe', 'Chobe - Chobe'),
    ('bobonong', 'Central - Bobonong'),
    ('boteti', 'Central - Boteti'),
    ('mahalapye', 'Central - Mahalapye'),
    ('orapa', 'Central - Orapa'),
    ('serowe_palapye', 'Central - Serowe/Palapye'),
    ('tutume', 'Central - Tutume'),
    ('CKGR', 'ghanzi - CKGR'),
    ('ghanzi', 'ghanzi - Ghanzi'),
    ('kgalagdi_north', 'Kgalagadi North'),
    ('kgalagadi_south', 'Kgalagadi South'),
    ('kgatleng', 'Kgatleng'),
    ('kweneng_east', 'Kweneng - East'),
    ('kweneng_west', 'Kweneng - West'),
    ('delta', 'north West - Delta'),
    ('ngamiland_north', 'North West - Ngamiland Nort'),
    ('ngamiland_south', 'North East - Ngamiland South'),
    ('north_east', 'North East'),
    ('barolong', 'Southern - Barolong'),
    ('ngwaketse', 'Southern - Ngwaketse'),
    ('ngwaketse_west', 'Southern - Ngwaketse West'),
)

FACILITY = (
    ('boatlaname_hp', 'Boatlaname HP'),
    ('bokaa_pc', 'Bokaa PC'),
    ('borakalalo_pc', 'Borakalalo PC'),
    ('boribamo_pc', 'Boribamo PC'),
    ('boswelakoko_pc', 'Boswelakoko PC'),
    ('ditshukudu_hp', 'Ditshukudu HP'),
    ('gakgatla_hp', 'Gakgatla HP'),
    ('gakuto_hp', 'Gakuto HP'),
    ('gamodubu_hp', 'Gamodubu HP'),
    ('hatsalatladi_hp', 'Hatsalatladi HP'),
    ('kgope_hp', 'Kgope HP'),
    ('kgosing_pc', 'Kgosing PC'),
    ('kopong_pc', 'Kopong PC'),
    ('kubung_hp', 'Kubung HP'),
    ('kumakwane_hp', 'Kumakwane HP'),
    ('kweneng_hp', 'Kweneng HP'),
    ('lekgwapheng_hp', 'Lekgwapheng HP'),
    ('lentsweletau_pc', 'Lentsweletau PC'),
    ('lephepe_pc', 'Lephepe PC'),
    ('lesilakgokong_hp', 'Lesilakgokong HP'),
    ('loologane_pc', 'Loologane PC'),
    ('magokotswane_hp', 'Magokotswane HP'),
    ('mahetlwe_hp', 'Mahetlwe HP'),
    ('medie_hp', 'Medie HP'),
    ('mmankgodi_pc', 'Mmankgodi PC'),
    ('mmanoko_hp', 'Mmanoko HP'),
    ('mmatseta_hp', 'Mmatseta HP'),
    ('mogonono_hp', 'Mogonono HP'),
    ('molepolole_comm_clinic_pc', 'Molepolole Community Clinic PC'),
    ('phuthadikobo_pc', 'Phuthadikobo PC'),
    ('phuting_hp', 'Phuting HP'),
    ('rungwane_hp', 'Rungwane HP'),
    ('shadishadi_hp', 'Shadishadi HP'),
    ('SLH', 'SLH - Scotting Livingstone Hospital'),
    ('sojwe_pc', 'Sojwe PC'),
    ('thamaga_pc', 'Thamaga PC'),
    ('TPH', 'TPH - Thamaga PH'),
    ('marotse_ms', 'Marotse MS'),
    ('chaoke_ms', 'Chaoke MS'),
    ('dam18_ms', 'Dam 18 MS'),
    ('dikgathong_ms', 'Dikgathong MS'),
    ('dikhutsana_ms', 'Dikhutsana MS'),
    ('diphepe_ms', 'Diphepe MS'),
    ('gamatsela_ms', 'Gamatsela MS'),
    ('gamononyane_ms', 'Gamononyane MS'),
    ('hubasanoko_ms', 'Hubasanoko MS'),
    ('kaminakwe_ms', 'Kaminakwe MS'),
    ('kgapamadi_ms', 'Kgapamadi MS'),
    ('khuduyamajako_ms', 'Khuduyamajako MS'),
    ('kokonje_ms', 'Kokonje MS'),
    ('lekgatshwane_ms', 'Lekgatshwane MS'),
    ('maanege_ms', 'Maanege MS'),
    ('mapateng_ms', 'Mapateng MS'),
    ('mmakanke_ms', 'Mmakanke MS'),
    ('mmamarobole_ms', 'Mmamarobole MS'),
    ('mmamohiko_ms', 'Mmamohiko MS'),
    ('mmankgodi_east_ms', 'Mmankgodi East MS'),
    ('mmaothate_ms', 'Mmaothate MS'),
    ('mmapaba_ms', 'Mmapaba MS'),
    ('mmasebele_ms', 'Mmasebele MS'),
    ('moamoge_ms', 'Moamoge MS'),
    ('moetlo_ms', 'Moetlo MS'),
    ('mophakane_ms', 'Mophakane MS'),
    ('mosekele_ms', 'MoseKELE MS'),
    ('moselele1_ms', 'Moselele 1 MS'),
    ('moselele2_ms', 'Moselele 2 MS'),
    ('mosokotso_ms', 'Mosokotso MS'),
    ('motlabaki_ms', 'Motlabaki MS'),
    ('phiriyabokwetse_ms', 'Phiriyabokwetse MS'),
    ('ramagapu_ms', 'Ramagapu MS'),
    ('ramakgatlanyane_ms', 'Ramakgatlanyane MS'),
    ('ramankhung_ms', 'Ramankhung MS'),
    ('ramaphatle_ms', 'Ramankhung MS'),
    ('ramasenyane_ms', 'Ramasenyane MS'),
    ('rammidi_ms', 'Rammidi MS'),
    ('rasegwagwa_ms', 'Rammidi MS'),
    ('sasakwe_ms', 'Sasakwe MS'),
    ('sekhukhwane_ms', 'Sekhukhwane MS'),
    ('sepene_ms', 'Sepene MS'),
    ('shonono_ms', 'Shonono MS'),
    ('suping_ms', 'Suping MS'),
    ('scatter&lamber_pc', 'Scatter & Lamber PC (private)'),
    ('ikago_pc', 'Ikago PC'),
    ('mec_pc', 'Molepopole Education Centre PC'),
    ('molepolole_prisons_pc', 'Molepolole Prisons PC'),
    ('princess_marina', 'Princess Marina Hospital'),
)

FACILITY_TYPE = (
    ('health_post', 'health post'),
    ('primary_clinic', 'primary clinic'),
    ('primary_hospital', 'primary hospital'),
    ('secondary_hospital', 'secondary hospital'),
    ('referral_hospital', 'referral hospital')
)

HOSPITILIZATION_REASONS = (
    ('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'),
    ('respiratory illness, cxr confirmed',
     'Respiratory Illness, CXR confirmed'),
    ('respiratory illness, cxr confirmed, bacterial pathogen, specify',
     'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'),
    ('respiratory illness, cxr confirmed, tb or probable tb',
     'Respiratory Illness, CXR confirmed, TB or probable TB'),
    ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'),
    ('diarrhea illness, viral or bacterial pathogen, specify',
     'Diarrhea Illness, viral or bacterial pathogen, specify'),
    ('sepsis(unspecified)', 'Sepsis(unspecified)'),
    ('sepsis, pathogen specified, specify',
     'Sepsis, pathogen specified, specify'),
    ('mengitis(unspecified)', 'Mengitis(unspecified)'),
    ('mengitis, pathogen specified, specify',
     'Mengitis, pathogen specified, specify'),
    ('non-infectious reason for hospitalization, specify',
     'Non-infectious reason for hospitalization, specify'),
    (OTHER, 'Other infection, specify'),
)

LTFU_CRITERIA = (
    ('missed_visits', 'Missed visits'),
    ('attempted_calls_to_patient',
     'attempted calls to patient x 3 or 3 different days'),
    ('attempted_calls_to_next_kin1',
     'attempted calls to next of kin 1 x 3 or 3 different days'),
    ('attempted_calls_to_next_kin2',
     'attempted calls to next of kin 2 x 3 or 3 different days'),
    ('home_visit_done_unable_to_trace', 'home visit done and unable to trace'),
)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),)

PLACE_OF_DEATH = (
    ('home', 'At home or in the community'),
    ('facility', 'At facility'),
    (UNKNOWN, 'Place of death unknown'),
)

POS_NEG_UNKNOWN_MISSING = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (UNKNOWN, 'Unknown'),
    (MISSING, 'Missing'),
)

REASON_FOR_EXIT = (
    ('death', 'Patient death'),
    ('ltfu', 'Patient lost to follow-up'),
    ('eval_complete', 'Cancer evaluation complete'),
    ('declines_further_eval',
     'Patient or clinician declines further evaluation'),
    ('patient_requests_removal', 'Patient requests removal from Potlako'),
    ('clinician_requests_removal', 'Clinician requests removal from Potlako'),
)

TREATMENT_INTENT = (
    ('curative', 'Curative'),
    ('palliative', 'Palliative'),
    ('uncertain', 'Uncertain'),
)
