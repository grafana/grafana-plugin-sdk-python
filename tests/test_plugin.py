from unittest import TestCase

from sdk.plugin import BasePlugin, Server


class FakePlugin(BasePlugin):

    def CheckHealth(self, request, context):
        pass

    def CollectMetrics(self, request, context):
        pass

    def QueryData(self, request, context):
        pass

    def CallResource(self, request, context):
        pass


class TestPlugin(TestCase):

    def test_plugin_created(self):

        plugin = Server(FakePlugin)

        self.assertIsInstance(plugin, Server)
