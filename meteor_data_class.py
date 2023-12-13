class MeteorDataEntry:
    '''
    This is the docstring for the MeteorDataEntry class
    This class is a MeteorDataEntry object that contains Meteorite data

    The information this object stores is:
        - name which is the name of a meteorite

        - id which is the id of a meteorite

        - nametype which is the nametype of a meteorite

        - recclass which is the recclass of a meteorite

        - mass which is the mass of a meteorite

        - fall which is the fall of a meteorite

        - year which is the year corresponding to the meteorite

        - reclat which is the reclat for the meteorite

        - reclong which is the reclong for the meteorite

        - geolocation which is the geolocation of the meteorite

        - state which is the state for the meteorite

        - counties which is the counties for the meteorite
    '''
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
        '''
        This is the docstring for the __init__ function
        This function is the __init__ function for the MeteorDataEntry object

        Parameters:
            - name which is the name of a meteorite

            - id which is the id of a meteorite

            - nametype which is the nametype of a meteorite

            - recclass which is the recclass of a meteorite

            - mass which is the mass of a meteorite

            - fall which is the fall of a meteorite

            - year which is the year corresponding to the meteorite

            - reclat which is the reclat for the meteorite

            - reclong which is the reclong for the meteorite

            - geolocation which is the geolocation of the meteorite

            - state which is the state for the meteorite

            - counties which is the counties for the meteorite
        '''
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
        '''
        This function returns all the information in a MeteorDataEntry object

        Parameters:
            - self

        Returns:
            - returns all the information in a MeteorDataEntry object
        '''
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
     
        
        

    