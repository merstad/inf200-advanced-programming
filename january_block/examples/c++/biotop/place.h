/*
  Example of a class with non-trivial destructor and for
  inheritance and polymorphism with the following class structure:


                          Place
                            |
                ------------------------
		|           |          |
              House      Pasture   ParkingLot


  Hans Ekkehard Plesser, 2003-03-10, 2006-04-03, 2021-01-19
*/

#include <list>
#include "animal.h"

class Place {

public:
  
  // Concstructor. No default value for x: we cannot create a
  // Place instance without specifying a location
 Place(unsigned x) : x_(x), animals_() {}

  // Place instances should not be copied or assigned. We forbid
  // this by deleting the copy constructor and assignment operator.
  // Otherwise, C++ would create them by default.
  Place(const Place&) = delete;
  Place& operator=(const Place&) = delete;
  
  // Destructor: needs to delete animal objects
  virtual ~Place();

  // Virtual (overridable) method placing animal in place,
  // returning true if animal is accepted.
  virtual bool place(Animal*);  

  unsigned num_animals() const { return animals_.size(); }

  void death();

  /* Pure virtual function implementing feeding of animals.

     There is no default feeding defined in the base class,
     all derived classes must define this method.
  */
  virtual void feed() =0;

protected:  // Accessible to derived classes
  std::list<Animal*> animals_;

private:
  unsigned       x_;      // x-coordinate
};

// -------------------------------------------

// House: animals not allowed here
class House : public Place {
public:
  House(unsigned x) : Place(x) {}

  bool place(Animal*);
  void feed();
};

// Pasture: animal can be here and find food
class Pasture : public Place {
public:
  Pasture(unsigned x) : Place(x) {}

  // we only override mat(), we inherit place() from the base class
  void feed();
};

// Parking lot: animals can be here but find no food
class ParkingLot : public Place {
public:
  ParkingLot(unsigned x) : Place(x) {}

  // we only override mat(), we inherit place() from the base class
  void feed();
};
