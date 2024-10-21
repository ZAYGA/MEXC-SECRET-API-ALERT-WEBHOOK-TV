1. Firt choose your folder.

2. Then copy repo Github.
   
```git clone https://github.com/ZAYGA/MEXC-SECRET-API-ALERT-WEBHOOK-TV.git```

3. Install the librairies:

```pip install requests curl-cffi Flask```

4. Install nrgok to receive Trading View alert webhook or others

```https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip```

Official link : ```https://ngrok.com/```

5. Start Ngrok and retrieved your login credentials:

```https://dashboard.ngrok.com/get-started/setup/windows```
![image](https://github.com/user-attachments/assets/854ca53c-cdf5-4692-925a-8940b5dca9e1)

Copy and paste on ngrok, now you are conected, then Choose the port to listen here is 5000

```ngrok http 5000```

Now you liste the 5000 port. They give you thise ling:
```https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app```
Just add /webhook at the end like that:
```https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app/webhook ```

6. Récuperer les cookies de connexion MEXC.

  6.1 Connectez vous à votre compte MEXC:
   ```https://www.mexc.com/fr-FR```

  6.2 Go on BTC_USDT Futures Traiding page:
  ```https://futures.mexc.com/fr-FR/exchange/BTC_USDT``` 
  
  6.3 Right click and open Devtool, go on **Application** then **Cookies** then **https://futures.mexc.com/** and click on u_id token and copy.

  ![image](https://github.com/user-attachments/assets/16e63f95-7cd3-4ea7-97cd-8368676d44e5)

  6.3.2 Then paste on the code at to part:

  ![image](https://github.com/user-attachments/assets/8a5c2d6d-2998-444e-beb5-eb64b0703dfc)

7. Create a webbok alert on traiding in object copy and paste that:

   The pair: ```{
    "pair": "ETH"
}```

The webhook link: ```https://9417-2a01-cb19-6d9-300-7c84-8278-6114-30b2.ngrok-free.app/webhook ```

The code aims to place an order as soon as it receives an alert containing the name of the peer and close along when you press enter you can modify the code to follow one of your strategies so that they are 100% automated.

side:   1 = Long 2 = Short 3 = Close Short  4 = Close Long



