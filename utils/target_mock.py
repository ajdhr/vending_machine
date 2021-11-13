from unittest import mock


def patch(target_module, target, new):
    return mock.patch(f"{target_module.__module__}.{target.__name__}", new=new)
