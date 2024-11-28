import logging
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from .models import Resource

logger = logging.getLogger(__name__)

@patch("app.models.GitHosting.get_version")
class ResourceTestCase(TestCase):
    def test_add_resource(self, mock_get_version):
        mock_get_version = "5678"

        logger.error("Adding resource ...")

        resource = Resource.objects.create(code_repository="http://mygit.com/foo/bar")

        self.assertEqual(resource.version, "HEAD")

@patch("app.models.GitHosting.get_version")
class ResourceViewTestCase(TestCase):
    def test_add_resource(self, mock_get_version):
        mock_get_version = "5678"

        logger.error("Submitting form ...")

        response = self.client.post(reverse("app:index"), {
            "code_repository": "http://mygit.com/foo/bar"
        })

        resource = Resource.objects.get(id=1)

        self.assertEqual(resource.version, "5678")