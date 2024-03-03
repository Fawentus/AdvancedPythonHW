import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def wc(files):
    def echo(f):
        lines = f.readlines()
        words = sum(len(line.split()) for line in lines)
        bytes = sum(len(bytearray(line.encode('utf-8'))) for line in lines)
        return len(lines), words, bytes

    if len(files) == 0:
        lines, words, bytes = echo(sys.stdin)
        click.echo(f"{lines:8}{words:8}{bytes:8}")
    else:
        total_lines, total_words, total_bytes = 0, 0, 0
        for file in files:
            lines, words, bytes = echo(open(file, 'r'))
            click.echo(f"{lines:8}{words:8}{bytes:8} {file}")
            total_lines += lines
            total_words += words
            total_bytes += bytes
        if len(files) > 1:
            click.echo(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


if __name__ == '__main__':
    wc()
