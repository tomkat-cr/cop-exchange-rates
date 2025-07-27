import sys
import json

from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

from cop import get_cop_exchange_rates, \
    get_google_cop, get_official_cop


def get_command_line_args():
    params = dict()
    params['mode'] = 'api'
    params['config_filename'] = '.env'
    if len(sys.argv) > 1:
        params['mode'] = sys.argv[1]
    if len(sys.argv) > 2:
        params['config_filename'] = sys.argv[2]
    return params


params = get_command_line_args()
if params['mode'] == 'cli':
    apiResponse = get_cop_exchange_rates()
    print(json.dumps(apiResponse))

api = FastAPI()
app = ASGIMiddleware(api)


@api.get("/get_exchange_rates")
def get_rates():
    api_response = get_cop_exchange_rates()
    return api_response


@api.get("/get_official_cop")
def get_rates_official():
    return get_official_cop()


@api.get("/get_google_cop")
def get_rates_from_google():
    return get_google_cop()
