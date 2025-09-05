# Database Structure

## user:
    - user Id
    - user name

## transactions:
    - transaction Id
    - user Id
    - amount (+ve deposit, -ve withdrawal)

## portfolio:
    - portfolio Id
    - user Id
    - instrument Id
    - quantity
    - avg price
    - last order date

## portfolioReturns:
    - return Id
    - portfolio Id
    - date
    - daily return
    - cumulative return

## order:
    - order Id
    - user Id
    - instrument Id
    - date
    - status
    - order type (buy sell)
    - price (bid ask)
    - order quantity

## trade:
    - trade Id
    - order Id
    - user Id
    - instrument Id
    - date
    - order type (buy sell)
    - traded price
    - filled quantity
    
## Instrument:
    - instrument Id
    - ticker
    
## price:
    - instrument Id
    - date
    - price
    - volume