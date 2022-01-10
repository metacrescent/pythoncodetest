from django.core.validators import RegexValidator

alphanumeric_validator = RegexValidator(r'[^\w\d]*(([0-9]+.*[A-Za-z]+.*)|^[0-9]*$|[A-Za-z]+.*)',
                                        'Only alphanumeric characters are allowed')

domain_regex = r'^[a-zA-Z0-9_-]+$'
domain_validator = RegexValidator(domain_regex, 'Invalid subdomain format')
