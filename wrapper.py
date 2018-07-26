# coding: utf-8

from urllib import request
from urllib import parse
import time
import ssl
import json
import hmac, base64, hashlib

class seniverseWrapper(object):
    def __init__(self, uid, key):
        self.baseUrl = 'https://api.seniverse.com/v3'
        self.uid = uid
        self.key = key
        self.context = ssl._create_unverified_context()
        self.signature()

    def signature(self):
        ts = int(time.time())
        params = "ts={ts}&uid={uid}".format(ts=ts, uid=self.uid)
        key = bytes(self.key, 'UTF-8')
        raw = bytes(params, 'UTF-8')
        digester = hmac.new(key, raw, hashlib.sha1).digest()
        signature = base64.encodestring(digester).rstrip()
        sig = parse.quote(signature.decode('utf8'))
        self.sig = sig

    def baseRequest(self, endpoint):
        url = self.baseUrl + endpoint
        res = request.urlopen(url=url, context=self.context)
        return json.loads(res.read().decode('utf-8'))

    def weatherNow(self, location='beijing', language='zh-Hans', unit='c'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'unit': unit}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/now.json?' + query
        return self.baseRequest(endpoint)


    def weatherGridNow(self, location='39.93:116.40', unit='c'):
        query_dict = {'key': self.key, 'location': location, 'unit': unit}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/grid/now.json?' + query
        return self.baseRequest(endpoint)

    def weatherGridMinutely(self, location='39.93:116.40'):
        query_dict = {'key': self.key, 'location': location}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/grid/minutely.json?' + query
        return self.baseRequest(endpoint)

    def weatherDaily(self, location='beijing', language='zh-Hans', unit='c', start='0', days='3'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'unit': unit, 'start': start, 'days': days}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/daily.json?' + query
        return self.baseRequest(endpoint)

    def weatherHourly(self, location='beijing', language='zh-Hans', unit='c', start='0', hours='3'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'unit': unit, 'start': start, 'hours': hours}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/hourly.json?' + query
        return self.baseRequest(endpoint)

    def weatherHourlyHistory(self, location='beijing', language='zh-Hans', unit='c'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'unit': unit}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/hourly_history.json?' + query
        return self.baseRequest(endpoint)

    def weatherHourly3H(self, location='beijing', language='zh-Hans', unit='c'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'unit': unit}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/hourly3h.json?' + query
        return self.baseRequest(endpoint)

    def weatherAlarm(self, location='beijing'):
        query_dict = {'key': self.key, 'location': location}
        query = parse.urlencode(query_dict)
        endpoint = '/weather/alarm.json?' + query
        return self.baseRequest(endpoint)

    def robotTalk(self, q='明天北京天气怎么样?', session=None):
        if session is not None:
            query_dict = {'key': self.key, 'q': q, 'session': session}
        else:
            query_dict = {'key': self.key, 'q': q}
        query = parse.urlencode(query_dict)
        endpoint = '/robot/talk.json?' + query
        return self.baseRequest(endpoint)

    def airNow(self, location='beijing', language='zh-Hans', scope='city'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'scope': scope}
        query = parse.urlencode(query_dict)
        endpoint = '/air/now.json?' + query
        return self.baseRequest(endpoint)


    def airRanking(self, language='zh-Hans'):
        query_dict = {'key': self.key, 'language': language}
        query = parse.urlencode(query_dict)
        endpoint = '/air/ranking.json?' + query
        return self.baseRequest(endpoint)

    def airDaily(self, location='beijing', days='3', language='zh-Hans'):
        query_dict = {'key': self.key, 'location': location, 'days': days, 'language': language}
        query = parse.urlencode(query_dict)
        endpoint = '/air/daily.json?' + query
        return self.baseRequest(endpoint)

    def airHourly(self, location='beijing', days='3', language='zh-Hans'):
        query_dict = {'key': self.key, 'location': location, 'days': days, 'language': language}
        query = parse.urlencode(query_dict)
        endpoint = '/air/hourly.json?' + query
        return self.baseRequest(endpoint)

    def airHourlyHistory(self, location='beijing', language='zh-Hans', scope='city'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'scope': scope}
        query = parse.urlencode(query_dict)
        endpoint = '/air/hourly_history.json?' + query
        return self.baseRequest(endpoint)

    def lifeSuggestion(self, location='beijing', language='zh-Hans'):
        query_dict = {'key': self.key, 'location': location, 'language': language}
        query = parse.urlencode(query_dict)
        endpoint = '/life/suggestion.json?' + query
        return self.baseRequest(endpoint)

    def lifeChineseCalendar(self, start='0', days='3'):
        query_dict = {'key': self.key, 'start': start, 'days': days}
        query = parse.urlencode(query_dict)
        endpoint = '/life/chinese_calendar.json?' + query
        return self.baseRequest(endpoint)

    def lifeDrivingRestriction(self, location='beijing'):
        query_dict = {'key': self.key, 'location': location}
        query = parse.urlencode(query_dict)
        endpoint = '/life/driving_restriction.json?' + query
        return self.baseRequest(endpoint)

    def tideDaily(self, location=None, port=None):
        if location is not None:
            query_dict = {'key': self.key, 'location': location}
            query = parse.urlencode(query_dict)
        else:
            query_dict = {'key': self.key, 'port': port}
            query = parse.urlencode(query_dict)
            
        endpoint = '/tide/daily.json?' + query
        return self.baseRequest(endpoint)

    def geoSun(self, location='beijing', language='zh-Hans', start='0', days='3'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'start': start, 'days': days}
        query = parse.urlencode(query_dict)
        endpoint = '/geo/sun.json?' + query
        return self.baseRequest(endpoint)

    def geoSum(self, location='beijing', language='zh-Hans', start='0', days='3'):
        query_dict = {'key': self.key, 'location': location, 'language': language, 'start': start, 'days': days}
        query = parse.urlencode(query_dict)
        endpoint = '/geo/moon.json?' + query
        return self.baseRequest(endpoint)

    def locationSearch(self, q='beijing', language='zh-Hans', limit='10', offset=0):
        query_dict = {'key': self.key, 'q': q, 'language': language, 'limit': limit, 'offset': offset}
        query = parse.urlencode(query_dict)
        endpoint = '/location/search.json?' + query
        return self.baseRequest(endpoint)

if __name__ == '__main__':
    wrapper = seniverseWrapper()
    data = wrapper.weatherNow('aomen')
    print(data)
