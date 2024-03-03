import click
import sys


@click.command()
@click.argument('file', type=click.File('r'), default=sys.stdin)
def nl(file):
    k = 0
    for line in file.readlines():
        k += 1
        line = line.rstrip('\n')
        click.echo(f"{k:6}  {line}")


if __name__ == '__main__':
    nl()
