/*
* LLNS Copyright Start
* Copyright (c) 2018, Lawrence Livermore National Security
* This work was performed under the auspices of the U.S. Department
* of Energy by Lawrence Livermore National Laboratory in part under
* Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
* Produced at the Lawrence Livermore National Laboratory.
* All rights reserved.
* For details, see the LICENSE file.
* LLNS Copyright End
*/
#include <cmath>
#include "Gauss4.h"
namespace griddyn {
namespace paradae {
Gauss4::Gauss4(Equation* eq):RungeKutta_Implicit(eq,false)
{
  nb_steps=2;
  order=4;
  this->InitArray();
  rk_A.Clone(DenseMatrix(nb_steps,Real(0.0)));
  rk_b.Resize(nb_steps);
  rk_binf.Resize(nb_steps);
  rk_c.Resize(nb_steps);

  Real sq3s6=sqrt(3.)/6.;
  rk_A(0,0)=Real(1./4.);rk_A(0,1)=Real(1./4.)-sq3s6;
  rk_A(1,0)=Real(1./4.)+sq3s6;rk_A(1,1)=Real(1./4.);
  rk_b(0)=Real(1./2.);rk_b(1)=Real(1./2.);
  rk_c(0)=Real(1./2.)-sq3s6;rk_c(1)=Real(1./2.)+sq3s6;
}
} // namespace paradae
} // namespace griddyn
