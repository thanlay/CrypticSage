class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        """Registers a new plugin."""
        self.plugins[name] = plugin

    def execute_plugin(self, name, *args, **kwargs):
        """Executes a plugin by name."""
        plugin = self.plugins.get(name)
        if not plugin:
            raise ValueError(f"Plugin {name} not found")
        return plugin(*args, **kwargs)