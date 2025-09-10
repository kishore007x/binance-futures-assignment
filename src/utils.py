from decimal import Decimal
from typing import Dict, Any

def parse_symbol_filters(exchange_info: Dict[str, Any], symbol: str):
    
    for s in exchange_info["symbols"]:
        if s["symbol"] == symbol:
            lot = next(f for f in s["filters"] if f["filterType"] == "LOT_SIZE")
            price = next(f for f in s["filters"] if f["filterType"] == "PRICE_FILTER")
            return {
                "stepSize": Decimal(lot["stepSize"]),
                "minQty": Decimal(lot["minQty"]),
                "tickSize": Decimal(price["tickSize"]),
            }
    raise ValueError(f"Symbol {symbol} not found")

def quantize_qty(qty: Decimal, step: Decimal) -> Decimal:
    return (qty // step) * step

def quantize_price(price: Decimal, tick: Decimal) -> Decimal:
    return (price // tick) * tick

def d(x) -> Decimal:
    return Decimal(str(x))
