import json
import pulsar
import base64
from Crypto.Cipher import AES


def decrypt_message(pulsar_message, access_key):
    payload = pulsar_message.data().decode('utf-8')
    # print("---\nreceived message origin payload: %s" % payload)
    # handler payload
    decrypt_model = pulsar_message.properties().get("em")
    # print("---\nreceived message decrypt_model: %s " % decrypt_model )
    return do_decrypt_message(payload, decrypt_model, access_key)

# handler message
def do_decrypt_message(payload, decrypt_model, access_key):
    # print("payload:%s" % payload)
    data_json = json.loads(payload)
    encrypt_data = data_json['data']
    decrypt_data = decrypt_by_aes(encrypt_data, access_key, decrypt_model)
    return decrypt_data




def decrypt_by_aes(raw: str, key: str, decrypt_model: str) -> str:

    raw_bytes = base64.b64decode(raw)
    # Extract the key (ensure it's 16 bytes for AES-128 or 24 bytes for AES-192)
    key_bytes = key[8:24].encode('utf-8')

    if decrypt_model == "aes_gcm":
        return decrypt_by_gcm(raw_bytes, key_bytes)
    else:
        return decrypt_by_ecb(raw_bytes, key_bytes)


def decrypt_by_gcm(raw_bytes: bytes, key_bytes: bytes) -> str:

    nonce = raw_bytes[:12]
    ciphertext = raw_bytes[12:-16]
    auth_tag = raw_bytes[-16:]
    aes_cipher = AES.new(key_bytes, AES.MODE_GCM, nonce)
    return aes_cipher.decrypt_and_verify(ciphertext, auth_tag).decode('utf-8')


def decrypt_by_ecb(raw_bytes: bytes, key_bytes: bytes) -> str:

    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(raw_bytes)

    # Decode the decrypted data
    res_str = decrypted_data.decode('utf-8')

    # Clean up the string (removing escape sequences)
    res_str = res_str.replace('\r', '').replace('\n', '').replace('\f', '')
    
    return res_str


def message_id(msg_id) -> str:
    return f"{msg_id.ledger_id()}:{msg_id.entry_id()}:{msg_id.partition()}:{msg_id.batch_index()}"