from datetime import datetime


def epoch_to_datetime(epoch):
    return int(datetime.fromtimestamp(epoch).timestamp())
