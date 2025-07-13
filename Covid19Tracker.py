import requests  # This lets us talk to websites and get data from them.

# A function to fetch and show COVID-19 stats for a given country
def show_covid_stats(country_name):
    api_url = f"https://disease.sh/v3/covid-19/countries/{country_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        covid_data = response.json()
        print(f"\n📍 COVID-19 Stats for {covid_data['country']}:")
        print(f"🦠 Total Cases     : {covid_data['cases']}")
        print(f"📈 New Cases Today: {covid_data['todayCases']}")
        print(f"💀 Total Deaths    : {covid_data['deaths']}")
        print(f"⚠️ Deaths Today    : {covid_data['todayDeaths']}")
        print(f"💚 Recovered       : {covid_data['recovered']}")
        print(f"🟡 Currently Sick  : {covid_data['active']}")
    else:
        print("❌ Sorry, I couldn't find data for that country. Please check the name and try again.")

# Ask the user which country they want to check
user_country = input("🌍 Enter the country name to check COVID-19 stats: ")
show_covid_stats(user_country)
