import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-server-ux",
    description="Meta package for oca-server-ux Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-barcode_action',
        'odoo13-addon-base_technical_features',
        'odoo13-addon-base_tier_validation',
        'odoo13-addon-base_tier_validation_formula',
        'odoo13-addon-date_range',
        'odoo13-addon-mass_editing',
        'odoo13-addon-mass_operation_abstract',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
