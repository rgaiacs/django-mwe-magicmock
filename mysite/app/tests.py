import logging
from unittest.mock import patch

from django.test import TestCase

from .models import Resource

logger = logging.getLogger(__name__)

@patch("app.models.GitHosting.get_version")
class ResourceTestCase(TestCase):
    def test_add_resource(self, mock_get_version):
        mock_get_version = "5678"

        logger.error("Testing ...")

        resource = Resource.objects.create(code_repository="http://mygit.com/foo/bar")

        self.assertEqual(resource.version, "5678")