# Database Structure

## users:
    - user Id
    - user name
    - user password

## transactions:
    - transaction Id
    - user Id
    - amount (+ve deposit, -ve withdrawal)

## portfolios:
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
    - order Id1
    - order Id2
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