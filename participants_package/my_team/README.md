# my_team

任务二（交易所 + 监管）开发目录。

- `submission.py` — 评测入口，不改签名
- `my_exchange.py` — `MyRegulator` 替换 baseline `RegulatoryAgent`，注入 baseline `ExchangeAgent`
- `detectors.py` — `WashDetector` / `SpoofDetector` / `PumpDumpDetector` 三个空壳，逻辑后续填
