import os
from typing import OrderedDict
from fastapi import APIRouter, status

class BaseRouter(object):
    router = APIRouter()

    def handle_success_response(self, res, code=status.HTTP_200_OK):
        data = {
            "status": "SUCCESS",
            "code": status.HTTP_200_OK,
            'result': res,
        }
        return data

    def handle_failed_response(self, e, code=status.HTTP_400_BAD_REQUEST):
        data = {
            "status": "FAILURE",
            "code": status.HTTP_400_BAD_REQUEST,
            "error": str(e)
        }
        return data
    
    @router.get("/", tags=["index"])
    async def get(self):
        try:
            dict = OrderedDict()
            dict["name"] = "Leadpages python coding challenge"
            dict["version"] = os.environ['APP_VERSION'] if 'APP_VERSION' in os.environ else "undefined"
            dict["env"] = "production" if os.environ['APP_ENV'] == "prod" else "development"
            return self.handle_success_response(dict)
        except Exception as e:
            return self.handle_failed_response(e)
