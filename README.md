# python-wechaty-plugin-<foo>

<foo> plugin which ...

## Features

this plugin contains the following features:

* feature
* ...

## Quick Start

### Install

```shell
pip install wechaty wechaty-plugin-<foo>
```

## Init Bot

```python
import asyncio
from wechaty import Wechaty

from wechaty_plugin_<foo> import <Foo>Plugin


async def run() -> None:
    """async run method"""
    plugin = <Foo>Plugin
    bot = Wechaty().use(plugin)
    await bot.start()


asyncio.run(run()) 
```

### v0.0.1 (Apr 2022)

The `python-wechaty-plugin-<foo>` project was created. 

## Maintainers

- [<author>](https://github.com/<author>)

## Copyright & License

- Code & Docs © 2022 [<author>](<author_email>)
- Code released under the Apache-2.0 License
- Docs released under Creative Commons