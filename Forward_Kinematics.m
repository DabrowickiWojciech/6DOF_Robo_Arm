syms f1 f2 f3 f4 f5 f6 a1 a2 a3 a4 a5 a6 d1 d2 d3 d4 d5 d6 r1 r2 r3 r4 r5 r6

%%
%Tu wpisujemy dane do obrotu maszyny patrzec na obrazek zawarty w plikach .jpg
f1t=0; 
f2t=0; 
f3t=0; 
f4t=0;
f5t=0;
f6t=0;

f1=(f1t*pi)/180;
f2=((f2t-90)*pi)/180;
f3=(f3t*pi)/180;
f4=((f4t+180)*pi)/180;
f5=((f5t+180)*pi)/180;
f6=(f6t*pi)/180;

%%
a1=(90*pi)/180;
a2=0;
a3=(90*pi)/180;
a4=(-90*pi)/180;
a5=(90*pi)/180;
a6=0;

d1=-70;
d2=0;
d3=0;
d4=-227;
d5=0;
d6=10;

r1=0;
r2=160;
r3=0;
r4=0;
r5=0;
r6=0;

%%
A1 = [cos(f1), -sin(f1)*cos(a1), sin(f1)*sin(a1), r1*cos(f1); sin(f1), cos(f1)*cos(a1), -cos(f1)*sin(a1), r1*sin(f1); 0, sin(a1), cos(a1), d1; 0, 0, 0, 1];
A2 = [cos(f2), -sin(f2)*cos(a2), sin(f2)*sin(a2), r2*cos(f2); sin(f2), cos(f2)*cos(a2), -cos(f2)*sin(a2), r2*sin(f2); 0, sin(a2), cos(a2), d2; 0, 0, 0, 1];
A3 = [cos(f3), -sin(f3)*cos(a3), sin(f3)*sin(a3), r3*cos(f3); sin(f3), cos(f3)*cos(a3), -cos(f3)*sin(a3), r3*sin(f3); 0, sin(a3), cos(a3), d3; 0, 0, 0, 1];
A4 = [cos(f4), -sin(f4)*cos(a4), sin(f4)*sin(a4), r4*cos(f4); sin(f4), cos(f4)*cos(a4), -cos(f4)*sin(a4), r4*sin(f4); 0, sin(a4), cos(a4), d4; 0, 0, 0, 1];
A5 = [cos(f5), -sin(f5)*cos(a5), sin(f5)*sin(a5), r5*cos(f5); sin(f5), cos(f5)*cos(a5), -cos(f5)*sin(a5), r5*sin(f5); 0, sin(a5), cos(a5), d5; 0, 0, 0, 1];
A6 = [cos(f6), -sin(f6)*cos(a6), sin(f6)*sin(a6), r6*cos(f6); sin(f6), cos(f6)*cos(a6), -cos(f6)*sin(a6), r6*sin(f6); 0, sin(a6), cos(a6), d6; 0, 0, 0, 1];
A03 = A1*A2*A3;
A06 = A1*A2*A3*A4*A5*A6;

%%
%A1 = [cos(f1), -sin(f1)*cos(a1), sin(f1)*sin(a1), r1*cos(f1); sin(f1), cos(f1)*cos(a1), -cos(f1)*sin(a1), r1*sin(f1); 0, sin(a1), cos(a1), d1; 0, 0, 0, 1];
%A2 = [cos(f2), -sin(f2)*cos(a2), sin(f2)*sin(a2), r2*cos(f2); sin(f2), cos(f2)*cos(a2), -cos(f2)*sin(a2), r2*sin(f2); 0, sin(a2), cos(a2), d2; 0, 0, 0, 1];
%A3 = [cos(f3), -sin(f3)*cos(a3), sin(f3)*sin(a3), r3*cos(f3); sin(f3), cos(f3)*cos(a3), -cos(f3)*sin(a3), r3*sin(f3); 0, sin(a3), cos(a3), d3; 0, 0, 0, 1];
%A4 = [cos(f4), -sin(f4)*cos(a4), sin(f4)*sin(a4), r4*cos(f4); sin(f4), cos(f4)*cos(a4), -cos(f4)*sin(a4), r4*sin(f4); 0, sin(a4), cos(a4), d4; 0, 0, 0, 1];
%A5 = [cos(f5), -sin(f5)*cos(a5), sin(f5)*sin(a5), r5*cos(f5); sin(f5), cos(f5)*cos(a5), -cos(f5)*sin(a5), r5*sin(f5); 0, sin(a5), cos(a5), d5; 0, 0, 0, 1];
%A6 = [cos(f6), -sin(f6)*cos(a6), sin(f6)*sin(a6), r6*cos(f6); sin(f6), cos(f6)*cos(a6), -cos(f6)*sin(a6), r6*sin(f6); 0, sin(a6), cos(a6), d6; 0, 0, 0, 1];

