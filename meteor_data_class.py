class MeteorDataEntry:
    name = ''
    id = ''
    nametype = ''
    recclass = ''
    mass = ''
    fall = ''
    year = ''
    reclat = ''
    reclong = ''
    geolocation = ''
    state = ''
    counties = ''

    # 12 Data Fields: name	id	nametype	recclass	mass (g)	fall	year	reclat	reclong	GeoLocation	States	Counties
    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation, state, counties): # constructor
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.state = state
        self.counties = counties

    def get_data(self): # returns all the information about MeteorDataEntry objects
        return {
            'name': self.name,
            'id': self.id,
            'nametype': self.nametype,
            'recclass': self.recclass,
            'mass': self.mass,
            'fall': self.fall,
            'year': self.year,
            'reclat': self.reclat,
            'reclong': self.reclong,
            'geolocation': self.geolocation,
            'state': self.state,
            'counties': self.counties
        }
     
        
        

    