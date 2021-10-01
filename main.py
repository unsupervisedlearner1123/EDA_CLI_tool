import click
import pandas as pd

pd.set_option("display.max_rows",10, "display.max_columns",20)
pd.options.display.float_format = "{:.2f}".format

@click.command()
@click.option('--fileurl', prompt = "Enter the URL to any csv dataset", help = "The URL of the dataset you want to check out")
def main(fileurl):
    df = pd.read_csv(fileurl)
    click.echo(df.describe())

if __name__=="__main__":
    main()