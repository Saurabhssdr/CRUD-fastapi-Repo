from models.location import Location

from repository import location_repo
 
async def create_location(location: Location):

    return await location_repo.create(location)
 
async def get_locations(country: str = None):

    return await location_repo.get_all(country)
 
async def update_location(country: str, city_id: str, location: Location):

    return await location_repo.update(country, city_id, location)
 
async def delete_location(country: str, city_id: str):

    return await location_repo.delete(country, city_id)

 