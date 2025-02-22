# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_service(field, value):
    return get_default_field_value(field, value)


def instance_disable_generic_tags(field, value):
    return False


def instance_empty_default_hostname(field, value):
    return False


def instance_message_flows(field, value):
    return True


def instance_metric_patterns(field, value):
    return get_default_field_value(field, value)


def instance_min_collection_interval(field, value):
    return 15


def instance_mq_password(field, value):
    return get_default_field_value(field, value)


def instance_mq_user(field, value):
    return get_default_field_value(field, value)


def instance_mqcd_version(field, value):
    return 9


def instance_persist_connections(field, value):
    return False


def instance_resource_statistics(field, value):
    return True


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_tls_auth(field, value):
    return False


def instance_tls_certificate_label(field, value):
    return get_default_field_value(field, value)


def instance_tls_cipher_spec(field, value):
    return 'TLS_RSA_WITH_AES_256_CBC_SHA'


def instance_tls_key_repository_location(field, value):
    return '/var/mqm/tls-db/client/KeyringClient'
