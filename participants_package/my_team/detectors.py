"""Surveillance detectors. Each detector is a stateful class with one `check` method.

骨架阶段：三个 check 全部返回 None。后续在这里填规则/LLM 逻辑即可，
不需要再动 submission.py 或 my_exchange.py。
"""

from __future__ import annotations

from typing import Iterable, List, Mapping, Optional

from competition_solution.exchange import Alert, LimitOrderBook, Order, Trade


class WashDetector:
    """Detect wash trading (same beneficial owner on both sides)."""

    def __init__(self) -> None:
        pass

    def on_pre_submit(self, order: Order, book: LimitOrderBook) -> Optional[Alert]:
        # TODO: 同 entity 自买自卖的预交易拦截
        return None

    def on_trades(
        self,
        trades: Iterable[Trade],
        order_snapshots: Mapping[str, Order],
    ) -> List[Alert]:
        # TODO: 同 entity 撮合后预警 + 关联账户对倒环检测
        return []


class SpoofDetector:
    """Detect spoofing / quote stuffing (large orders cancelled fast)."""

    def __init__(self) -> None:
        pass

    def on_cancel(
        self,
        order: Order,
        timestamp: int,
        book: LimitOrderBook,
    ) -> Optional[Alert]:
        # TODO: 大单 + 快速撤单 + 远离盘口
        return None


class PumpDumpDetector:
    """Detect coordinated pump-and-dump across multiple entities.

    Baseline 完全未实现，是任务二的最大提分点。
    """

    def __init__(self) -> None:
        pass

    def on_trades(
        self,
        trades: Iterable[Trade],
        order_snapshots: Mapping[str, Order],
        tick: int,
    ) -> List[Alert]:
        # TODO: 多账户协同拉升后集中卖出
        return []
