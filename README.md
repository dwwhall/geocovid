# geocovid
PostGIS, Django, and PostgreSQL were used in the development of this database.  



Geocovid displays the Confirmed cases of Covid-19 on a geographical map.

The developer is currently looking into Coronavirus Monitor API which would supply updated Confirmed, Deaths, and Recovered cases by country.

The sequences and variation of sequences were not added.  Nextstrain (nextstrain.org) can be used to find a overlapping visual representation of sequence mutation by country.

The sequence search leads to a page for sequencing technology, country, and sequence ID for complet gene regions of COVID-19 found on National Center for Biotechnology Information(NCBI). 

The developer set out to have a Multiple Sequence Aligner as a function of the website, yet the implentation did not occur.  Please refer to NCBI virus for multiple sequence alignments (https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome%20coronavirus%202%20(SARS-CoV-2),%20taxid:2697049&Completeness_s=complete).

The publicaitons search leads to a page, which includes 8,000+ publications relating to COVID-19.  The publications data was extracted from the World Health Organization (WHO).

The curves were generated by Novel Coronavirus 2019 Datahub.io https://datahub.io/core/covid-19.  Data provided by John Hopkins University Center for Systems Science and Engineering (CSSE).  This database embedded the datahub curves and graphs - - total number of confirmed cases and deaths
- cofirmed cases for countries: China, US, UK, Italy, France, Germany, Spain, and Iran
- mortality rate in percentage
- Increase rate by day

The total number of confirmed cases and deaths is a timeline from January to May 2020 displaying the total number of COVID-19 confrimed and deaths across the globe.  The curve indicates that the numbers are continuing to rise.  

The cofirmed cases for countries: China, US, UK, Italy, France, Germany, Spain, and Iran is a timeline from January to May 2020 displaying the total number of COVID-19 confrimed cases across each country.  The curve indicates that the numbers are continuing to rise. 

Mortality rate in percenatage displays the total mortaility rate for global deaths on a timeline from January to May 2020.   

The increase rate is a timeline that is based on the increase rate of confirmed cases from the previous day.







#References:

The interactive graphs are currently provided by Data Hub.
Geographical map developed by Dwight Hall, IUPUI Bioinformatics student. 

Search functions developed by Vivek Matcha, IUPUI Health informatics student.

The Real Python course 'Make a Location-Based Web app with Django and GeoDjango' taught by Jackie Wilson was used as a template to help get the postgis map and leaflet set up on Django. 

Data Hub. https://datahub.io/core/covid-19#python

