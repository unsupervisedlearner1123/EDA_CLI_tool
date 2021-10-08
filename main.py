import click
import pandas as pd

pd.set_option("display.max_rows",15, "display.max_columns",50)
pd.options.display.float_format = "{:.2f}".format

@click.command()
@click.option('--fileurl', prompt = "Enter the URL to any .csv dataset", help = "The URL of the dataset you want to check out")
@click.option('--check_missing', type=bool, default=False)
@click.option('--check_dups', type=bool, default=False)
def main(fileurl,check_missing,check_dups):
    df = pd.read_csv(fileurl)
    
    click.echo("\n")
    click.echo("This is a summary of all the variables and their types present in the dataset provided.")
    click.echo(df.info())
    
    click.echo("These are the summary statistics for the numerical variables in the dataset provided.")
    click.echo(df.describe(include="all"))
    
    if check_missing:
        click.echo("\n")
        click.echo("These are the proportion of nulls per column of the dataset provided.")
        click.echo((df.isnull().sum()/len(df)).apply(lambda x:'{:.2%}'.format(x)))
        
    if check_dups:
        click.echo("\n")
        click.echo("Count of duplicate rows found:")
        click.echo(df[df.duplicated()].shape[0])

if __name__=="__main__":
    main()