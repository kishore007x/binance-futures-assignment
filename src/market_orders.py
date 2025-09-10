import json
import typer
from binance.error import ClientError
from src.binance_client import get_client
from src.utils import d, parse_symbol_filters, quantize_qty
from src.logger_config import get_logger

app = typer.Typer()
log = get_logger("market")

@app.command()
def place(
    quantity: float = typer.Argument(..., help="Order quantity, e.g. 0.001"),
    side: str = typer.Argument(..., help="Order side: BUY or SELL"),
    symbol: str = typer.Argument(..., help="Trading pair, e.g. BTCUSDT")
):
    
    side = side.upper()
    if side not in {"BUY", "SELL"}:
        raise typer.BadParameter("side must be BUY or SELL")

  
    client = get_client()
    ex = client.exchange_info()
    f = parse_symbol_filters(ex, symbol)

   
    qty = quantize_qty(d(quantity), f["stepSize"])
    if qty <= 0:
        raise typer.BadParameter("quantity too small")

    
    try:
        resp = client.new_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=float(qty)
        )
        log.info(f"MARKET {side} {symbol} {qty} -> {json.dumps(resp)}")
        typer.echo(json.dumps(resp, indent=2))
    except ClientError as e:
        log.error(f"ClientError {e.status_code} {e.error_message}")
        typer.echo(str(e))
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
