from numpy import sin, cos, array, pi, arctan2, sqrt


def _forward_kinematics(f1input,f2input,f3input,f4input,f5input,f6input,d1,d2,d3,d4,d5,d6,r1,r2,r3,r4,r5,r6):
    
    f1 = (f1input*pi)/180
    f2 = ((f2input-90)*pi)/180
    f3 = (f3input*pi)/180
    f4 = ((f4input+180)*pi)/180
    f5 = ((f5input+180)*pi)/180
    f6 = (f6input*pi)/180
    
    #parameters of length of robotic arm
    #changes of axis (redirections of joints, check notes)
    a1 = (90*pi)/180
    a2 = 0
    a3 = (90*pi)/180
    a4 = (-90*pi)/180
    a5 = (90*pi)/180
    a6 = 0

    #universal code for forward kinematics
    A06 = array([[sin(f6)*(sin(a4)*sin(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) - cos(f4)*sin(a1)*sin(a4)*sin(f1)) + cos(f6)*(cos(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) - sin(f5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2))), cos(a6)*cos(f6)*(sin(a4)*sin(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) - cos(f4)*sin(a1)*sin(a4)*sin(f1)) - cos(a6)*sin(f6)*(cos(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) - sin(f5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2))), sin(a5)*sin(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) + cos(f5)*sin(a5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2)), d4*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2)) + d5*(sin(a4)*sin(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) - cos(f4)*sin(a1)*sin(a4)*sin(f1)) + r1*cos(f1) + d6*(sin(a5)*sin(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) + cos(f5)*sin(a5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2))) - r5*sin(f5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2)) + r4*cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + r2*cos(f1)*cos(f2) + d2*sin(a1)*sin(f1) + d3*sin(a1)*sin(f1) + r6*sin(f6)*(sin(a4)*sin(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) - cos(f4)*sin(a1)*sin(a4)*sin(f1)) + r5*cos(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) + r6*cos(f6)*(cos(f5)*(cos(f4)*(cos(f1)*cos(f2)*cos(f3) - cos(a2)*cos(f1)*sin(f2)*sin(f3)) + sin(a1)*sin(f1)*sin(f4)) - sin(f5)*(cos(f1)*cos(f2)*sin(a3)*sin(f3) + cos(a2)*cos(f1)*cos(f3)*sin(a3)*sin(f2))) + r3*cos(f1)*cos(f2)*cos(f3) + r4*sin(a1)*sin(f1)*sin(f4) - r3*cos(a2)*cos(f1)*sin(f2)*sin(f3)],
    [sin(f6)*(sin(a4)*sin(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) + cos(f1)*cos(f4)*sin(a1)*sin(a4)) + cos(f6)*(cos(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) - sin(f5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2))), cos(a6)*cos(f6)*(sin(a4)*sin(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) + cos(f1)*cos(f4)*sin(a1)*sin(a4)) - cos(a6)*sin(f6)*(cos(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) - sin(f5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2))), sin(a5)*sin(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) + cos(f5)*sin(a5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2)), d4*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2)) + d5*(sin(a4)*sin(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) + cos(f1)*cos(f4)*sin(a1)*sin(a4)) + r1*sin(f1) + d6*(sin(a5)*sin(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) + cos(f5)*sin(a5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2))) + r6*cos(f6)*(cos(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) - sin(f5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2))) - r5*sin(f5)*(cos(f2)*sin(a3)*sin(f1)*sin(f3) + cos(a2)*cos(f3)*sin(a3)*sin(f1)*sin(f2)) - d2*cos(f1)*sin(a1) - d3*cos(f1)*sin(a1) + r2*cos(f2)*sin(f1) + r4*cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) + r6*sin(f6)*(sin(a4)*sin(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) + cos(f1)*cos(f4)*sin(a1)*sin(a4)) + r5*cos(f5)*(cos(f4)*(cos(f2)*cos(f3)*sin(f1) - cos(a2)*sin(f1)*sin(f2)*sin(f3)) - cos(f1)*sin(a1)*sin(f4)) + r3*cos(f2)*cos(f3)*sin(f1) - r4*cos(f1)*sin(a1)*sin(f4) - r3*cos(a2)*sin(f1)*sin(f2)*sin(f3)],
    [                                                                                                                sin(a4)*sin(f4)*sin(f6)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)) - cos(f6)*(sin(f5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) - cos(f4)*cos(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3))),                                                                                                                 cos(a6)*sin(f6)*(sin(f5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) - cos(f4)*cos(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3))) + cos(a6)*cos(f6)*sin(a4)*sin(f4)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)),                                                             cos(f5)*sin(a5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) + cos(f4)*sin(a5)*sin(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)),                                                                                                                                                                                                                                                                                                                                                                                                                                    d1 + d4*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) + r2*sin(f2) + d6*(cos(f5)*sin(a5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) + cos(f4)*sin(a5)*sin(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3))) - r6*cos(f6)*(sin(f5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) - cos(f4)*cos(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3))) + r3*cos(f3)*sin(f2) - r5*sin(f5)*(sin(a3)*sin(f2)*sin(f3) - cos(a2)*cos(f2)*cos(f3)*sin(a3)) + r4*cos(f4)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)) + r3*cos(a2)*cos(f2)*sin(f3) + r5*cos(f4)*cos(f5)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)) + d5*sin(a4)*sin(f4)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3)) + r6*sin(a4)*sin(f4)*sin(f6)*(cos(f3)*sin(f2) + cos(a2)*cos(f2)*sin(f3))],
    [                                                                                                                                                                                     0,                                                                                                                                                                                            0,                0,                                                                                                                                                                                            1]])
 

    #print(f"{A06}\n")
    for i in range (0,3):
        for j in range (0,3):
            if A06[i][j] < 1e-13:
                A06[i][j] = 0
        j = 0
    i = 0
    #print(f"{A06}\n")
                
    xout = abs(round(A06[0][3],4))
    yout = abs(round(A06[1][3],4))
    zout = abs(round(A06[2][3],4))
    
    print(f"x value : {xout}mm \ny value : {yout}mm \nz value :{zout}mm \n")

    return(xout,yout,zout)

def _inverse_kinematics(xinput,yinput,zinput,d1,d2,d4,r1,r2,r4,):
    
    l1 = abs(d1+r1)
    l2 = abs(d2+r2)
    l4 = abs(d4+r4)
    
    # Compute the joint angles
    f1out = arctan2(yinput, xinput)
    
    d = sqrt(xinput**2 + yinput**2) - l1
    r = sqrt(d**2 + zinput**2)
    D = (l2**2 - l4**2 + r**2) / (2 * l2 * r)

    f3out = arctan2(-sqrt(1 - D**2), D) + arctan2(d, zinput)
    
    gamma = arctan2(-l4, l2)
    alpha = arctan2(r * sin(f3out - gamma), d + r * cos(f3out - gamma))
    beta = arccos((l2**2 + r**2 - l4**2) / (2 * l2 * r))
    f2out = pi/2 - (alpha + beta)
    
    f4out = arctan2(-sin(f2out + f3out), cos(f2out + f3out))
    
    # Assuming a fixed orientation for the last two joints
    f5out = 0.0
    f6out = 0.0
    
    #changing radians to degrees
    f1out = f1out * 57.2957795
    f2out = f2out * 57.2957795
    f3out = f3out * 57.2957795
    f4out = f4out * 57.2957795
    f5out = f5out * 57.2957795
    f6out = f6out * 57.2957795
    
    return(f1out,f2out,f3out,f4out,f5out,f6out)


def main():
    #x = (float)(input("Enter a value of x : "))
    #y = (float)(input("Enter a value of y : "))
    #z = (float)(input("Enter a value of z : "))
    
    #########Forward_Kinematics ############
    #values of angles that you want
    f1user = 45
    f2user = 30
    f3user = -60
    f4user = 0
    f5user = 0
    f6user = 0
    
    #length of the arm (check notes)
    d1 = -70 
    d2 = 0 
    d3 = 0
    d4 = -227
    d5 = 0
    d6 = 10
    
    r1 = 0
    r2 = 160
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    
    x,y,z = _forward_kinematics(f1user,f2user,f3user,f4user,f5user,f6user,d1,d2,d3,d4,d5,d6,r1,r2,r3,r4,r5,r6)
    
    f1,f2,f3,f4,f5,f6 = _inverse_kinematics(x,y,z,d1,d2,d4,r1,r2,r4)

    print(f"f1 : {f1}\n f2 : {f2}\n f3 : {f3}\n f4 : {f4}\n f5 : {f5}\n f6 : {f6}\n ")
    
if __name__ == "__main__":
    main()
    
