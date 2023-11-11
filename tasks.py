from contextlib import contextmanager
from pathlib import Path

from invoke import task, Context


class Paths:
    here = Path(__file__).parent
    repo_root = here

    @staticmethod
    @contextmanager
    def cd(c: Context, p: Path):
        with c.cd(str(p)):
            yield


@task
def compile_requirements(c, install=False, upgrade=False):
    with Paths.cd(c, Paths.repo_root):
        upgrade_flag = "--upgrade" if upgrade else ""
        c.run(
            f"pip-compile --resolver=backtracking {upgrade_flag} -v --strip-extras  -o requirements.txt"
        )
        if install:
            c.run("pip install -r requirements.txt")
            c.run("pip install -r requirements.dev.txt")


@task
def run_streamlit(c):
    with Paths.cd(c, Paths.repo_root / "src"):
        c.run(
            "python -m streamlit run streamlit_app.py",
            pty=True,
        )
