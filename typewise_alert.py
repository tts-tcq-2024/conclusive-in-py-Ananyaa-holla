temp_breach_limits = {
'PASSIVE_COOLING':{'lowerLimit':0, 'upperLimit':35},
'HI_ACTIVE_COOLING':{'lowerLimit':0, 'upperLimit':45},
'MED_ACTIVE_COOLING':{'lowerLimit':0, 'upperLimit':40}
}


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
 
  lowerLimit = temp_breach_limits[coolingType]['lowerLimit']
  upperLimit = temp_breach_limits[coolingType]['upperLimit']
  
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def display_message(recepient,message):
   print(f'To: {recepient}')
   print(f'Hi, the temperature is too {message}')

def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    display_message(recepient,"low")
  elif breachType == 'TOO_HIGH':
    display_message(recepient,"high")

batteryChar ={'coolingType':'PASSIVE_COOLING'}
check_and_alert('TO_EMAIL',batteryChar, 125)
