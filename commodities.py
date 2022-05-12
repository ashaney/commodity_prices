import pandas as pd
import altair as alt
import datapane as dp
import os

md = """

---

### Description of Categories
#### Energy

  - Coal (Australia), from January 2015, port thermal, fo.b. Newcastle, 6000 kcal/kg spot price. 2002-2014, thermal GAR, f.o.b. piers, Newcastle/Port Kembla , 6,300 kcal/kg (11,340 btu/lb), less than 0.8%, sulfur 13% ash; previously 6,667 kcal/kg (12,000 btu/lb), less than 1.0% sulfur, 14%  ash
  - Coal (Colombia), thermal GAR, f.o.b. Bolivar,  6,450 kcal/kg, (11,200 btu/lb), less than 1.0%, sulfur 16% ash from August 2005 onwards; during years 2002-July 2005 11,600 btu/lb, less than .8% sulfur, 9% ash , 180 days forward delivery
  - Coal (South Africa), from January 2015, f.o.b. Richards Bay, NAR, 6,000 kcal/kg, sulfur less than 1%, forward month 1;  from February 13, 2017 to December 2017, thermal NAR netback assessment f.o.b. Richards Bay 6,000 kcal/kg; during 2006-February 10, 2017 thermal NAR; during 2002-2005 6,200 kcal/kg (11,200 btu/lb), less than 1.0%, sulfur 16% ash; years 1990-2001 6390 kcal/kg (11,500 btu/lb)
  - Crude oil, average spot price of Brent, Dubai and West Texas  Intermediate, equally weighed
  - Crude oil, UK Brent 38
  - Crude oil, Dubai Fateh 32
  - Crude oil, US, West Texas Intermediate (WTI)
  - Natural gas index (Laspeyres), average of Europe, US and Japan (LNG), weights based on 5-year average consumption volumes, updated every 5 years, except the 11-year period 1960-70.
  - Natural Gas (Europe), from April 2015, Netherlands Title Transfer Facility (TTF); April 2010 to March 2015, average import border price and a spot price component, including UK; during June 2000 - March 2010 prices excludes UK.
  - Natural Gas (U.S.), spot price at Henry Hub, Louisiana
  - Liquefied natural gas (Japan), LNG, import price, cif; recent two months' averages are estimates.

#### Agriculture
- Beverages
- Food
- Raw Materials

#### Beverages
- Cocoa (ICCO), International Cocoa Organization daily price, average of  the first three positions on the terminal markets of New York and London, nearest three future trading months.
- Coffee (ICO), International Coffee Organization indicator price, other mild Arabicas, average New York and Bremen/Hamburg markets, ex-dock
- Coffee (ICO), International Coffee Organization indicator price, Robustas, average New York and Le Havre/Marseilles markets, ex-dock
- Tea , average three auctions, arithmetic average of quotations at Kolkata, Colombo and Mombasa/Nairobi.
- Tea (Colombo auctions), Sri Lankan origin, all tea, arithmetic average of weekly quotes.
- Tea (Kolkata auctions), leaf, include excise duty, arithmetic average of weekly quotes.
- Tea (Mombasa/Nairobi auctions), African origin, all tea, arithmetic average of weekly quotes.

#### Food
- Oils and Meals
- Grains
- Other 

#### Oils and Meals
- Coconut oil (Philippines/Indonesia), from January 2021, crude, CIF Rotterdam; January 1999 to December 2020, crude, CIF NW Europe; previously, bulk, c.i.f. Rotterdam Copra (Philippines/Indonesia), bulk, c.i.f. N.W. Europe
- Fishmeal, from January 2021, German Fishmeal, Danish 64% Pro, FOB Bremen; January 1999 to December 2020, German, 64% protein, EXW Hamburg
- Groundnuts (U.S.), Runners 40/50, CFR N.W. Europe. Europe beginning January 1999; previously (US), Runners 40/50 shelled basis, c.i.f. Rotterdam
- Groundnut oil, Dutch Refined GroundNut Oil A/O, Ex Tank Rotterdam, beginning December 2020; January 1999-November 2020, U.S. crude, FOB South-East; previously any origin, c.i.f. Rotterdam.
- Palm oil (Malaysia), from January 2021, RBD, FOB Malaysia Ports; December 2001 to December 2020, RBD, CIF Rotterdam; previously Malaysia 5%,  c.i.f. N.W. Europe, bulk, nearest forward .
- Palmkernel oil (Malaysia/Indonesia), from January 2021, crude CIF Rotterdam; August 2001 to December 2020, crude, CIF NW Europe; previously Malaysian, nearest forward.
- Soybean meal, from January 2021, Soybean Pellets 48% Pro, Brazil, CIF Rotterdam; January 1999 to December 2020, Brazilian pellets 48% protein, CIF Rotterdam; during 1990 - 1998, 45/46% c.i.f. Rotterdam, nearest forward; previously US origin 44%.
- Soybean oil, from January 2021, Dutch Soyoil Crude Degummed, EXW Dutch Mills; January 1999 to December 2020, Dutch crude degummed, FOB NW Europe; previously crude, f.o.b. ex-mill Netherlands, nearest forward.
- Soybeans, from January 2021, U.S Gulf Yellow Soybean #2, CIF Rotterdam; December 2007 to December 2020, U.S. No. 2 yellow meal, CIF Rotterdam; previously US origin, nearest forward.
- Sunflower oil, from September 2020, Dutch Sunseed Oil, f.o.b. Rotterdam; February 2011 to August 2020, European crude, f.o.b. Rotterdam; previously, EU f.o.b NW Europe ports.

#### Grains
- Barley (U.S.) feed, No. 2, spot, 20 days To-Arrive, delivered Minneapolis from May 2012 onwards; during 1980 - 2012 April Canadian, feed, Western No. 1, Winnipeg Commodity Exchange, spot, wholesale farmers' price
- Maize (U.S.), no. 2, yellow, f.o.b. US Gulf ports
- Rice (Thailand), 5% broken, white rice (WR), milled, indicative price based on  weekly surveys of export transactions, government standard, f.o.b. Bangkok
- Rice (Thailand), 25% broken, WR, milled indicative survey price, government standard, f.o.b. Bangkok
- Rice (Thailand), 100% broken, A.1 Super from 2006 onwards, government standard, f.o.b. Bangkok; prior to 2006, A1 Special, a slightly lower grade than A1 Super.
- Rice (Vietnam), 5% broken, WR, milled, weekly indicative survey price, Minimum Export Price, f.o.b. Hanoi
- Sorghum (US), no. 2 milo yellow, Texas export bids for grain delivered to export elevators, rail-truck, f.o.b. Gulf ports
- Wheat (Canada), no. 1, Western Red Spring (CWRS), in store, St. Lawrence, export price
- Wheat (U.S.), no. 2 hard red winter Gulf export price; June 2020 backwards, no. 1, hard red winter, ordinary protein, export price delivered at the US Gulf port for prompt or 30 days shipment
- Wheat (U.S.), no. 2, soft red winter, export price delivered at the US Gulf port for prompt or 30 days shipment

#### Other Food
- Bananas (Central & South America), major brands, free on truck (f.o.t.) Southern Europe, including duties; prior to October 2006, f.o.t. Hamburg. 
- Bananas (Central & South America), major brands, US import price, free on truck (f.o.t.) US Gulf ports. 
- Meat, beef (Australia/New Zealand), mixed trimmings 85%, East Coast, 7-45 day deferred delivery, FOB port of entry, beginning January 1995; previously cow forequarters
- Meat, chicken (US), Urner Barry North East weighted average for broiler/fryer, whole birds, 2.5 to 3.5 pounds, USDA grade "A" from 2013 onwards; 1980-2012, Georgia Dock weighted average, 2.5 to 3 pounds,wholesale; previously World Bank estimates.
- Meat, sheep (New Zealand), frozen whole carcasses Prime Medium (PM) wholesale, Smithfield, London  beginning January 2006; previously Prime Light (PL)
- Oranges (Mediterranean exporters) navel, European Union indicative import price, c.i.f. Paris
- Shrimp , (U.S.), brown, shell-on, headless, in frozen blocks, source Gulf of Mexico, 26 to 30 count per pound, wholesale US beginning 2004; previously New York.
- Sugar (EU), European Union negotiated import price for raw unpackaged sugar from African, Caribbean and Pacific (ACP) under Lome Conventions, c.I.f. European ports
- Sugar (U.S.), nearby futures contract, c.i.f. 
- Sugar (World), International Sugar Agreement (ISA) daily price, raw,  f.o.b. and stowed at greater Caribbean ports

#### Raw Materials
- Timber
- Other

#### Timber
- Logs (Africa), sapele, high quality (loyal and marchand), 80 centimeter or more, f.o.b. Douala, Cameroon beginning January 1996; previously of unspecified dimension
- Logs (Southeast Asia), meranti, Sarawak, sale price charged by importers, Tokyo beginning February 1993; previously average of Sabah and Sarawak weighted by Japanese import volumes
- Plywood (Africa and Southeast Asia), Lauan, 3-ply, extra, 91 cm x 182 cm x 4 mm,  wholesale price, spot Tokyo
- Sawnwood (Africa), sapele, width 6 inches or more, length 6 feet or more, f.a.s. Cameroonian ports
- Sawnwood (Southeast Asia), dark red seraya/meranti, select and better quality, average 7 to 8 inches; length average 12 to 14 inches; thickness 1 to 2 inch(es);  kiln dry, c. & f. UK ports, with 5% agents commission including premium for products of certified sustainable forest beginning January 2005; previously excluding the premium
- Woodpulp (Sweden), softwood, sulphate, bleached, air-dry weight, c.i.f.  North Sea ports

#### Other Raw Materials
- Cotton (Cotton Outlook "CotlookA index"), middling 1-3/32 inch, traded in Far East, C/F beginning 2006; previously Northern Europe, c.i.f.
- Cotton (US), Memphis/Eastern, middling 1-3/32 inch, Far East , C/F beginning October 2008; previously c.i.f. Northern Europe
- Rubber (Asia), RSS3 grade, Singapore Commodity Exchange Ltd (SICOM) nearby contract beginning 2004; during 2000 to 2003, Singapore RSS1; previously Malaysia RSS1
- Rubber (any origin), Ribbed Smoked Sheet (RSS) no. 1, in bales, Rubber Traders Association (RTA), spot, New York
- Rubber (Asia), TSR 20, Technically Specified Rubber, SGX/SICOM nearby futures contract
- Tobacco (any origin), unmanufactured, general import , cif, US

#### Fertilizers
- DAP (diammonium phosphate), spot, f.o.b. US Gulf
- Phosphate rock , f.o.b. North Africa
- Potassium chloride (muriate of potash), f.o.b. Vancouver
- TSP (triple superphosphate), spot, import US Gulf
- Urea, (Ukraine), prill spot f.o.b. Middle East, beginning March 2022; previously, f.o.b. Black Sea.

#### Metals and Minerals
- Base Metals
- Precious Metals

#### Base Metals (excluding Iron Ore)
- Aluminum (LME) London Metal Exchange, unalloyed primary ingots, high grade, minimum 99.7% purity, settlement price beginning 2005; previously cash price
- Copper (LME), grade A, minimum 99.9935% purity, cathodes and wire bar shapes, settlement price
- Lead (LME), refined, 99.97% purity, settlement price
- Nickel (LME), cathodes, minimum 99.8% purity, settlement price beginning 2005; previously cash price
- Steel products index
- Steel, Cold-rolled coil/sheet (Japan) producers' export contracts (3 to 12 months terms) fob mainly to Asia
- Steel, Hot-rolled coil/sheet (Japan) producers' export contracts (3 to 12 months terms) fob mainly to Asia
- Steel, Rebar (concrete Reinforcing bars) (Japan) producers' export contracts (3 to 12 months terms) fob mainly to Asia
- Steel, Wire ord (Japan) producers' export contracts (3 to 12 months terms) fob mainly to Asia
- Tin (LME), refined, 99.85% purity, settlement price
- Zinc (LME), high grade, minimum 99.95% purity, settlement price beginning April 1990; previously special high grade, minimum 99.995%, cash prices 

#### Precious Metals
- Gold (UK), 99.5% fine, London afternoon fixing, average of daily rates
- Platinum (UK), 99.9% refined, London afternoon fixing
- Silver (UK), 99.9% refined, London afternoon fixing; prior to July 1976 Handy & Harman.  Grade prior to 1962 unrefined silver.
"""

alt.data_transformers.disable_max_rows()

path = os.getcwd()
df = pd.read_csv(path+'all_prices.csv')
df['Date'] = pd.to_datetime(df['Date'])
commodity_list = list(df['Commodity'].unique())

input_dropdown = alt.binding_select(options=commodity_list, name="Commodity ")
selection = alt.selection_single(name='Commodity', fields=['Commodity'], bind=input_dropdown)

alt_plot = alt.Chart(df).mark_line().encode(
    x='Date',
    y='Price'
).add_selection(
    selection
).transform_filter(
    selection
)

report = dp.Report(
    "## Commodity Prices",
    dp.Plot(alt_plot, name="Chart", caption="Commodity prices over time"),
    dp.Text(md)
  )

report.upload(name="Commodity Prices", open=True, description = "Commodity Price Data from World Bank")