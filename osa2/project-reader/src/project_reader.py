from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_data = toml.loads(content)

        # Haetaan modernin formaatin mukaisesti:
        name = toml_data.get("project", {}).get("name", "")
        description = toml_data.get("project", {}).get("description", "")
        dependencies = toml_data.get("project", {}).get("dependencies", [])
        dev_dependencies = toml_data.get("dependency-groups", {}).get("dev", [])

        return Project(name, description, dependencies, dev_dependencies)
