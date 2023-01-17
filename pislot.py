def func1(arg1, arg2):
    def func2(arg3, arg4):
        var9 = func3(arg1, arg4)
        var19 = var12(arg3, arg2)
        var24 = func7(arg4, arg3)
        var25 = var24 + ((var9 & arg2) & arg2)
        var26 = arg4 | var24
        var27 = var26 + 174
        var28 = var27 | arg1
        if var19 < var24:
            var29 = var25 | var9 ^ arg4 | arg2
        else:
            var29 = var28 | var25
        var30 = (arg1 + var19) & arg4
        var31 = ((var24 - var24) ^ var28) + var25
        if var26 < arg2:
            var32 = (var30 | (var19 ^ var28)) - var25
        else:
            var32 = var25 + var31
        var33 = arg2 + -586
        var34 = var25 + -206 ^ arg3 + arg1
        var35 = arg2 - var25 ^ arg1 - 923
        result = arg1 ^ (-1894139639 | var24) + var30
        return result
    var36 = func2(arg2, arg1)
    var37 = func10()
    var38 = var36 - var36
    var39 = -839 - -1166343750
    if arg1 < var36:
        var40 = arg1 & 374 | var39
    else:
        var40 = -458 - var38
    var41 = var39 | var37 & arg1 + arg1
    var42 = ((arg1 - var36) ^ var38) + var41
    var43 = arg1 & (arg1 | var41) | var37
    var44 = (arg2 + var41) ^ var42 ^ var37
    var45 = var41 + -785 - var39 ^ var43
    var46 = var36 + var39 ^ var45 + -1359299653
    var47 = var43 & arg2 - arg2 & var36
    var48 = arg2 ^ 386
    result = arg1 & (arg1 & (var47 - (var43 & var39)))
    return result
def func10():
    func8()
    result = len(xrange(29))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : 4
def func7(arg20, arg21):
    var22 = 0
    for var23 in xrange(12):
        if var23 < arg20:
            var22 += arg21 ^ arg21 | arg20
        else:
            var22 += var22 & (arg21 ^ var22)
    return var22
def func6(arg13, arg14):
    var15 = arg14 & 813 + arg14 + arg13 ^ (arg14 - arg13 + 358216279) + -562 - (arg14 | 417 ^ arg13 & arg13 - (1923414263 | (((arg13 - 1499672486) & arg13) & arg14)) + 2058481551 | arg13 ^ 1519372010 - arg14 ^ arg13)
    var16 = var15 + ((((arg13 & (var15 - arg14 - ((var15 | arg13 - arg14 & -520 | arg14) - (arg14 | (arg14 - -777 + 645) ^ arg14 & arg13)))) - (arg14 + arg14) ^ var15) & arg14) ^ (arg13 & (arg14 ^ arg14)))
    var17 = -467 & -516411786
    var18 = (var16 ^ ((-57 ^ arg13 + (678 + arg13 + arg13 & var17)) - (var17 - (1579617236 & 941 ^ arg14 ^ arg13 ^ var16 & 36 - (var15 & var15 - var15) ^ -1274509977))) - arg14) + -1813747918 + -1782385539 | 219
    result = arg14 | var16
    return result
def func5():
    closure = [-7]
    def func4(arg10, arg11):
        closure[0] += func6(arg10, arg11)
        return closure[0]
    func = func4
    return func
var12 = func5()
def func3(arg5, arg6):
    var7 = 0
    for var8 in range(12):
        var7 += var8 - (arg6 - var8)
    return var7
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 49'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
