import click

def echo(text: str, fg: str) -> None:
    click.echo(click.style(text=text, fg=fg))

def info(text: str,) -> None:
    echo(text, 'green')

def warning(text: str) -> None:
    echo(text, 'red')
