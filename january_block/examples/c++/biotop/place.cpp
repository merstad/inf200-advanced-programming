#include "place.h"

/* Destructor for Place: All animals in the animal list 
   must be delete explicitly before the list of pointers
   to the animals is deleted with the Place object.
 */

Place::~Place()
{
  for ( auto animal : animals_ )
    delete animal;   // animal is a pointer to an animal
}

// -------------------------------------------

// Default place()
bool Place::place(Animal *new_animal)
{
  animals_.push_back(new_animal);
  return true;
}

// Override for House: no animals accepted
bool House::place(Animal *)
{
  return false;
}

// -------------------------------------------

void Place::death()
{
  // NB: Don't use a for-loop here, the content of the animals_ list
  // changes as we iterate over animals_
  auto it = animals_.begin();
  while ( it != animals_.end() ) 
  {
    if ( (*it)->dies() ) 
    {
      delete *it;              // delete animal object
      it = animals_.erase(it);  // remove pointer to object from list
    }
    else
    {
      ++it;  // move to next animal in list
    }
  }
}

// -------------------------------------------

void House::feed()
{
  // no food, do nothing
  return;
}

void Pasture::feed()
{
  // offer food to all animals
  for ( auto animal : animals_ )
    animal->eat(50);
  return;
}

void ParkingLot::feed()
{
  // no food, do nothing
  return;
}

// -------------------------------------------
