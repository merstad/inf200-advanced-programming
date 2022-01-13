#include <cmath>      // for exp
#include "animal.h"   
#include "random.h"

// statiske data members må defineres et sted
double Animal::w_loss_ = 0;
double Animal::w_birth_ = 0;
double Animal::F_     = 0;
double Animal::mu_    = 0;

double Animal::eat(double food)
{
  const double eaten = food < F_ ? food : F_;

  weight_ += eaten;

  return eaten;
}

void Animal::lose_weight()
{
  weight_ *= w_loss_;
}

bool Animal::dies() const
{
  return toolbox::randomGen().drand() < 1 - std::exp(-0.1 * weight_);
}

bool Animal::moves() const
{
  return toolbox::randomGen().drand() < mu_;
}

void Animal::set_params(double w_loss, double w_birth, double F, double mu)
{
  w_loss_ = w_loss;
  w_birth_ = w_birth;
  F_ = F;
  mu_ = mu;
}
