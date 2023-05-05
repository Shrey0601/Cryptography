# The code for the function "coppersmith_howgrave_univariate" has been taken from the open-source implementation of the attack: https://github.com/mimoo/RSA-and-LLL-attacks/#coppersmith

e = 5
N = 78714125558938006524263341891637661470621059531118097724645452095297789818891276010645630214833377767004437365131816549623548561938688009253516694435330379062091610989184365198788789234888046760957515418067618141116204483148124743033377595378322100172820821638753951573113884455431885381705501055635435019199
C = 53492016290318493210715432498776825237772044591843427566242802775877352113724490995358632192436585294028774625146463728136078436094684926513796651235534614988872690820243416461533815867105822335860438183971120103180709046611655786471251408575270698016145312280514937178411796861309849520944186887837854305110

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    #
    # init
    #
    dd = pol.degree()
    nn = dd * mm + tt

    #
    # checks
    #
    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1)")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    #
    # calculate bounds and display them
    #
    """
    * we want to find g(x) such that ||g(xX)|| <= b^m / sqrt(n)
    * we know LLL will give us a short vector v such that:
    ||v|| <= 2^((n - 1)/4) * det(L)^(1/n)
    * we will use that vector as a coefficient vector for our g(x)
    
    * so we want to satisfy:
    2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)
    
    so we can obtain ||v|| < N^(beta*m) / sqrt(n) <= b^m / sqrt(n)
    (it's important to use N because we might not know b)
    """
    
    #
    # Coppersmith revisited algo for univariate
    #

    # change ring of pol and x
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # display basis matrix

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    print("potential roots:", potential_roots)

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    # 
    return roots

# RSA known parameters
ZmodN = Zmod(N);


def break_rsa(p_str, max_length_M):
    global e, C, ZmodN

    p_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in p_str])

    for length_M in range(0, max_length_M+1, 4):          # size of the root

        # Problem to equation (default)
        P.<M> = PolynomialRing(ZmodN) #, implementation='NTL'
        pol = ((int(p_binary_str, 2)<<length_M) + M)^e - C
        dd = pol.degree()

        # Tweak those
        beta = 1                                
        epsilon = beta / 7                      
        mm = ceil(beta**2 / (dd * epsilon))     
        tt = floor(dd * mm * ((1/beta) - 1))    
        XX = ceil(N**((beta**2/dd) - epsilon))  

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

        if roots:
            print ("Root is: :", ' {0:b}'.format(roots[0]))
            return

    print ('No solution found\n')

if __name__ == "__main__":
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is: ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS: ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is: ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:  ", 310).
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:  ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:  ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:   ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:   ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:   ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:    ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:    ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:    ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:     ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:     ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:     ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:      ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:      ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:      ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:       ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:       ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:       ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:        ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:        ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:        ", 310)
    break_rsa("sha4269: This door has RSA encryption with exponent 5 and the password is:         ", 310)
    break_rsa("SHA4269: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS:         ", 310)
    break_rsa("sha4269: this door has rsa encryption with exponent 5 and the password is:         ", 310)