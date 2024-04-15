'''
    Author: PhongNVA
    Project: Explore US Bikeshare Data
    Date: 15-04-2024
'''

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =input("Please enter cities:\n").lower()
        if city in cities:
            break
        else:
            print('Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input('Please enter the month. If not, type in all\n')).title()
        if month not in months:
            print('Invalid month, Please try again.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Please enter the day. If not, type in all\n')).title()
        if day not in days:
            print('Invalid day, Please try again.')
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day to new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'All':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df ['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    mc_start_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(mc_start_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours: ", total_duration)

    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time in hours: ", avg_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('Sorry! Gender data unavailable for Washington')
    else:
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' not in df):
        print('Sorry! Birth Year data unavailable for Washington')
    else:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print(' ' * 40)
        print('Oldest User(s) Birth Year: ', earliest)
        print('Youngest User(s) Birth Year: ', most_recent)
        print('Most Common Birth Year: ', most_common)        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    start=0
    choice=input('\nDo you want to view the data? Enter yes or no.\n').lower()
    while choice=='yes':
        try:
            n=int(input('Enter the number of rows to view\n'))
            n=start+n
            print(df[start:n])
            choice=input('More rows? Enter yes or no.\n').lower()
            start=n

        except ValueError:
            print('Enter appropriate integer value')
    print('-'*40)       
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()