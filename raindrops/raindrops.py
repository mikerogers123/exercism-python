from functools import reduce

def convert(number):
    returnVal = reduce(
        aggregateSounds(number),
        factorToRaindropSoundMap.keys(),
        ''
    )

    return f'{number}' if returnVal is '' else returnVal

def aggregateSounds(number):
    return (lambda agg, factor: agg + getSound(number, factor))

def getSound(number, factor): 
    return factorToRaindropSoundMap[factor] if number % factor == 0 else ''

factorToRaindropSoundMap = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}   
