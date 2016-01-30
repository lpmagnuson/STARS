import csv
word_list = 'Agriculture,Alternative,Applied%Science,Awareness%Raising,Balance,Behavior%Change,Biodiversity,Bioenergy,Biomass,Biomimicry,Brundtland%Commission,Building,Carbon%Offset,Catalyze,Change,Change%Management,City,Civil,Climate,Coastal,Collaboration,Commissioning,Community,Community%Health,Complex%Systems,Conserve,Conservation,Conservation%Biolog,Corporate%Social%Responsibility,Cost%Benefit%Analysis,Cradle%to%Cradle,Culture,Deforestation,Design,Development,Innovative,Integrated,Interconnections,Interdisciplinary,Invest,Justice,Land,Landscape,LEED%(Leadership%in%Energy%and%Environmental%Design),Systems,Life,Life%Cycle,Local,Marine,Materials,Minority,Modernization,Movements,Multidisciplinary,Natural%Systems%,Nature,Nutrition,Outreach,Partnership,Photovoltaic,Planning,Policy,Political,Population,Poverty,Problem%Based,Prosperity,Public,Public%Health,Race,Recycle,Recycling,Renewable,Resilience,Resources,Revolving%Fund,Rights,Rural,Sea%Level,Social,Solar,Disaster,Discrimination,Diversity,Ecological,Ecology,Economic,Ecosystem,Efficiency,Energy,Engaged%Scholarship,Engagement,Entrepreneurship,Environment,Externality,Equality,Equity,Farming,Finance,Food,Food%Systems,Food%Chain,Footprint,Future,Gender,Geothermal,Global,Globalization,Governance,Green,Greenhouse%Gas,Growth,Human%Condition,Human%Rights,Human-Environment%Interactions,Innovation,Solutions,Stakeholder,Stewardship,Suburbanization,Supply%Chain,Sustainable,Sustainability,Systems%Dynamics,Thinking,Technology,Three%Legged%Stool,Three%Pillars,Tradeoffs,Transdisciplinary,Transformation,Transit,Transparency,Transportation,Triple%Bottom%Line,Underserved,Unintended%Consequences,Urban,Urbanization,Water,Welfare,Wind%Energy,Women,agriculture,alternative,applied%science,awareness%raising,balance,behavior%change,biodiversity,bioenergy,biomass,biomimicry,brundtland%commission,building,carbon%offset,catalyze,change,change%management,city,civil,climate,coastal,collaboration,commissioning,community,community%health,complex%systems,conserve,conservation,conservation%biolog,corporate%social%responsibility,cost%benefit%analysis,cradle%to%cradle,culture,deforestation,design,development,innovative,integrated,interconnections,interdisciplinary,invest,justice,land,landscape,leed%(leadership%in%energy%and%environmental%design),systems,life,life%cycle,local,marine,materials,minority,modernization,movements,multidisciplinary,natural%systems%,nature,nutrition,outreach,partnership,photovoltaic,planning,policy,political,population,poverty,problem%based,prosperity,public,public%health,race,recycle,recycling,renewable,resilience,resources,revolving%fund,rights,rural,sea%level,social,solar,disaster,discrimination,diversity,ecological,ecology,economic,ecosystem,efficiency,energy,engaged%scholarship,engagement,entrepreneurship,environment,externality,equality,equity,farming,finance,food,food%systems,food%chain,footprint,future,gender,geothermal,global,globalization,governance,green,greenhouse%gas,growth,human%condition,human%rights,human-environment%interactions,innovation,solutions,stakeholder,stewardship,suburbanization,supply%chain,sustainable,sustainability,systems%dynamics,thinking,technology,three%legged%stool,three%pillars,tradeoffs,transdisciplinary,transformation,transit,transparency,transportation,triple%bottom%line,underserved,unintended%consequences,urban,urbanization,water,welfare,wind%energy,women'
word_set = set(word_list.split(','))
csv_out = csv.writer(open('research_output.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
with open ('combinedrecs.csv', 'rb') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    if (set(row[23].split()) & word_set) & (set(row[9].split()) & word_set) :
      csv_out.writerow(["title & abstract match",row[61],row[1],row[9],row[23],(set(row[9].split()) & word_set), (set(row[23].split()) & word_set)])
    elif set(row[9].split()) & word_set:
      csv_out.writerow(["title match",row[61],row[1],row[9],row[23], (set(row[9].split()) & word_set)])
    elif set(row[23].split()) & word_set:
      csv_out.writerow(["abstract match",row[61],row[1],row[9],row[23], (set(row[23].split()) & word_set)])
    