import matplotlib
matplotlib.use('agg')

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import time

#relay_pin = 26
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(relay_pin, GPIO.OUT)

#sensor = Adafruit_DHT.DHT22
#dht_pin23


temperature=np.arange(0, 11, 0.1)
humidity=np.arange(0, 11, 0.1)

temperature_cold = fuzz.gaussmf(temperature, 0, 1.5)
temperature_warm = fuzz.gaussmf(temperature, 5, 1.5)
temperature_hot = fuzz.gaussmf(temperature, 10, 1.5)

humidity_low = fuzz.trapmf(humidity, [0, 0, 1, 3])
humidity_high = fuzz.gaussmf(humidity, 10, 1.5)

comfort = np.arange(0, 30, 0.1)
comfort_low = fuzz.trimf(comfort, [0, 5, 10])
comfort_ave = fuzz.trimf(comfort, [10, 15, 20])
comfort_very = fuzz.trimf(comfort, [20, 25, 30])

def temperature_category(temperature_in=18):
    temperature_cat_cold = fuzz.interp_membership(temperature,temperature_cold,temperature_in)
    temperature_cat_warm = fuzz.interp_membership(temperature,temperature_warm,temperature_in)
    temperature_cat_hot =  fuzz.interp_membership(temperature,temperature_hot,temperature_in)
    return dict(cold=temperature_cat_cold, warm=temperature_cat_warm, hot=temperature_cat_hot)

def humidity_category(humidity_in=2):
    humidity_cat_low = fuzz.interp_membership(humidity,humidity_low, humidity_in)
    humidity_cat_high = fuzz.interp_membership(humidity,humidity_high, humidity_in)
    return dict(low=humidity_cat_low, high=humidity_cat_high)

print('saving membership......')

fig, ax = plt.subplots(2, 1)

[t1,t2,t3] = ax[0].plot(temperature, temperature_cold, 'r', temperature, temperature_warm, 'm+', temperature, temperature_hot, 'b--', label=['Temp. cold', 'Temp. warm', 'Temp. hot'])
ax[0].set_ylabel('Fuzzy membership')
ax[0].set_title('Temperature')
ax[0].set_ylim(-0.05, 1.05)
ax[0].set_xlim(0, 10)

lgd1 = ax[0].legend([t1,t2,t3], ['Temp. cold', 'Temp. warm', 'Temp. hot'], loc='center left', bbox_to_anchor=(1, 0.5))

[t1,t2] = ax[1].plot(humidity, humidity_low, 'r', humidity, humidity_high, 'b+')
ax[1].set_ylabel('Fuzzy membership')
ax[1].set_title('Humidity')
ax[1].set_ylim(-0.05, 1.05)
ax[1].set_xlim(0, 10)

lgd2 = ax[1].legend([t1,t2], ['Hum. low', 'Hum. high', 'Temp. hot'], loc='center left', bbox_to_anchor=(1, 0.5))


plt.grid(True)
plt.tight_layout()
plt.show()
fig.savefig('fuzzy_mem_temp_hum.png', dpi=100, bbox_extra_artists=(lgd1, lgd2), bbox_inches='tight')
print('done')

print('Program karar temelli bulanik mantik vermeye hazir')

machine_state = -1

while 1:

    #sen_humidity,sen_temperature = Adafruit_DHT.read_retry(sensor, dht_pin)

    if humidity is not None and temperature is not None:
        #print('Sensing: Temperature={0:0.1f}*C   Humidity={1:0.1f}%'.format(sen_temperature, sen_humidity))
        #sen_temperature=18
        #sen_humidity=80
        t1 = input("Oda sicakligini giriniz?")
        t11 = float(t1)
        t2 = input("Oda nemini giriniz?")
        t22 = float(t2)
        print('sensing: Temperature={0:0.1f}*C   Humidity={1:0.1f}%'.format(t11,t22))

        t11=18
        t22=60

        norm_temperature = t11 / 60
        norm_humidity = t22 / 18

        print('Normalization: Temperature={0:0.0001f}  Humidity={1:0.0001f}'.format(norm_temperature, norm_humidity))

        temp_in = temperature_category(norm_temperature)
        hum_in = humidity_category(norm_humidity)

        print('fuzyy membership: Temperature={0}   Humidity={1}'.format(temp_in, hum_in))

        rule1 = np.fmax(temp_in['hot'], hum_in['low'])
        rule2 = temp_in['warm']
        rule3 = np.fmax(temp_in['warm'], hum_in['high'])

        imp1 = np.fmin(rule1, comfort_low)
        imp2 = np.fmin(rule2, comfort_ave)
        imp3 = np.fmin(rule3, comfort_very)

        aggregate_membership = np.fmax(imp1, imp2, imp3)

        result_comfort = fuzz.defuzz(comfort, aggregate_membership, 'centroid')

        print(result_comfort)


        #if result_comfort >= 5.002:
           #if machine_state < 0:
               #machine_state=1
               #print('makineyi ac')
               #GPIO.output(relay_pin, GPIO.HIGH)
           #else
               #print('makine zaten acik')
        #else:
           #if machine_state > 0:
              #machine state=0
              #print('makineyi kapat')
              #GPIO.output(relay_pin, GPIO.LOW)
           #else:
               #print('makine zaten kapalı')

            #time.sleep(2)

#except KeyboardInterrupt:
      #GPIO.output(relay_pin, GPIO.LOW)
      #GPIO.cleanup()

#print('Programdan cik')












