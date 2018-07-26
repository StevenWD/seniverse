# seniverse
Python wrapper for seniverse.com API

#### Initialize

```python
from wrapper import seniverseWrapper

wrapper = seniverseWrapper(uid='your user id', key='your api key')
```

#### Usage

Instant weather information:

```python
>>> wrapper.weatherNow('beijing')

{'results': [{'location': {'id': 'WX4FBXXFKE4F',
    'name': '北京',
    'country': 'CN',
    'path': '北京,北京,中国',
    'timezone': 'Asia/Shanghai',
    'timezone_offset': '+08:00'},
   'now': {'text': '多云',
    'code': '4',
    'temperature': '33',
    'feels_like': '32',
    'pressure': '1001',
    'humidity': '51',
    'visibility': '35.0',
    'wind_direction': '东南',
    'wind_direction_degree': '132',
    'wind_speed': '10.44',
    'wind_scale': '2',
    'clouds': '50',
    'dew_point': ''},
   'last_update': '2018-07-26T18:45:00+08:00'}]}
```





