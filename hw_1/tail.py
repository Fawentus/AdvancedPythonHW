import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def tail(files):
    def echo(f, count=10):
        lines = f.readlines()
        for line in lines[-count:]:
            line = line.rstrip('\n')
            click.echo(line)

    if len(files) == 0:
        echo(sys.stdin, count=17)
    elif len(files) == 1:
        echo(open(files[0], 'r'))
    else:
        click.echo(f"==> {files[0]} <==")
        echo(open(files[0], 'r'))

        files = files[1:]
        for file in files:
            click.echo(f"\n==> {file} <==")
            echo(open(file, 'r'))


if __name__ == '__main__':
    tail()
