import click
from .parsers.apache_parser import parse_apache
from .parsers.ssh_parser import parse_ssh
from .parsers.windows_parser import parse_windows
from .report import generate_report

@click.command()
@click.option('--type', '-t', type=click.Choice(['apache', 'ssh', 'windows']), required=True, help='Log type')
@click.option('--file', '-f', required=True, type=click.Path(exists=True), help='Path to log file')
@click.option('--output', '-o', default='report.txt', help='Output file for report')
def main(type, file, output):
    """LogHunter - Parse security logs and detect threats."""
    click.echo(f"[*] Parsing {type} log: {file}")
    
    if type == 'apache':
        df = parse_apache(file)
    elif type == 'ssh':
        df = parse_ssh(file)
    elif type == 'windows':
        df = parse_windows(file)
    else:
        click.echo("Unsupported log type")
        return
    
    if df.empty:
        click.echo("[-] No relevant entries found.")
        return
    
    generate_report(df, type, output)
    click.echo(f"[+] Report saved to {output}")

if __name__ == '__main__':
    main()
