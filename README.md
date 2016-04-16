# ACA Marketplace

This repo containes scripts for cleaning and formatting the crosswalk files in prep for Bayeshack 

- ACA marketplace <a href="https://www.cms.gov/CCIIO/Resources/Data-Resources/Downloads/PlanCrosswalk_DataDictionary_2016.pdf">2014-2015 Crosswalk file dictionary</a>
- ACA marketplace <a href="https://www.cms.gov/CCIIO/Resources/Data-Resources/Downloads/2014-Plan-Crosswalk-Data-Dictionary.pdf">2015-2016 Crosswalk file dictionary</a>

The scripts read the raw crosswalk files for 2014-2015 and 2015-2016 and recode missing values as "NA".  The output consists of three files:

- "all" file contains all records with missing values clearly and uniformly indicated
- "all_formatted" file has the contents of the "all" file with variable values recoded to more intuttive names
- "formatted_qhp" file is the subset of the "all_formatted" records with the exception of plans that only provide dental insurance

