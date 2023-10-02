import pandas as pd

site_list = pd.read_excel("./SiteList.xlsx")
results = pd.read_excel("./Results.xlsx")

#* Filter datas 2023 sites only
site_list = site_list[site_list["Year"] == 2023]
results = results[results["Year"] == 2023]
# Create the new "Site Name" column from the individual columns
results['Site Name'] = results.apply(lambda row: f"{row['Year']}{row['Site ID']}-{row['City']}{row['State']}", axis=1)

# Saving new datas after filter
site_list.to_excel("./Solution/Reports/SiteList.xlsx", index=False)
results.to_excel("./Solution/Reports/Results.xlsx", index=False)

# Building a report, in format excel
new_columns = ['Site Name', 'Site ID', 'State', 'Equipment', 'Signal (%)', 'Quality (0-10)', 'Mbps']
report_of_quality = results[new_columns]

# Order by 'state'
report_of_quality.sort_values(by='State')

# Rename any columns to respect format data requested
report_of_quality = report_of_quality.rename(columns={'Site Name': 'Site', 'State': 'Estado', 'Equipment':'Equipamento'})

# Saving report of quality
report_of_quality.to_excel('./Solution/Reports/Relatório_Final.xlsx', index=False)

#* Second step of question, printing datas in console
# Getting archive provided evaluator
results = pd.read_excel("./Results.xlsx")
# Remaking the "Site Name" column from the individual columns
results['Site Name'] = results.apply(lambda row: f"2023{row['Site ID']}-{row['City']}{row['State']}", axis=1)

print("\nSites with active alerts:")
alert_sites = results[results['Alerts'] == 'Yes']['Site Name']
for alert in alert_sites:
  print(alert)

print("\n------------------------------------")
print("Sites with a quality score of 0:")
quality_zero_sites = results[results['Quality (0-10)'] == 0]['Site Name']
for speed in quality_zero_sites:
  print(speed)

print("\n------------------------------------")
print("Sites with more than 80 Mbps:")
high_speed_sites = results[results['Mbps'] > 80]['Site Name']
for speed in high_speed_sites:
  print(speed)

print("\n------------------------------------")
print("Sites with less than 10 Mbps:")
low_speed_sites = list(results[results['Mbps'] < 10]['Site Name'])
for speed in low_speed_sites:
  print(speed)

print("\n------------------------------------")
print("Sites that are not present in Site List:")
sites_in_site_list = set(site_list['Site Name'])
sites_in_results = set(results['Site Name'])
sites_not_in_site_list = sites_in_results - sites_in_site_list

for site in sites_not_in_site_list:
  print(site)
