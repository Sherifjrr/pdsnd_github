import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print(' Hello! Let\'s explore some US bikeshare data!')

    while True : 
        city = input(' Which city do you want to explore : Chicago, New York City, Washington ').lower()
        if city in ('chicago', 'new york city', 'washington'):
            break 

    while True : 
        month = input(' In which month you want to explore? all, january, february, ... , june ')
        if month in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            break
        

    while True : 
        day = input(' Which day? all, monday, tuesday, ... sunday ').lower()
        if day in ('sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','all'):
            break 
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
                     
                     
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) 
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    print('The Most Common Month is : {}'.format(str(df['month'].mode().values[0])))


    print('The Most Common Day Of Week is : {}'.format(str(df['day_of_week'].mode().values[0])))


    df['Start Hour'] = df['Start Time'].dt.hour
    print('The Most Common Start Hour is : {}'.format(str(df['Start Hour'].mode().values[0])))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                
     
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    print('The Most Commonly Used Start Station is : {}'.format(df['Start Station'].mode().values[0]))


    print('The Most Commonly Used End Station is : {}'.format(df['End Station'].mode().values[0]))



    df['Both Sta'] = df['Start Station'] + " " + df['End Station']
    print('The Most Commonly Combination Of Start and End Staion is : {}'.format(df['Both Sta'].mode().values[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    

    print('Total Travel Time : {}'.format(str(df['Trip Duration'].sum())))
    


    print('Mean Of Travel Time : {}'.format(str(df['Trip Duration'].mean())))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
     
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    print('The Count Of User Types : {}'.format(str(df['User Type'].value_counts())))
    city = ('chicago', 'new york city', 'washington')
    if  city in  ['chicago', 'new york city']:   
          print('The Count Of Gender : {}'.format(str(df['Gender'].value_counts())))
          print('The Earliest Year Of Birth : {}'.format(str(df['Birth Year'].min())))
          print("\nThe Latest Year Of Birth : {}".format(str(df['Birth Year'].max())))
          print("\nThe Most Common Year Of Birth : {}".format(str(df['Birth Year'].mode().values[0])))    
    else :
        print('The Information Is Not Available')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    i=5

    while(i< df.shape[0]):
        check = input(' Do You Wish to Continue Showing Raw Data yes/no:   ').lower()
        if check == 'yes' :
            print(df.head(i))
            i+=5
        else :
            break

    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#Git project for udacity Program 2019
# refactoring the python codess of bikeshare
# refactoring the python code bike program

# refactoring the python code 2
# for refacoting in git project 1
