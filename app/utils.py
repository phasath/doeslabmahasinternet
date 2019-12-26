from constants import brazilTimezone
from pytz import utc

def localizeTimeStampInBR(timestamp):
    localizedTimestamp = brazilTimezone.localize(timestamp)
    return localizedTimestamp.strftime('%d/%m/%Y - %H:%M:%S')

def localizeNaiveTimeStampInBR(timestamp):
    localizedTimestamp = utc.localize(timestamp).astimezone(tz=brazilTimezone)
    return localizedTimestamp.strftime('%d/%m/%Y - %H:%M:%S')