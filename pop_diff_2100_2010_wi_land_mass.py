#  Peter Stephens
# 5/8/2016

from collections import defaultdict
import operator 
population_dict_2010 = defaultdict(int)
population_dict_2100 = defaultdict(int)
population_dict_diff = defaultdict(int)
population_dict_land_mass = defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','r') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            population_dict_2010[line[0]] += line[5]
            population_dict_2100[line[0]] += line[6]
            population_dict_diff[line[0]] = population_dict_2100[line[0]] - population_dict_2010[line[0]]
            population_dict_land_mass[line[0]] = population_dict_2010[line[0]] / float(line[7])

# OUTPUT     
with open('continent_population_differences.csv','w') as outputFile:
    outputFile.write('continent,population_difference_2010_to_2100\n')
    population_dict_diff = sorted(population_dict_diff.items(), key=operator.itemgetter(1), reverse=True)
    for item in population_dict_diff:
        outputFile.write(str(item[0]) + ',' + str(item[1]) + '\n')
    
    max_pop = population_dict_diff[0]
    print('\nThe largest change in population belongs to: ' + str(max_pop[0]) + ' with a population change of: ' + str(max_pop[1]))

with open('continent_land_mass.csv','w') as outputFile:    
    outputFile.write('continent,land_mass\n')
    population_dict_land_mass = sorted(population_dict_land_mass.items(), key=operator.itemgetter(1), reverse=True)
    for item in population_dict_land_mass:
        outputFile.write(str(item[0]) + ',' + str(item[1]) + '\n')
    
    max_land_mass = population_dict_land_mass[0]
    print('\nThe largest population density in 2010 belongs to: ' + str(max_land_mass[0]) + ' with a land mass of: ' + str(max_land_mass[1]))
