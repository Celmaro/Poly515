#!/usr/bin/env python3
"""Startup precheck - verify critical imports before running bot.py"""
import sys
import traceback

checks = []

# Check 1: stdlib
try:
    import os
    import asyncio
    checks.append(("stdlib", True, None))
except Exception as e:
    checks.append(("stdlib", False, str(e)))

# Check 2: nautilus_trader core
try:
    from nautilus_trader.config import TradingNodeConfig
    checks.append(("nautilus_trader.config", True, None))
except Exception as e:
    checks.append(("nautilus_trader.config", False, f"{e}\n{traceback.format_exc()}"))

# Check 3: loguru
try:
    from loguru import logger
    checks.append(("loguru", True, None))
except Exception as e:
    checks.append(("loguru", False, str(e)))

# Check 4: redis
try:
    import redis
    checks.append(("redis", True, None))
except Exception as e:
    checks.append(("redis", False, str(e)))

# Check 5: patch_gamma_markets
try:
    from patch_gamma_markets import apply_gamma_markets_patch
    checks.append(("patch_gamma_markets", True, None))
except Exception as e:
    checks.append(("patch_gamma_markets", False, f"{e}\n{traceback.format_exc()}"))

# Report
sys.stderr.write("=" * 60 + "\n")
sys.stderr.write("Poly515 PRECHECK RESULTS\n")
sys.stderr.write("=" * 60 + "\n")
failed = False
for name, ok, detail in checks:
    status = "OK" if ok else "FAIL"
    sys.stderr.write(f"  [{status}] {name}\n")
    if not ok and detail:
        sys.stderr.write(f"    {detail}\n")
    if not ok:
        failed = True

sys.stderr.write("=" * 60 + "\n")
sys.stderr.flush()

if failed:
    sys.stderr.write("PRECHECK FAILED - not starting bot.py\n")
    sys.stderr.flush()
    sys.exit(1)
else:
    sys.stderr.write("PRECHECK PASSED - starting bot.py\n")
    sys.stderr.flush()
