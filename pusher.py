import requests

import config


def push(key=config.DEFAULT_SENDKEY, title='Empty Title', message=None):
    """

    :param key: Channel Key, default Value is config.DEFAULT_SENDKEY
    :param title: Title of the message
    :param message: Full-Message,Markdown supported, default Value is None
    """
    request_json = {
        'sendkey': key,
        "text": title,
        "desp": message,
    }
    print(request_json)
    resp = requests.get(
        url=config.API,
        params=request_json
    )
    print(resp.json())


if __name__ == '__main__':
    push(
        title='Hello World!',
        message='测试信息'
    )
