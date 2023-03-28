from flask import Flask
import pandas as pd
import glob

import common
import weight
import step_daily_trend
import calories_burned
import stress
import heart_rate
import sleep_stage

app = Flask(__name__)

def makeDF(type, csv):
    df = type.readCsv(csv)
    day_df = type.dayDF(df)
    return day_df

def makeDay(db, file, userId):
    for csv in file:
        if 'weight' in csv:
            weight_list = makeDF(weight, csv)
        if 'step_daily_trend' in csv:
            step_daily_trend_list = makeDF(step_daily_trend, csv)
        if 'calories_burned' in csv:
            calories_burned_list = makeDF(calories_burned, csv)
        if 'stress' in csv and 'histogram' not in csv:
            stress_list = makeDF(stress, csv)
        if 'heart_rate' in csv and 'recovery' not in csv:
            heart_rate_list = makeDF(heart_rate, csv)
        if 'sleep_stage' in csv:
            sleep_stage_list = makeDF(sleep_stage, csv)
            sleep_stage_list['user_id'] = userId
            common.saveDB(db, 'daily_sleep', sleep_stage_list)

    day = common.combine(calories_burned_list, step_daily_trend_list, stress_list, weight_list, heart_rate_list)
    day['user_id'] = userId
    common.saveDB(db, 'daily_wearable', day)
    
    day_merge = pd.merge(day, sleep_stage.sleepDF(sleep_stage_list), on='date', how='outer')
    return day_merge

@app.route('/upload/<userId>')
def upload(userId):
    db = common.connectDB()
    s3 = common.connectS3()
    common.decompress(s3, userId)

    files = glob.glob('samsunghealth/*')
    file = glob.glob(files[0] + '/*')

    day = makeDay(db, file, userId)
    week = common.periodDF(day, '1W', userId)
    month = common.periodDF(day, '1M', userId)
    average = common.avgDF(month)

    common.saveDB(db, 'weekly_wearable', week)
    common.saveDB(db, 'monthly_wearable', month)
    common.saveDB(db, 'user_average', average)

    return f'Hello, {day}!'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, ssl_context =("cert.pem", "privkey.pem"))