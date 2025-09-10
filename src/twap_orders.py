import time
import json
import typer
from decimal import Decimal as d
from binance.error import ClientError

from .binance_client import get_client
from .utils import parse_symbol_filters, quantize_qty
from .logger_config import log

app = typer.Typer(help="TWAP Order Placement")

@app.command()
def twap(
    symbol: str = typer.Argument(..., help="Trading pair, e.g., BTCUSDT"),
    total_qty: float = typer.Argument(..., help="Total quantity to trade, e.g., 0.01"),
    side: str = typer.Argument(..., help="Order side: BUY or SELL"),
    interval: int = typer.Argument(..., help="Interval between orders in seconds"),
    parts: int = typer.Argument(..., help="Number of slices to break the order into"),
):
   
    side = side.upper()
    if side not in {"BUY", "SELL"}:
        raise typer.BadParameter("side must be BUY or SELL")

    client = get_client()
    ex = client.exchange_info()
    f = parse_symbol_filters(ex, symbol)

    # divide into equal parts
    qty_per_order = total_qty / parts
    qty_per_order = quantize_qty(d(qty_per_order), f["stepSize"])

    log.info(f"TWAP strategy -> {parts} parts, {qty_per_order} per order, interval={interval}s")

    for i in range(parts):
        try:
            resp = client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=float(qty_per_order)
            )
            log.info(f"TWAP {side} {symbol} part {i+1}/{parts}: {json.dumps(resp)}")
            typer.echo(json.dumps(resp, indent=2))
        except ClientError as e:
            log.error(f"ClientError {e.status_code} {e.error_message}")
            typer.echo(str(e))
            raise typer.Exit(code=1)

        if i < parts - 1:
            time.sleep(interval)
