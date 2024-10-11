import datetime

class AnimalMapper(object):

    # Mapper to map response object returned by the external API to output response object
    @staticmethod
    def map_resp_to_output(resp):
        resp["friends"] = resp["friends"].split(",") if "friends" in resp else None
        if "born_at" in resp and resp["born_at"] is not None:
            # Assuming that timestamp is in ms:
            timestamp = resp["born_at"] / 1000
            resp["born_at"] = datetime.datetime.fromtimestamp(timestamp, datetime.UTC).isoformat()
        return resp
