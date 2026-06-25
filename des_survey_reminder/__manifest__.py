{
    'name': 'Supplier Quality Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage and Streamline Supplier Evaluations through Automated Surveys and Quality Processes',
    'description': '''
    Supplier Quality Management Module
    ==================================

    This module provides a comprehensive solution for:
    - Automated supplier evaluation surveys
    - Quality process tracking
    - Seamless integration with contacts and survey systems

    Key Features:
    - Generate and send automated survey reminders to suppliers
    - Track supplier performance and quality metrics
    - Enhance supplier relationship management
    ''',
    'sequence': 10,
    'depends': ['contacts', 'mail', 'survey', 'bo_license_client'],
    'author': 'BACKOFFICE S.A.S.',
    'company': 'BackOffice',
    'maintainer': 'BackOffice',
    'website': 'https://desinty.ws',
    'data': [
        'views/res_config_views.xml',
        'views/res_partner_views.xml',
        'views/survey.xml',
        'data/survey_reminder_mail.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
