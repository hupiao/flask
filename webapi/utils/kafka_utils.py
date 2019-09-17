# -*- coding: utf-8 -*-
import logging
from kafka import KafkaProducer, KafkaConsumer, KafkaClient


def create_sender(**configs):
    sender = None
    try:
        sender = KafkaProducer(**configs)
    except Exception as err:
        logging.info('create kafka producer failed:{}'.format(err))
    return sender


class KfSender(object):
    """
    DEFAULT_CONFIG = {
        'bootstrap_servers': 'localhost',
        'client_id': None,
        'key_serializer': None,
        'value_serializer': None,
        'acks': 1,
        'compression_type': None,
        'retries': 0,
        'batch_size': 16384,
        'linger_ms': 0,
        'partitioner': DefaultPartitioner(),
        'buffer_memory': 33554432,
        'connections_max_idle_ms': 9 * 60 * 1000,
        'max_block_ms': 60000,
        'max_request_size': 1048576,
        'metadata_max_age_ms': 300000,
        'retry_backoff_ms': 100,
        'request_timeout_ms': 30000,
        'receive_buffer_bytes': None,
        'send_buffer_bytes': None,
        'socket_options': [(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)],
        'reconnect_backoff_ms': 50,
        'reconnect_backoff_max': 1000,
        'max_in_flight_requests_per_connection': 5,
        'security_protocol': 'PLAINTEXT',
        'ssl_context': None,
        'ssl_check_hostname': True,
        'ssl_cafile': None,
        'ssl_certfile': None,
        'ssl_keyfile': None,
        'ssl_crlfile': None,
        'ssl_password': None,
        'api_version': None,
        'api_version_auto_timeout_ms': 2000,
        'metric_reporters': [],
        'metrics_num_samples': 2,
        'metrics_sample_window_ms': 30000,
        'selector': selectors.DefaultSelector,
        'sasl_mechanism': None,
        'sasl_plain_username': None,
        'sasl_plain_password': None,
    }
    """

    def __init__(self, topic=None, **configs):
        self.sender = create_sender(**configs)

    def send(self, data):
        if self.sender is None:
            return False
        self.sender.send(data)