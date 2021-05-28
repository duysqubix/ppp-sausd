from django.shortcuts import render
import requests
# Create your views here.

def main_view(req):
    params = {
        'rand': None,
        'usd': None,
        'orig': 1,
        'active': False
    }
    if req.POST:
        url = "https://api.purchasing-power-parity.com/"
        resp = requests.get(url, params={'target': 'ZA'})
        data = resp.json()
        try:
            ex_rate = float(data['ppp']['currencyMain']['exchangeRate'])
            conv_rate = float(data['ppp']['pppConversionFactor'])
            _from = req.POST['fromCurrency']
            _to = req.POST['toCurrency']

            value = float(req.POST['currencyValue'])
            if _from == "USD":
                ans_usd = round(value*conv_rate, 2)
                ans_rand = round(ans_usd*ex_rate,2)

            if _from == "ZAR":
                ans_rand = round(value*(1-conv_rate), 2)
                ans_usd = round(ans_rand/ex_rate,2)
            params['rand'] = ans_rand
            params['usd'] = ans_usd
            params['active'] = True
            params['orig'] = value
            params['from'] = _from
            params['to']  = _to
        except:
            pass

    print(params)
    return render(req, "index.html", params)
