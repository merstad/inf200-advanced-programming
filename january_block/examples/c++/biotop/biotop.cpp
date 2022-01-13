/*
  A program illustrating inheritance

  Programmet viser en endimensjonal verden med
  tre landskapstyper, men uten bevegelse.

  Hans Ekkehard Plesser, 2003-03-25, 2006-04-03
*/

#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

#include "random.h"
#include "animal.h"
#include "place.h"

using namespace std;

typedef vector<Place*> lp_vec;

int main(int argc, char *argv[])
{
  
  if ( argc != 5 ) {
    cout << "\n Usage: biotop world numAnimals numYear seed\n" << endl;
    return -1;
  }

  string geography(argv[1]);
  unsigned int n_animals = atoi(argv[2]);
  unsigned int n_year = atoi(argv[3]);

  toolbox::randomGen(atoi(argv[4])); // seed

  // build world from geography string:
  // each character in the string is one cell
  // initialize with zero-pointers
  lp_vec world(geography.size(), 0);

  for ( unsigned int c = 0 ; c < geography.size() ; ++c )
    {
      switch ( geography[c] ) {
      case 'H':
	world[c] = new House(c);
	break;
      case 'P':
	world[c] = new Pasture(c);
	break;
      case 'L':
	world[c] = new ParkingLot(c);
	break;
      default:
	cout << "\nError: geography description can only contain H, P, L\n"
	     << endl;
	return -2;
	break;
      }
    }

  // set class parameters
 Animal::set_params(5, 0.5, 10, 0.2);

  // fill cells with animals
  for ( auto cell : world )
    {
      auto n = toolbox::randomGen().nrand(n_animals + 1);
      for ( unsigned int j = 0 ; j < n ; ++j )
	{
	  Animal *new_animal = new Animal;
	  if ( not cell->place(new_animal) )
	    delete new_animal;
	}
    }

  // simulate
  unsigned int year = 0;
  cout << endl;

  do {

    // print out year and number of animals in each cell
    cout << setw(3) << year << " : ";

    unsigned int total = 0;
    for ( auto cell : world )
      {
	cout << setw(3) << cell->num_animals();
	total += cell->num_animals();
      }

    cout << "   [" << setw(3) << total << "]" << endl;

    // feeding and death
    for ( auto cell : world )
      cell->feed();

    for ( auto cell : world )
      cell->death();
    
    ++year;

  } while ( year < n_year );

  cout << "\nFarewell!\n" << endl;
  
  return 0;

}
