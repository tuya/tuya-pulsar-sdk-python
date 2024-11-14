import hashlib
import pulsar


def get_authentication(access_id, accsess_key):
    # generate password
    md5_access_key = hashlib.md5(accsess_key.encode('utf-8')).hexdigest()
    combined = access_id + md5_access_key
    md5_combined = hashlib.md5(combined.encode('utf-8')).hexdigest()
    # base on basic concat rather than json
    password = '"' + md5_combined[8:24] + '"}'
    user_name='{{"username": "{}","password"'.format(access_id)
    return pulsar.AuthenticationBasic(user_name, password, "auth1")