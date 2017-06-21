Bus.con = [ ... 
  1  20  1.03  0.3229  1  1;
  2  20  1.01  0.1536  1  1;
  3  20  1.03  -0.1187  2  1;
  4  20  1.01  -0.295  2  1;
  5  230  1.01  0.2112  1  1;
  6  230  0.9876  0.03665  1  1;
  7  230  1  -0.1065  1  1;
  8  230  1  -0.3368  3  1;
  9  230  0.9899  -0.555  2  1;
  10  230  0.9938  -0.4119  2  1;
  11  230  1.013  -0.2339  2  1;
 ];

Line.con = [ ... 
  5  6  100  230  60  0  0  0.0025  0.025  0.04375  0  0  1  0  0  1;
  6  7  100  230  60  0  0  0.001  0.01  0.0175  0  0  1  0  0  1;
  8  9  100  230  60  0  0  0  0.11  0  0  0  1  0  0  1;
  7  8  100  230  60  0  0  0.011  0.11  0.1925  0  0  1  0  0  1;
  11  10  100  230  60  0  0  0.0025  0.025  0.04375  0  0  1  0  0  1;
  10  9  100  230  60  0  0  0.001  0.01  0.0175  0  0  1  0  0  1;
  9  8  100  230  60  0  0  0.011  0.11  0.1925  0  0  1  0  0  1;
  7  8  100  230  60  0  0  0.011  0.11  0.1925  0  0  1  0  0  1;
  1  5  900  20  60  0  0.08695652  0  0.15  0  0  0  1  0  0  1;
  2  6  900  20  60  0  0.08695652  0  0.15  0  0  0  1  0  0  1;
  4  10  900  20  60  0  0.08695652  0  0.15  0  0  0  1  0  0  1;
  3  11  900  20  60  0  0.08695652  0  0.15  0  0  0  1  0  0  1;
 ];

Breaker.con = [ ... 
  7  8  100  230  60  1  1.05  100  1  0;
 ];

Fault.con = [ ... 
  8  100  230  60  1  1.05  1e-05  0.01;
 ];

SW.con = [ ... 
  3  100  20  1.03  -0.1186824  99  -99  1.1  0.9  7  1  1  1;
 ];

PV.con = [ ... 
  1  100  20  7.35  1.03  5  -2  1.1  0.9  1  1;
  2  100  20  7.35  1.01  5  -2  1.1  0.9  1  1;
  8  100  230  0  0.95  5  -2  1.1  0.9  1  1;
  4  100  20  7.35  1.01  5  -2  1.1  0.9  1  1;
 ];

PQ.con = [ ... 
  9  100  230  18.5535  -2.625  1.05  0.95  0  1;
  7  100  230  10.1535  -1.05  1.05  0.95  0  1;
 ];

Pl.con = [ ... 
  7  100  230  60  0  100  0  0  0  100  1  1;
  9  100  230  60  0  100  0  0  0  100  1  1;
 ];

Syn.con = [ ... 
  1  900  20  60  6  0.2  0.0025  1.8  0.3  0.25  8  0.03  1.7  0.55  0.25  0.4  0.05  13  0  0  0  1  1  0.002  0  0;
  2  900  20  60  6  0.2  0.0025  1.8  0.3  0.25  8  0.03  1.7  0.55  0.25  0.4  0.05  13  0  0  0  1  1  0  0  0;
  3  900  20  60  6  0.2  0.0025  1.8  0.3  0.25  8  0.03  1.7  0.55  0.25  0.4  0.05  12.35  0  0  0  1  1  0  0  0;
  4  900  20  60  6  0.2  0.0025  1.8  0.3  0.25  8  0.03  1.7  0.55  0.25  0.4  0.05  12.35  0  0  0  1  1  0  0  0;
 ];

Tg.con = [ ... 
  1  2  1  0.02  1.2  0.3  10  1  0  12  50  1;
  2  2  1  0.02  1.2  0.3  10  1  0  12  50  1;
  3  2  1  0.01  1.2  0.3  10  1  0  12  50  1;
  4  2  1  0.02  1.2  0.3  10  1  0  12  50  1;
 ];

Exc.con = [ ... 
  1  3  5  -5  200  1  1  1  1  0.001  0.01  0.0006  0.9  1;
  2  3  5  -5  200  1  1  1  1  0.001  0.01  0.0006  0.9  1;
  4  3  5  -5  200  1  1  1  1  0.001  0.01  0.0006  0.9  1;
  3  3  5  -5  200  1  1  1  1  0.001  0.01  0.0006  0.9  1;
 ];

Upfc.con = [ ... 
  3  1  100  230  60  30  75  0.005  0.2  -0.2  0.2  -0.2  3  -1  1  0  0  1;
 ];

Pod.con = [ ... 
  4  1  4  5  0.12  -0.12  -0.577  10  0.3187  0.1928  0.3187  0.1928  0.001  1;
 ];

Bus.names = {... 
  'Bus 01'; 'Bus 02'; 'Bus 03'; 'Bus 04'; 'Bus 05'; 
  'Bus 06'; 'Bus 07'; 'Bus 08'; 'Bus 09'; 'Bus 10'; 
  'Bus 11'};
