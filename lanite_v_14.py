import requests
import hashlib
import json
import time
from curl_cffi import requests
from pprint import pprint
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("MEXC_API_KEY")

app = Flask(__name__)


def get_futures_price(symbol):
    """
    Récupère le prix actuel d'un actif sur les marchés futures de MEXC.

    :param symbol: Le symbole de l'actif à interroger, par exemple 'BTC_USDT'
    :return: Le prix actuel de l'actif ou None si une erreur survient
    """
    base_url = "https://contract.mexc.com/api/v1/contract/ticker"

    # Paramètres de la requête API
    params = {
        'symbol': symbol
    }

    try:
        # Requête GET pour obtenir les informations du marché
        response = requests.get(base_url, params=params)
        
        # Affichage du code de statut et du contenu pour débogage
    #    print(f"Statut HTTP: {response.status_code}")
    #    print("Contenu brut de la réponse:", response.text)
        
        # Vérification du code de statut HTTP
        if response.status_code == 200:
            data = response.json()

            # Affichage des données JSON pour voir la structure
            #print("Données JSON reçues:", data)
            
            # Vérifier si l'appel est un succès et récupérer le prix
            if 'data' in data:
                current_price = data['data']['lastPrice']  # Récupération du dernier prix
                return float(current_price)
            else:
                print(f"Erreur dans les données reçues: {data}")
                return None
        else:
            print(f"Erreur HTTP: {response.status_code}")
            return None

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

# Exemple d'utilisation de la fonction
symbol = 'BTC_USDT'  # Exemple de paire
price = get_futures_price(symbol)

#if price is not None:
    #print(f"Le prix actuel de {symbol} sur MEXC Futures est {price} USDT.")
#else:
    #print("Impossible de récupérer le prix.")

#price = price // 2
#print(f"La moitié du prix actuel sur {symbol} sur MEXC Futures est de {price} USDT.")



def md5_1(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

def mexc_crypto_1(key, obj):
    date_now = str(int(time.time() * 1000))
    g = md5_1(key + date_now)[7:] 
    s = json.dumps(obj, separators=(',', ':'))
    sign = md5_1(date_now + s + g)
    return {'time': date_now, 'sign': sign}

def place_order(key, obj, url):
    signature = mexc_crypto_1(key, obj)
    headers = {
        'Content-Type': 'application/json',
        'x-mxc-sign': signature['sign'],
        'x-mxc-nonce': signature['time'],
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Authorization': key
    }
    response = requests.post(url, headers=headers, json=obj)
    return response.json()
key = 'WEB87bf8dbf95937c7429b2aa67725b04e2ca8c45c0a45a34fb1dbc3843f600597c'
obj = { 
    "symbol": f"{symbol}", 
    "side": 1, 
    "openType": 1, 
    "type": "1", 
    "vol": 0.5, 
    "leverage": 20, 
    "price": f"{price}", 
    "priceProtect": "0" 
}

url = 'https://futures.mexc.com/api/v1/private/order/create'

#response = place_order(key, obj, url)
#print(response)


KEY = 'WEB87bf8dbf95937c7429b2aa67725b04e2ca8c45c0a45a34fb1dbc3843f600597c'
INTERVAL = 1 # en secondes
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Authorization': KEY
}

def md5_2(val):
    return hashlib.md5(val.encode('utf-8')).hexdigest()

def mexc_crypto_2(obj=''):
    date_now = str(int(time.time() * 1000))  
    g = md5_2(KEY + date_now)[7:]
    s = json.dumps(obj, separators=(',', ':'))  
    sign = md5_2(date_now + s + g)  
    return date_now, sign

def get_open_orders():
    date_now, sign = mexc_crypto_2()
    headers = HEADERS
    headers['x-mxc-sign'] = sign
    headers['x-mxc-nonce'] = date_now
    response = requests.get('https://futures.mexc.com/api/v1/private/order/list/open_orders?page_size=200', headers=headers)
    return response.json()

def chase_order(order_id):
    obj = {"orderId": order_id}
    date_now, sign = mexc_crypto_2(obj)
    headers = HEADERS
    headers['x-mxc-sign'] = sign
    headers['x-mxc-nonce'] = date_now
    response = requests.post('https://futures.mexc.com/api/v1/private/order/chase_limit_order', headers=headers, json=obj)
    return response.json()
    
def get_open_positions():
    date_now, sign = mexc_crypto_2()
    headers = HEADERS
    headers['x-mxc-sign'] = sign
    headers['x-mxc-nonce'] = date_now
    # Endpoint pour les positions ouvertes
    response = requests.get('https://futures.mexc.com/api/v1/private/position/open_positions', headers=headers)
    return response.json()



def compute_vol(symbol, usdt_size, price, leverage=1):
    res = requests.get('https://futures.mexc.com/api/v1/contract/detailV2?client=web')
    cs = [i['cs'] for i in res.json()['data'] if i['symbol'] == symbol][0]
    return round(usdt_size / (cs * price)) * leverage

compute_vol('BTC_USDT', 10, 80000, 1)



input("Appuyez sur 'Entrée' pour déclencher la fonction main...\n")
def main():
    symbol = "BTC_USDT"
        
    # 1. Récupérer le prix actuel
    price = get_futures_price(symbol)
    
    if price is not None:
        print(f"Le prix actuel de {symbol} sur MEXC Futures est {price} USDT.")
    else:
        print("Impossible de récupérer le prix.")
        return  # Arrêter si on ne peut pas récupérer le prix
    
    # 2. Diviser le prix par deux
    half_price = price // 2
    print(f"La moitié du prix actuel est {half_price} USDT.")

    # Calculer le prix du take profit (par exemple 20% au-dessus du prix actuel)
    takeprofit = price * 1.001
    print(f"Take Profit calculé: {takeprofit} USDT")
    
    # 3. Placer un ordre limit
    obj = { 
        "symbol": symbol, 
        "side": 1, 
        "openType": 1, 
        "type": "1", 
        "vol": 2, 
        "leverage": 20, 
        "price": str(half_price),  # Utiliser la moitié du prix
        "priceProtect": "0"
    }
    url = 'https://futures.mexc.com/api/v1/private/order/create'
    response = place_order(key, obj, url)
    print("Réponse de l'ordre:", response)
    
    # 4. Récupérer les ordres ouverts
    open_orders = get_open_orders()
    if 'data' in open_orders and len(open_orders['data']) > 0:
        order_id = open_orders['data'][0]['orderId']
        order_symbol = open_orders['data'][0]['symbol']
        print(f"Ordre ouvert détecté sur {order_symbol}, ID de l'ordre : {order_id}")
    else:
        print("Aucun ordre ouvert trouvé.")
        return  # Arrêter si aucun ordre ouvert trouvé
    
    # 5. Placer l'ordre au meilleur bid avec chase_order()

    #enter_market = False
 #   while enter_market == False:
    data = chase_order(order_id)
    if data['success']:
        print("Ordre déplacé au meilleur bid.")
    else:
        print(f"Erreur lors du déplacement de l'ordre : {data['message']}")

    input("Appuyez sur 'Entrée' pour déclencher la fonction de close du long...\n")
            # Placer un ordre de vente limit
    sell_order = {
        "symbol": symbol,
        "side":     4,    # 1 ouvri long 4 = fermer long
        "openType": 1,
        "type": "1",  # 1 = isolé,   2 = croisé
        "vol": 2,
        "leverage": 20,
        "price": str(price),
        "priceProtect": "0"
    }
    url = 'https://futures.mexc.com/api/v1/private/order/create'
    response = place_order(key, sell_order, url)
    print("Réponse de l'ordre de vente:", response)
    if response.get('success', False):
        print("Erreur lors de la récupération du prix.")    
    time.sleep(5)  # Attendre 5 secondes avant de vérifier à nouveau


    # 4. Récupérer les ordres ouverts
    open_orders = get_open_orders()
    if 'data' in open_orders and len(open_orders['data']) > 0:
        order_id = open_orders['data'][0]['orderId']
        order_symbol = open_orders['data'][0]['symbol']
        print(f"Ordre ouvert détecté sur {order_symbol}, ID de l'ordre : {order_id}")
    else:
        print("Aucun ordre ouvert trouvé.")
        return  # Arrêter si aucun ordre ouvert trouvé
    
    #  placer un ordre limit de vente 

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # 5. Placer l'ordre au meilleur ask avec chase_order()
    data = chase_order(order_id)
    if data['success']:
        print("Ordre déplacé au meilleur ask.")
    else:
        print(f"Erreur lors du déplacement de l'ordre : {data['message']}")

main()



#à rentrer dans ngrok

# 1) L'authentification:                              ngrok config add-authtoken 2QFZkFoC0WF50pW4NEd9He65l2b_?????????????????

# 2) Surveiller le localhost:                         ngrok http 5000

# 3 ) URL à entrer dans le webhook de TradingView :   https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app/webhook 




#1 pour ouvrir une position longue (acheter),
#2 pour ouvrir une position courte (vendre à découvert),
#3 pour fermer une position courte,
#4 pour fermer une position longue.