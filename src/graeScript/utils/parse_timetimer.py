from pathlib import Path
from typing import List, Tuple

import pandas as pd
from pandas.core.frame import DataFrame


def separate_data(
        dataframe: DataFrame, column: str, match_values: List[str]
        ) -> DataFrame:
    """Returns a DataFrame containing only rows where column = match_value"""
    return dataframe[dataframe[column].isin(match_values)]


def for_ssa_45(
        file: Path, date_cols: List[str]
        ) -> Tuple[DataFrame, DataFrame, DataFrame]:
    """Create DataFrames for specific use-case: Programming Totals"""
    # Create DataFrame object from file,parsing datetimes
    print('Generating total times spent on computer-related learning...')
    df = pd.read_csv(file, parse_dates=date_cols, )

    # Convert Duration column to timedelta
    df['Duration'] = pd.to_timedelta(df['Duration'])

    # Convert text columns to strings
    df['Group'] = df['Group'].astype('string')
    df['Activity type'] = df['Activity type'].astype('string')
    df['Comment'] = df['Comment'].astype('string')

    # DataFrame without the columns "Group".
    no_category = df[['Activity type', 'Comment', 'Duration', 'From', 'To']]
    # DataFrame only with "Activity Type" of Learn
    Activity_Learn = no_category[no_category['Activity type'] == 'Learn']

    # Lists used to create DataFrames based on values in "Comment" column.
    coding = ['Dragon', 'Dragon Script', 'VBA', 'Python', 'Python Install',
              'Sqlite', 'Dragon & Python', 'Python & Sqlite', 'VS Code',
              'JavaScript', 'Git', 'HTML', 'NAS']
    other = ['Excel', 'Keyboard Shortcuts', 'Windows Narrator']
    together = coding.copy()
    for i in other:
        together.append(i)

    # Create DataFrames based on the Comment column.
    coding_df = separate_data(Activity_Learn, 'Comment', coding)
    other_df = separate_data(Activity_Learn, 'Comment', other)
    both_df = separate_data(Activity_Learn, 'Comment', together)

    # coding_df - Create new DataFrames containing the Duration by Date.
    coding_simplified = pd.DataFrame(coding_df[['To', 'Duration']])
    coding_simplified['Date'] = coding_simplified['To'].dt.date
    cs = coding_simplified[['Date', 'Duration']]
    cs = cs.groupby(['Date']).sum()
    cs.Name = 'Coding'

    # other_df - Create new DataFrames containing the Duration by Date.
    other_simplified = pd.DataFrame(other_df[['To', 'Duration']])
    other_simplified['Date'] = other_simplified['To'].dt.date
    ots = other_simplified[['Date', 'Duration']]
    ots = ots.groupby(['Date']).sum()
    ots.Name = 'Other'

    # both_df - Create new DataFrames containing the Duration by Date.
    both_simplified = pd.DataFrame(both_df[['To', 'Duration']])
    both_simplified['Date'] = both_simplified['To'].dt.date
    bs = both_simplified[['Date', 'Duration']]
    bs = bs.groupby(['Date']).sum()
    bs.Name = 'Both'
    return cs, ots, bs


# Functions to simplify returning data for multiple Dataframes.
def get_totals(dataframe: DataFrame) -> None:
    print(f'{dataframe.Name} Total Duration:')
    print('\t', dataframe['Duration'].sum())


def get_start(dataframe: DataFrame) -> None:
    print(f'{dataframe.Name} Start Dates:')
    print('\t', dataframe.index.min())


def get_last_date(dataframe: DataFrame) -> None:
    print(f'{dataframe.Name} Most Recent Date:')
    print('\t', dataframe.index.max())


def get_mean(dataframe: DataFrame) -> None:
    print(f'{dataframe.Name} Mean Duration:')
    print('\t', dataframe['Duration'].mean())


def get_median(dataframe: DataFrame) -> None:
    print(f'{dataframe.Name} Median Duration:')
    print('\t', dataframe['Duration'].median())


if __name__ == "__main__":
    timetimer_path = Path("")
    file = timetimer_path / '2019-11-12 - 2021-11-07 - report.csv'
    dataframes = for_ssa_45(file, ['From', 'To'])
    for item in dataframes:
        print('rows=', item.size)
        get_start(item)
        get_last_date(item)
        get_totals(item)
        get_mean(item)
        get_median(item)
        print()
