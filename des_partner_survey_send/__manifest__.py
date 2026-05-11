{
    'name': 'Partner Survey Send',
    'version': '17.0.1.0.0',
    'summary': 'Manage completed survey sends to contacts with pending/sent status',
    'description': '''
    Partner Survey Send
    ===================
    - One2many from contact to survey send lines
    - Each line: completed survey + state (pending/sent)
    - Send button per line, reset to pending from form
    ''',
    'sequence': 11,
    'depends': ['des_survey_reminder', 'bo_license_client'],
    'author': 'BACKOFFICE S.A.S.',
    'company': 'BackOffice',
    'maintainer': 'BackOffice',
    'website': 'https://www.boffice.cloud/',
    'images': [
        'static/description/screenshots/screen_01_contacto.svg',
        'static/description/screenshots/screen_02_lista.svg',
        'static/description/screenshots/screen_03_encuesta_generar.svg',
        'static/description/screenshots/screen_04_envio.svg',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_survey_send_views.xml',
        'views/res_partner_views.xml',
        'views/survey_generate_wizard_views.xml',
        'views/survey_survey_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
