import requests

import config


def push(title, message=None):
    request_json = {
        'sendkey': config.sendkey,
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
