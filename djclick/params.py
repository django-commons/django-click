from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import click
from django.core.exceptions import ObjectDoesNotExist

if TYPE_CHECKING:
    from django.db import models


class ModelInstance(click.ParamType):
    def __init__(
        self,
        qs: type[models.Model] | models.QuerySet[Any],
        lookup: str = "pk",
    ) -> None:
        from django.db import models

        if isinstance(qs, type) and issubclass(qs, models.Model):
            qs = cast(Any, qs).objects.all()
        self.qs = qs
        self.name = f"{qs.model._meta.app_label}.{qs.model.__name__}"
        self.lookup = lookup

    def convert(
        self,
        value: Any,
        param: click.Parameter | None,
        ctx: click.Context | None,
    ) -> Any:
        if value is None:  # NOCOV
            return super().convert(value, param, ctx)
        try:
            return self.qs.get(**{self.lookup: value})
        except ObjectDoesNotExist:
            pass
        # call `fail` outside of exception context to avoid nested exception
        # handling on Python 3
        msg = "could not find {s.name} with {s.lookup}={value}".format(
            s=self, value=value
        )
        self.fail(msg, param, ctx)
