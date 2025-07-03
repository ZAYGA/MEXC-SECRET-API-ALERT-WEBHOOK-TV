# MEXC-SECRET-API-ALERT-WEBHOOK-TV

## 1. Firt choose your folder.

```bash
mkdir MEXC_SECRET_API && cd MEXC_SECRET_API
```

## 2. Then copy repo Github.
   
```bash
git clone https://github.com/ZAYGA/MEXC-SECRET-API-ALERT-WEBHOOK-TV.git
```

## 3. Install the librairies:

```bash
pip install requests curl-cffi Flask
```

## 4. Install nrgok to receive Trading View alert webhook or others

```bash
https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
```

__Official link :__
```bash
https://ngrok.com/
```

## 5. Start Ngrok and retrieved your login credentials:

```bash
https://dashboard.ngrok.com/get-started/setup/windows
```
![image](https://github.com/user-attachments/assets/854ca53c-cdf5-4692-925a-8940b5dca9e1)

*5.1 Copy and paste on ngrok, now you are conected, then Choose the port to listen here is 5000*

```bash
ngrok http 5000
```

*5.2 Now you liste the 5000 port. They give you thise link:*

```bash
https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app
```

*5.3 Just add /webhook at the end like that:*

```bash
https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app/webhook
```

![image](https://github.com/user-attachments/assets/22e84b59-810a-4865-9747-f0bb83a1a561)

## 6. Retrieve MEXC login cookies. (use chrome)

*6.1 Creat MEXC account (referral)
```bash
https://promote.mexc.com/r/g3RinJco
```

 *6.2 Log in to your MEXC account:*
 ```bash
 https://www.mexc.com/fr-FR
```

  *6.3 Go on BTC_USDT Perp Futures Traiding page:*
  ```bash
  https://futures.mexc.com/fr-FR/exchange/BTC_USDT
  ``` 
  
  *6.4.1 Right click and open Devtool, go on **Application** then **Cookies** then **https://futures.mexc.com/** and click on u_id token and copy.*

  ![image](https://github.com/user-attachments/assets/16e63f95-7cd3-4ea7-97cd-8368676d44e5)

  *6.4.2 Then paste on the code at to part:*

  ![image](https://github.com/user-attachments/assets/0557b7f7-3dea-4925-a88a-82c815624641)


## 7. Create a webhook alert on traiding in object copy and paste that:

   The pair: ```{
    "pair": "BTC"
}```

The webhook link (exemple): ```https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app/webhook ```

The code aims to place an order as soon as it receives an alert containing the name of the peer and close along when you press enter you can modify the code to follow one of your strategies so that they are 100% automated.

**side:**  
1 = Long 
2 = Short 
3 = Close Short 
4 = Close Long 


## 8.  Start Algo & Enjoy
```bash
python lanite_v_14.py
```

Warning this is not a financial advice make your own research.

If you want to support me you can use this referal link:
https://promote.mexc.com/r/g3RinJco

If you have any questions, contact me on discord at: 
zaygargon2
