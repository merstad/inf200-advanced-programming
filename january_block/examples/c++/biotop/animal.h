#ifndef ANIMAL_H
#define ANIMAL_H

/*
  Class representing an animal

  Hans Ekkehard Plesser, 2003-03-10, 2006-04-03, 2021-01-19

  Declaration of class Animal
*/

class Animal {

public:

  // constructor: animal created with given weight
  Animal(double weight = w_birth_) : weight_(weight) {} 

  ~Animal() {}  // destruktør

  // return how much you have eaten
  double eat(double food = 0);
  void lose_weight();
  double get_weight() const { return weight_; }

  bool dies() const;   // true if animal dies
  bool moves() const;  // true if animal wants to move


  // static member function: function for entire class
  static void set_params(double w_birth, double w_loss, double F, double mu);

private:

  double weight_;  // member variable (attribute) of individual animal
   
  // class variables, apply to all animals
  static double w_loss_;   // annual weight loss
  static double w_birth_;  // weight at birth
  static double F_;        // appetite 
  static double mu_;       // mobility parameter
};

#endif

