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
        motiont = str(y2 - y1)
        motionb = str(x2 - x1)
        motion = '%s/%s' % (motiont, motionb)
        if x1 - x2 == 0:
            print 'Vertical line at x=%s' % (x1)
            return 'wot'
        elif y1 - y2 == 0:
            print 'Horizontal line at y=%s' % (y1)
            return 'wot'
        m = (y2 - y1) / float(x2 - x1)
        u = False
        if m < 0:
            u = True
        print m
        print motion
        S = 'y'
        k = m*x1
        cosa = y1 - k
        print 'Point-slope form: y - %s = %sx - %s' % (y1, motion, k)
        print 'Slope-intercept form: y = %sx - %s' % (motion, cosa)
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
        top = int(raw_input('What is the top of your slope?'))
        bottom = int(raw_input('What is the bottom of your slope?'))
        m = top / float(bottom)
        h = False
        if m < 0:
            h = True
        slope = '%s/%s' % (str(top), str(bottom))
        k = m*x1
        print 'Point-slope form: y - %s = %sx - %s' % (y1, slope, k)
        cosa = y1 - k
        print 'Slope-intercept form: y = %sx - %s' % (slope, cosa)
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

