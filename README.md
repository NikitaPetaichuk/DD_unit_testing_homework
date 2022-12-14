# DD Unit Testing Homework
В этом репозитории хранится решение задачи по написанию юнит-тестов от Школы систем хранения данных (Digital Design).

## Задание

```python
RaidState = Literal[
    "need_init",
    "initing",
    "need_recon",
    "reconstructing",
    "need_restripe",
    "restriping",
    "online",
    "offline",
    "degraded"
]


def raid_progresses(state: List[RaidState]) -> List[str]:
    res = []
    if "need_init" in state or "initing" in state:
        res.append("init_progress")
    if "need_recon" in state or "reconstructing" in state:
        res.append("recon_progress")
    if "need_restripe" in state or "restriping" in state:
        res.append("restripe_progress")
    return res
```

Необходимо написать unit-тесты с помощью фреймворка unittest или pytest для данной функции raid_progresses.

## Установка проекта и запуск тестов

- Необходимо склонировать себе репозиторий, после чего необходимо создать витруальное окружение внутри с помощью средств IDE или с помощью команд:

```shell
python3 -m venv ./.venv
source ./.venv/bin/activate # Activate virtualenv 
```
- Установка всех необходимых зависимостей

```shell
pip3 install -r requirements.txt
```

- Запуск юнит-тестов

```shell
pytest unit_tests/
```
