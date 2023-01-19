# get_cop_exchange_rates.py
# 2023-01-18 | CR

import datetime
import os
import sys
import warnings
from bs4 import BeautifulSoup
import requests


# Send telegram messages


def send_tg_message(message):
    try:
        bot_token = os.environ['TELEGRAM_BOT_TOKEN']
        user_id = os.environ['OWNER']
        # Send the message
        url = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + user_id + '&text=' + str(message)
        response = requests.get(url)
        print(response.content)
    except Exception as err:
        print(f'ERROR on send_tg_message: {str(err)}')
    return response


def report_error_to_tg_group(api_response):
    if not api_response['error']:
        return
    message = {
        'type': 'ERROR in a Mediabros API',
        'app_name': os.environ.get('APP_NAME'),
        'server_name': os.environ.get('SERVER_NAME'),
        'calling_func': sys._getframe(1).f_code.co_name,
        'error_message': api_response['error_message'],
    }
    print(f'send_tg_message: {message}')
    return send_tg_message(message)


# API functions

def get_api_standard_response():
    standard_response = dict()
    standard_response['error'] = False
    standard_response['error_message'] = ''
    standard_response['data'] = dict()
    return standard_response


def get_formatted_date():
    date_format = "%Y-%m-%d %H:%M:%S UTC"
    formatted_date = datetime.date.strftime(
        datetime.datetime.utcnow(), date_format
    )
    return formatted_date


def get_currency_section_value_2(soup, api_response, id_name, currency):
    error_message = []
    error_flag = False
    exchange_value = None
    currency_symbol = None
    effective_date = None
    # Locate the element with specified id
    try:
        currentSection = soup.find("div", {"id": id_name})
    except Exception as err:
        error_flag = True
        error_message = f'id "{id_name}" not found | {str(err)}'
    # Scrape the first <div> inside it to get the exchange rate
    if not error_flag:
        try:
            first_div = currentSection.find_all("div")[0]
        except Exception as err:
            error_flag = True
            error_message = f'1st <div> not found | {str(err)}'
    # Scrape the "data-exchange-rate" attribute
    if not error_flag:
        try:
            exchange_value = first_div['data-exchange-rate'].strip()
        except Exception as err:
            error_flag = True
            error_message = 'The "data-exchange-rate" attribute' + \
                f' in 1st <div> not found | {str(err)}'
    # Scrape the second <div> to get the effective date
    if not error_flag:
        try:
            second_div = currentSection.find_all("div")[0]
        except Exception as err:
            error_flag = True
            error_message = f'2nd <div> not found | {str(err)}'
    # Scrape the <span> element, get the text attribute
    # with the effective date/time
    if not error_flag:
        try:
            effective_date = second_div.find("span").text.strip()
            effective_date = effective_date.replace(' · ', '')
        except Exception as err:
            error_flag = True
            error_message = 'The <span> in 2nd <div> not found' + \
                f' trying to get the effective date/time | {str(err)}'
    # Scrape the 2nd <div> element inside the 1st <div>
    if not error_flag:
        try:
            second_div_1st_div = first_div.find_all("div")[1]
        except Exception as err:
            error_flag = True
            error_message = f'The <span> in 2nd <div> not found | {str(err)}'
    # Scrape the 2nd <span> element, get the text attribute with curreny name
    if not error_flag:
        try:
            currency_symbol = second_div_1st_div.find_all(
                "span"
            )[1].text.strip()
        except Exception as err:
            error_flag = True
            error_message = 'The <span> in 2nd <div> not found'
            f', trying to get the currency name | {str(err)}'

    api_response['data'][currency] = dict()
    api_response['data'][currency]['unit'] = currency_symbol
    api_response['data'][currency]['value'] = exchange_value
    api_response['data'][currency]['effective_date'] = effective_date

    if error_flag:
        api_response['error'] = True
        api_response['error_message'] = f'ERROR(s) on id "{id_name}"'
        api_response['data'][currency]['error_message'] = error_message


def get_currency_section_value(soup_root, api_response, id_name):
    error_message = []
    error_flag = False
    exchange_value = None
    currency_symbol = None
    effective_date = None
    # Locate the element with specified id
    try:
        soup = soup_root.find("main")
    except Exception as err:
        error_flag = True
        error_message = f'main section not found | {str(err)}'
    if not error_flag:
        try:
            currentSection = soup.find("div", {"jsname": id_name[0]})
        except Exception as err:
            error_flag = True
            error_message = f'jsname "{id_name[0]}" not found | {str(err)}'
    # Scrape the first <div> inside it to get the exchange rate
    if not error_flag:
        try:
            first_div = currentSection.find("div")
        except Exception as err:
            error_flag = True
            error_message = f'1st <div> not found | {str(err)}'
    # Scrape the exchange-rate text
    if not error_flag:
        try:
            exchange_value = first_div.text.strip().replace(',', '')
        except Exception as err:
            error_flag = True
            error_message = 'The text' + \
                f' in 1st <div> not found | {str(err)}'
    # Scrape the second <div jsname> to get the effective date
    try:
        currentSection = soup.find("div", {"jsname": id_name[1]})
    except Exception as err:
        error_flag = True
        error_message = f'jsname "{id_name[1]}" not found | {str(err)}'
    # Scrape the text attribute with the effective date/time
    if not error_flag:
        try:
            effective_date = currentSection.text.strip()
            effective_date = effective_date.replace(' · Disclaimer', '')
        except Exception as err:
            error_flag = True
            error_message = 'The text cannot be retrieved,' + \
                f' trying to get the effective date/time | {str(err)}'
    # Scrape the <div role> to get the curreny name
    try:
        currentSection = soup.find("div", {"role": id_name[2]})
    except Exception as err:
        error_flag = True
        error_message = f'role "{id_name[2]}" not found | {str(err)}'
    # Scrape the text attribute with curreny name
    if not error_flag:
        try:
            currency_symbol = currentSection.text.strip()
            currency_symbol = currency_symbol.replace('Home', '')
            currency_symbol = currency_symbol.replace(' • Currency', '')
        except Exception as err:
            error_flag = True
            error_message = 'The text cannot be retrieved,'
            f', trying to get the currency name | {str(err)}'

    api_response['data'] = dict()
    api_response['data']['unit'] = currency_symbol
    api_response['data']['value'] = exchange_value
    api_response['data']['effective_date'] = effective_date

    if error_flag:
        api_response['error'] = True
        api_response['error_message'] = f'ERROR(s) on id "{str(id_name)}"'
        api_response['data']['error_message'] = error_message


def get_google_cop():
    api_response = get_api_standard_response()
    # url = "https://www.google.com/search?q=dolar+cop"
    url = "https://www.google.com/finance/quote/USD-COP"
    try:
        response = requests.get(url=url)
    except requests.exceptions.SSLError:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(url=url, verify=False)
        except Exception as err:
            api_response['error'] = True
            api_response['error_message'] = str(err)
    except Exception as err:
        api_response['error'] = True
        api_response['error_message'] = str(err)

    if api_response['error']:
        return api_response
    soup = BeautifulSoup(response.text, "html.parser")
    # print(f'>>--> url = {url}')
    # print(f'>>--> soup.body = {str(soup.body)}')
    # get_currency_section_value_2(
    #     soup,
    #     api_response,
    #     "knowledge-currency__updatable-data-column",
    #     'cop'
    # )
    get_currency_section_value(
        soup,
        api_response,
        ['ip75Cb', 'Vebqub', 'heading'],
    )
    api_response['run_timestamp'] = get_formatted_date()
    report_error_to_tg_group(api_response)
    return api_response


def get_official_cop():
    api_response = get_api_standard_response()
    url = 'https://www.datos.gov.co/api/id/32sa-8pi3.json?' + \
        '$query=select%20*%2C%20%3Aid%20order%20by%20%60vigenciadesde' + \
        '%60%20desc%20limit%201'
    try:
        response = requests.get(url)
    except Exception as err:
        api_response['error'] = True
        api_response['error_message'] = str(err)
    else:
        if response.status_code == 200:
            api_response['data'] = response.json()[0]
        else:
            api_response['error'] = True
            api_response['error_message'] = 'ERROR reading ' + \
                'datos.gov.co USD/COP API'
    api_response['run_timestamp'] = get_formatted_date()
    report_error_to_tg_group(api_response)
    return api_response


def get_cop_exchange_rates():

    api_response = get_api_standard_response()

    api_response['data']['google_cop'] = get_google_cop()
    api_response['data']['official_cop'] = get_official_cop()

    if api_response['data']['google_cop']['error']:
        api_response['error'] = True
        api_response['error_message'] = \
            ', ' if api_response['error_message'] != '' else '' + \
            api_response['data']['google_cop']['error_message']

    if api_response['data']['official_cop']['error']:
        api_response['error'] = True
        api_response['error_message'] = \
            ', ' if api_response['error_message'] != '' else '' + \
            api_response['data']['official_cop']['error_message']

    return api_response
