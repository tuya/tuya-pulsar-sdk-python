import pulsar
from mq_authentication import get_authentication
from message_util import decrypt_message, message_id


# env
MQ_ENV_PROD = "event"
MQ_ENV_TEST = "event-test"

# server url
PULSAR_SERVER_CN = "pulsar+ssl://mqe.tuyacn.com:7285/"
PULSAR_SERVER_EU = "pulsar+ssl://mqe.tuyaeu.com:7285/"
PULSAR_SERVER_US = "pulsar+ssl://mqe.tuyaus.com:7285/"
PULSAR_SERVER_IND = "pulsar+ssl://mqe.tuyain.com:7285/"

# access_id, access_key, server_url, mq_env
ACCESS_ID = ""
ACCESS_KEY = ""
PULSAR_SERVER_URL = PULSAR_SERVER_CN
MQ_ENV = MQ_ENV_PROD

# handler message
def handle_message(pulsar_message, decrypt_mssage, msg_id):
    print("---\n start handle message message_id: %s" % msg_id)
    # TODO handle message
    print("---\n handle message success message_id: %s" % msg_id)


client = pulsar.Client(PULSAR_SERVER_CN, 
    authentication=get_authentication(ACCESS_ID, ACCESS_KEY),
    tls_allow_insecure_connection=True,
    )

consumer = client.subscribe(ACCESS_ID + '/out/' + MQ_ENV, ACCESS_ID + '-sub', consumer_type=pulsar.ConsumerType.Failover)

while True:
    try:
        pulsar_message = consumer.receive()
        msg_id = message_id(pulsar_message.message_id())
        print("---\n received message message_id: %s" % msg_id)
        decrypt_mssage = decrypt_message(pulsar_message, ACCESS_KEY)
        handle_message(pulsar_message, decrypt_mssage, msg_id)
        print("---\n message decrypt message: %s" % decrypt_mssage)
        consumer.acknowledge(pulsar_message)
    except pulsar.Interrupted:
        print("Stop receiving messages")
        break
client.close()

