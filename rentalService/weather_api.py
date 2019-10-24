import urllib.request
import json
import datetime
import pytz

def get_weather_data() :
    api_date, api_time = get_api_date()
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    #key = "serviceKey=" + bill.key
    key = "serviceKey= JjbywyzXYdAVJuDl83%2BnwRh869bVO79KJWhoAuncSyKPuDDJpDa2RIOGPtZfgUQvNnPUJ74YrPeOWpd8M4Mn9Q%3D%3D"
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    nx = "&nx=97"
    ny = "&ny=76"
    numOfRows = "&numOfRows=100"
    type = "&_type=json"
    api_url = url + key + date + time + nx + ny + numOfRows + type

    data = urllib.request.urlopen(api_url).read().decode('utf8')
    data_json = json.loads(data)

    parsed_json = data_json['response']['body']['items']['item']
    target_date = parsed_json[0]['fcstDate']
    target_time = parsed_json[0]['fcstTime']

    save_data= {}
    for parsed_data in parsed_json:
        if parsed_data['fcstDate'] == target_date and parsed_data['fcstTime'] == target_time:
            save_data[parsed_data['category']] = parsed_data['fcstValue']
    return save_data

if __name__ == '__main__':
    print(get_weather_data())

def get_api_date():
    standard_time = [2, 5, 8, 11, 14, 17, 20, 23]
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    check_time = int(time_now) - 1
    day_calibrate = 0
    while not check_time in standard_time :
        check_time -= 1
        if check_time < 2 :
            day_calibrate = 1
            check_time = 23

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')
    check_date = int(date_now) - day_calibrate

    return (str(check_date), (str(check_time) + '00'))
