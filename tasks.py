"""
Development and test tasks for ansible-pull-nialov.
"""
from invoke import task


@task
def pre_commit(c):
    """
    Run pre-commit on all files.
    """
    c.run("pre-commit run --all-files")


@task
def check_playbook(c):
    """
    Check local.yml syntax.
    """
    c.run("ansible-playbook --syntax-check local.yml")


@task(pre=[pre_commit, check_playbook])
def test(c):
    """
    Test project.
    """
