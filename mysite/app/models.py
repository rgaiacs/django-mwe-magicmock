import logging

from django.core.exceptions import ValidationError
from django.db import models

from .aid import GitHosting

logger = logging.getLogger(__name__)

class Resource(models.Model):
    code_repository = models.URLField(
        help_text="Link to the repository where the un-compiled, human readable code and related code is located."
    )
    version = models.CharField(
        blank=True,
        # Git hash contains 40 characters
        max_length=50,
        default="HEAD",
        help_text="The version of the resource in the format of a Git commit ID or Git tag.",
    )

    def clean(self):
        """
        NOT invoked when you call your model’s save() method.

        Check if the resource really exists.
        """
        logger.error("Cleaning data ...")

        if len(self.code_repository) == 0:
            raise ValidationError("Code repository is empty.")

        git_host = GitHosting()
        self.version = git_host.get_version()