import shutil
from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.sdist import sdist


def copy_json_schemas(target_dir: Path) -> None:
    schema_src = Path("json")
    if not schema_src.exists():
        return
    schema_dest = target_dir / "impresso_schemas" / "json"
    if schema_dest.exists():
        shutil.rmtree(schema_dest)
    shutil.copytree(schema_src, schema_dest)


class BuildPy(build_py):
    def run(self):
        super().run()
        copy_json_schemas(Path(self.build_lib))


class Sdist(sdist):
    def make_release_tree(self, base_dir, files):
        super().make_release_tree(base_dir, files)
        copy_json_schemas(Path(base_dir))


setup(
    cmdclass={
        "build_py": BuildPy,
        "sdist": Sdist,
    },
)
