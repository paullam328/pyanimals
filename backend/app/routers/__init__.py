import os
from typing import OrderedDict
from fastapi import APIRouter, status

class RouterUtils(object):
    @staticmethod
    def handle_success_response(res, code=status.HTTP_200_OK):
        data = {
            "status": "SUCCESS",
            "code": status.HTTP_200_OK,
            'result': res,
        }
        return data
    @staticmethod
    def handle_failed_response(e, code=status.HTTP_400_BAD_REQUEST):
        data = {
            "status": "FAILURE",
            "code": status.HTTP_400_BAD_REQUEST,
            "error": str(e)
        }
        return data

root_router = APIRouter()

@root_router.get("/", tags=["index"])
async def get():
    try:
        dict = OrderedDict()
        dict["name"] = "Leadpages python coding challenge"
        dict["version"] = os.environ['APP_VERSION'] if 'APP_VERSION' in os.environ else "undefined"
        dict["env"] = "production" if os.environ['APP_ENV'] == "prod" else "development"
        return RouterUtils.handle_success_response(dict)
    except Exception as e:
        return RouterUtils.handle_failed_response(e)
