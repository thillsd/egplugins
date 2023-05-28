from pluginBase import BasePlugin


class TestPlugin(BasePlugin):
    def run():
        print("Hello! I am a test plugin!")


plugin = TestPlugin
