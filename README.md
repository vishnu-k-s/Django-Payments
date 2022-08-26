                        PAYPAL PAYMENTS


STEPS

    - Create a paypal account
    - Create a sandbox personal & businness account
    - Crate an app to get keys

    1. Standard Checkout Payments
        - Add the payment buttons to web page
                add the PayPal JavaScript SDK code to your checkout page provided in the documentation
        - Buyer clicks the button
        - The button calls the PayPal Orders API to set up a transaction
        - The button launches the PayPal Checkout experience
        - The buyer approves the payment
        - The button calls the PayPal Orders API to finalize the        transaction
        - Show a confirmation message to buyer
        - Test the purchase by logging into sandbox accounts

    2. Payment through API'S
        1. API to Generate access_token
            - POST : https://api.sandbox.paypal.com/v1/oauth2/token 
            - Select Auth -> Basic Auth
                username = Client ID
                password = Client secret id
                under Dashboard > My Apps & Credentials.
            - Header: Content-Type -> application/x-www-form-urlencoded
            - body: form-urlencoded
                key: grant_type
                value: client_credentials
            - get access token from response

        2. API to make payment
            - POST : https://api-m.sandbox.paypal.com/v1/payments/payment
            - Select Headers: Authorization -> Bearer <access token>
            - body : json data (ex provided in offical doc, link in below)
            - get approval url from response paste it in browser 
            - login to sandbox account(personal) and make payment
            - This wll redirect into a sucess url provided in the body
              get PayerID from url
        
        3. API to accept paymetn
            - POST : url in execute url from response of 2nd api call
            - Select Headers: Authorization -> Bearer <access token>
            -  body : {
                        "payer_id" : "#######" =PayerID  
                      }
            - look the response for more information


TECHNOLOGY STACK

    * Python – Django
    * HTML
    * JavaScript


REFERENCES

    - https://developer.paypal.com/docs/checkout/standard/integrate/
    - https://youtu.be/ejaUtmpns7s

    - https://youtu.be/tkN4EQt1P6I
    - https://developer.paypal.com/docs/archive/payments/paypal-payments/