import importlib
import importlib.util
from pathlib import Path

plugins_dir = Path(__file__).parent / "plugins"
plugin_files = plugins_dir.glob("*.py")

plugins = []

for file in plugin_files:
    name = Path(file).name.rsplit(".", 1)[0]

    spec = importlib.util.spec_from_file_location(name, str(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    plugins.append(module.plugin)


for plugin in plugins:
    plugin.run()
