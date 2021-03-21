from dataclasses import dataclass

@dataclass
class Truck():
    objectid: float
    applicant: str
    facilitytype: str
    cnn: str
    locationdescription: str
    address: str
    blocklot: str
    block: str
    lot: str
    permit: str
    status: str
    fooditems: str
    x: float
    y: float
    latitude: float
    longitude: float
    schedule: str
    dayshours: str
    noisent: str
    approved: str
    received: float
    priorpermit: str
    expirationdate: str
    location: str
    computed_region_yftq_j783: float
    computed_region_p5aj_wyqh: float
    computed_region_rxqg_mtj9: float
    computed_region_bh8s_q3mv: float
    computed_region_fyvs_ahh9: float
    
    def to_json(self):
        return self.__dict__
    
truck_schema = {
    'objectid': 'objectid',
    'applicant': 'applicant',
    'facilitytype': 'facilitytype',
    'cnn': 'cnn',
    'locationdescription':'locationdescription',
    'address':'address',
    'blocklot': 'blocklot',
    'block':'block',
    'lot':'lot',
    'permit':'permit',
    'status':'status',
    'fooditems':'fooditems',
    'x':'x',
    'y':'y',
    'latitude':'latitude',
    'longitude':'longitude',
    'schedule':'schedule',
    'dayshours':'dayshours',
    'noisent':'noisent',
    'approved':'approved',
    'received':'received',
    'priorpermit':'priorpermit',
    'expirationdate':'expirationdate',
    'location':'location',
    ':@computed_region_yftq_j783':'computed_region_yftq_j783',
    ':@computed_region_p5aj_wyqh':'computed_region_p5aj_wyqh',
    ':@computed_region_rxqg_mtj9':'computed_region_rxqg_mtj9',
    ':@computed_region_bh8s_q3mv':'computed_region_bh8s_q3mv',
    ':@computed_region_fyvs_ahh9':'computed_region_fyvs_ahh9'
}
