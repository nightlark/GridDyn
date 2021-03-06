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
#include "Radau3.h"

// 1/3 | 5/12 -1/12
// 1   | 3/4   1/4
// -----------------
//     | 3/4   1/4
namespace griddyn {
namespace paradae {
Radau3::Radau3(Equation* eq):RungeKutta_Implicit(eq,false)
{
  nb_steps=2;
  order=3;
  this->InitArray();
  rk_A.Clone(DenseMatrix(nb_steps,Real(0.0)));
  rk_b.Resize(nb_steps);
  rk_binf.Resize(nb_steps);
  rk_c.Resize(nb_steps);

  rk_A(0,0)=Real(5./12.);rk_A(0,1)=Real(-1./12.);
  rk_A(1,0)=Real(3./4.);rk_A(1,1)=Real(1./4.);
  rk_b(0)=Real(3./4.);rk_b(1)=Real(1./4.);
  rk_c(0)=Real(1./3.);rk_c(1)=Real(1.);
}
} // namespace paradae
} // namespace griddyn
