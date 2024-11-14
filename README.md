
# python pulsar consumer client sdk example
# Support python versions
    Python 3.8, 3.9, 3.10, 3.11, 3.12

# Install requirements

## pulsar client
```
    # current pulsar version ==3.5.0
    # more info: https://pulsar.apache.org/docs/en/client-libraries-python/
    pip3 install pulsar-client
```
## Crypto
```
    # current certifi version ==2024.8.30
    pip3 install pycryptodome
```


# Required parameters

    ACCESS_ID = ""
    ACCESS_KEY = ""
    PULSAR_SERVER_URL = ""
    MQ_ENV=""

# PULSAR_SERVER_URL
```
    //CN
    "pulsar+ssl://mqe.tuyacn.com:7285/";
    //US
    "pulsar+ssl://mqe.tuyaus.com:7285/";
    //EU
    "pulsar+ssl://mqe.tuyaeu.com:7285/";
    //IND
    "pulsar+ssl://mqe.tuyain.com:7285/";
```

# Process the messages you receive，business logic is implemented in this method
```
    handle_message
```