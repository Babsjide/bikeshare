import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }


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
    valid_option1 = False
    while valid_option1 == False:
        
        city = input('Which city would you like to investigate? \n1. Chicago (c) \n2. NewYork (n) \n3. Washington (w) \n>>> ').lower()
        
        if city == 'c' or city == 'n' or city == 'w':
            valid_option1 = True
            break
        else:
            print('\nPlease select a valid option\n')
            
    
  
    valid_option2 = False
    while valid_option2 == False:
        
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('\nWhich month would you like to investigate? \nAll months (a), January (jan), February (feb), Match (mar), April (apr), May (m), June (j)  \n>>>  ').lower()
        if month == 'a' or month == 'jan' or month == 'feb' or month == 'mar' or month == 'apr' or month == 'm' or month == 'j':
            valid_option2 = True
            break
            
        else:
            print('Please enter a valid input\n')
            
    valid_option3 = False
    while valid_option3 == False:
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nWhich day would you like to investigate? All (a) \nMonday (mon) \nTuesday (tue) \nWednesday      (wed)\nThursday(th) \nFriday (fri) \nSaturday (sat) \nSunday (sun) \n>>>  ').lower()
        if day == 'a' or day == 'mon' or day == 'tue' or day == 'wed' or day == 'th' or day == 'fri' or day == 'sat' or day == 'sun':
            valid_option3 = True
            break
        else:
            print('\nPlease select a valid option.\n')
            

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
    
    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
      
    # Convert Start Time column to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
       
    # Extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    
     # filter by month if applicable
    if month != 'a':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'm', 'j']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']== month]
  

    # filter by day of week if applicable
    if day != 'a':
        # filter by day of week to create the new dataframe
        days = ['mon', 'tue', 'wed', 'th', 'fri', 'sat', 'sun']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
   
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nThe most common month is {}.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of week is {}.'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\nThe most common start hour is {}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\n{} is the most commonly used start station.'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\n{} is the most commonly used end station.'.format(popular_end_station))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum().sum()
    print('\nThe total travel time is {}.'.format(travel_time))

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('\nThe average travel time is {}.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].count()
    print('User types: {}'.format(user_type))

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_count = df['Gender'].count()
        print('Gender count: {}'.format(gender_count))
   

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_b_y = np.min(df['Birth Year'])
        recent_b_y = np.max(df['Birth Year'])
        common_b_y = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is {}, the most recent birth year is {} \nand the most common birth year is {}.'.format(earliest_b_y, recent_b_y, common_b_y))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    row = 0
    while True:
        view_raw_data = input('\n Do you want to view 5 lines of output at a time?.\n1. Yes \n2. No\n3. Show all.(Warning!!! This is a large data collection.)\n>>> ')
        if view_raw_data.lower() == 'yes':
            
            print(tabulate(df.iloc[np.arange(0+row, row + 5)], headers = "keys"))
            row += 5
        elif view_raw_data.lower() == 'no':
            break

            
        else:
            print(tabulate(df, headers= "keys"))
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
