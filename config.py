import os


class Config:
    LED_COUNT = int(os.getenv('LED_COUNT', '150'))
