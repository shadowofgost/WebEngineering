"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-12 17:51:18
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/manage.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:30:01
# @Software         : Vscode
"""
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as Runserver


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebEngineering.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    Runserver.default_addr = "localhost"  # 修改默认地址
    Runserver.default_port = "9000"  # 修改默认端口
    main()
