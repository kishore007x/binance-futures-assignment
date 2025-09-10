import json
import typer
from binance.error import ClientError
from src.binance_client import get_client
from src.utils import d, parse_symbol_filters, quantize_qty, quantize_price
from src.logger_config import get_logger

app = typer.Typer()
log = get_logger("limit")

@app.command()
def place(symbol: str, side: str, quantity: float, price: float):
    """Place a LIMIT order"""
    side = side.upper()
    if side not in {"BUY", "SELL"}:
        raise typer.BadParameter("side must be BUY or SELL")

    client = get_client()
    ex = client.exchange_info()
    f = parse_symbol_filters(ex, symbol)

    qty = quantize_qty(d(quantity), f["stepSize"])
    px = quantize_price(d(price), f["tickSize"])

    try:
        resp = client.new_order(
            symbol=symbol, side=side, type="LIMIT",
            timeInForce="GTC", quantity=float(qty), price=float(px)
        )
        log.info(f"LIMIT {side} {symbol} {qty}@{px} -> {json.dumps(resp)}")
        typer.echo(json.dumps(resp, indent=2))
    except ClientError as e:
        log.error(f"ClientError {e.status_code} {e.error_message}")
        typer.echo(str(e))
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
