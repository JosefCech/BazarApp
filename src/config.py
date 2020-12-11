import os


class EnvVariable:
    def __init__(self, name: str):
        self._name = name
        self._value = os.environ.get(self._name)

    def get(self):
        return self._value


config = {
    "ImageS3Bucket": EnvVariable("PhotoBucket").get()
}
