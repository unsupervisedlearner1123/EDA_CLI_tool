#!/ec2-user/.venv/bin/python3

import click
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",15, "display.max_columns",50)
pd.options.display.float_format = "{:.2f}".format

@click.command(help = "This is a helper tool to perform exploratory data analysis on a .csv dataset.")
@click.option('--fileurl', prompt = "Enter the URL to any .csv dataset", help = "Input the URL of the dataset you want to check out")
@click.option('--check_missing', type=bool, default=False, help = "Returns the proportion of nulls for every column in the dataframe")
@click.option('--check_dups', type=bool, default=False, help = "Checks if there are duplicate rows in the dataframe")

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
        pass
        
    if check_dups:
        click.echo("\n")
        click.echo("Count of duplicate rows found:")
        click.echo(df[df.duplicated()].shape[0])
        pass
    
    list_num = df.select_dtypes(include='number').columns.tolist()
    
    sns.color_palette("deep")
    for col in list_num:
        sns.kdeplot(data=df, x=col,label = col)
        pass
    
    plt.legend(prop={'size': 6})
    plt.title('Density Plot with Numerical Attributes')
    plt.ylabel('Density')
    
    plt.savefig('display.svg')

if __name__=="__main__":
    main()