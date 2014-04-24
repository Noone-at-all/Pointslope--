def GCF(arg1, arg2):
    if arg1 < 0:
        arg1 = arg1 * -1
    elif arg2 < 0:
        arg2 = arg2 * -1
    CF = []
    l = 1
    if arg1 > arg2:
        g = arg2
    elif arg2 >= arg1:
        g = arg1
    for item in range(g):
        if arg1 % l == 0 and arg2 % l == 0:
            CF.append(l)
            l += 1
        else:
            l += 1
    CF.sort()
    h = CF[::-1]
    return h[0]
    
def pointslope():
    y1 = int(raw_input('y1?'))
    x1 = int(raw_input('x1?'))
    S = raw_input('Do you have a slope?').lower()
    if S not in 'yn' or S == '':
        print 'Only "y" and "n" are accepted inputs'
        pointslope()
    elif S == 'n':
        y2 = int(raw_input('y2?'))
        x2 = int(raw_input('x2?'))
        motionu = str(y2 - y1)
        motionl = str(x2 - x1)
        motiont = int(y2 - y1) / GCF(int(motionu), int(motionl))
        motionb = int(x2 - x1) / GCF(int(motionu), int(motionl))
        motion = '%s/%s' % (motiont, motionb)
        if x1 - x2 == 0 and y1 - y2 == 0:
            print 'Something happened, you tried to divide 0 by 0.'
            return 'sail'
        elif x1 - x2 == 0:
            print 'Vertical line at x=%s' % (x1)
            return 'wot'
        elif y1 - y2 == 0:
            print 'Horizontal line at y=%s' % (y1)
            return 'wot'
        m = (y2 - y1) / float(x2 - x1)
        u = False
        if m < 0:
            u = True
        S = 'y'
        k = m*x1
        cosa = y1 - k
        print m
        print motion
        print 'Point-slope form: y - %s = %sx - %s' % (y1, motion, k)
        print 'Slope-intercept form: y = %sx + %s' % (motion, cosa)
        if raw_input('Standard form?') == 'y':
            mi = float(motionb)
            cosa = cosa * mi
            if u == True:
                print 'x + %sy = %s' % (mi, cosa)
            else:
                print 'x - %sy = - %s' % (mi, cosa)
        else:
            print 'You\'re done!'
    elif S == 'y':
        upper = int(raw_input('What is the top of your slope?'))
        lower = int(raw_input('What is the bottom of your slope?'))
        top = upper / GCF(upper, lower)
        bottom = lower / GCF(upper, lower)
        m = top / float(bottom)
        h = False
        if m < 0:
            h = True
        slope = '%s/%s' % (str(top), str(bottom))
        k = m*x1
        print 'Point-slope form: y - %s = %sx - %s' % (y1, slope, k)
        cosa = y1 - k
        print 'Slope-intercept form: y = %sx + %s' % (slope, cosa)
        if raw_input('Standard form?') == 'y':
            print 'Assume this is standard form.'
            mi = bottom
            cosa = cosa * mi
            if h == True:
                print 'x + %sy = %s' % (mi, cosa)
            else:
                print 'x - %sy = - %s' % (mi, cosa)
        else:
            print 'You\'re done!'
