from genomics_demo.dna import DNA
import click

@click.command()
@click.argument('seq', type=str)
@click.option('--reverse/--no-reverse', default=False, help="Whether to reverse or not")
def get_reverse_complement(seq, reverse=False):
    """Take a DNA sequence and returns its complement"""
    complement = str(DNA(seq).compliment())
    if reverse:
        complement = complement[::-1]
    click.echo(complement)


get_reverse_complement()