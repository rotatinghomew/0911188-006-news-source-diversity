# 新闻信源覆盖概览

多语种报道、引用来源和议题。当前总览只按议题合计引用次数。

样例数据均为本地合成记录，不对应真实个人、媒体、机构或交易。项目使用 Python 3.11.14 标准库，数据随项目保存，不访问外部服务。

## 使用

在项目根目录运行 `python3 -m app summary` 查看按当前基础口径生成的 JSON 总览。

## 验证

运行 `python3 -m unittest discover -s tests -v` 和 `python3 -m compileall -q app tests`。

## 结构

`data/data.json` 保存领域记录与基础汇总口径；`app/storage.py` 读取并检查数据形状；`app/analysis.py` 计算基础分组统计；`app/service.py` 组合数据读取和统计；`tests/` 验证产品入口及无效数据处理。

## 工作台

每月以有效引文的已核来源编号统计选题覆盖。执行 `python3 -m app citations` 查看有效与未核引文，`python3 -m app coverage` 查看各议题、受访群体的来源数。`assignments` 对照目标和已派任务计算缺口，`brief` 保存当月晨会简报，加 `--key 2026-06` 读取归档。

来源 `parent` 是已登记的转载上游；当前统计按各自编号计数，不沿上游追溯。`topics` 保留复核和提议，稿件 `topic` 是初标，提议不代表认可。采访任务的 `draft` 未通知记者，`sent` 已派发；已派发不表示采访已取得新来源。

操作数据在 `data/workbench.json`。工作台涉及的领域代码：`citations` 维护当前有效引文及实体复核情况, `coverage` 计算采访覆盖, `desk` 投递采访任务、保留已送任务。已有总览仍使用 `data/data.json`。
