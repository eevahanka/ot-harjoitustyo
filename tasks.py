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

@task(test, lint)
def do(ctx):
    """ just to make my life easier
    """
    print("cheks done :)")

@task
def build(ctx):
    ctx.run("python3 src/build.py")
