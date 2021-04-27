from invoke import task

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
@task
def test(ctx):
    ctx.run("pytest src")

@task
def start(ctx):
    ctx.run("python3 src/start.py")


@task
def lint(ctx):
    ctx.run("pylint src")
